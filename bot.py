"""
Goldpatent Telegram Bot
Tovar belgisi davlat bojini hisoblash + bog'lanish
"""

import os
import logging
import asyncio
from datetime import datetime
from typing import Dict, Any

from telegram import (
    Update, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
    BotCommand
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
    ConversationHandler
)
from telegram.constants import ParseMode

from data.translations import get_text, TRANSLATIONS
from data.tariffs import calculate_total, format_money
from data.classes import NICE_CLASSES, search_classes, get_class_by_number, get_classes_by_type
from utils.security import (
    check_rate_limit, 
    validate_name, 
    validate_phone, 
    sanitize_text
)

# ============================================
# LOGGING SOZLAMALARI
# ============================================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)

# ============================================
# KONFIGURATSIYA (environment variables)
# ============================================
BOT_TOKEN = os.getenv("BOT_TOKEN", "8240102163:AAFKPXaeYltJVV1NAsjJanemdBeHQ08nwk4")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", "1223964472"))

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

# ============================================
# CONVERSATION STATES
# ============================================
# Calculator states
CALC_APPLICANT, CALC_MARK_TYPE, CALC_CLASSES, CALC_STAGES = range(4)
# Contact states
CONTACT_NAME, CONTACT_PHONE, CONTACT_BRAND, CONTACT_MESSAGE = range(4, 8)
# Search state
SEARCH_INPUT = 8


# ============================================
# YORDAMCHI FUNKSIYALAR
# ============================================
def get_user_lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    """Foydalanuvchi tilini olish"""
    return context.user_data.get('lang', 'uz')


def t(context: ContextTypes.DEFAULT_TYPE, key: str) -> str:
    """Tarjima olish (qisqartma)"""
    return get_text(get_user_lang(context), key)


async def check_rate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Rate limit tekshirish - True qaytarsa davom etish mumkin"""
    user_id = update.effective_user.id
    allowed, wait = check_rate_limit(user_id)
    
    if not allowed:
        msg = t(context, "error_rate_limit")
        if update.message:
            await update.message.reply_text(f"{msg}\n({wait}s)")
        elif update.callback_query:
            await update.callback_query.answer(f"{msg} ({wait}s)", show_alert=True)
        return False
    
    return True


# ============================================
# MAIN MENU
# ============================================
def get_main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Asosiy menyu klaviaturasi"""
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_calculator"), callback_data="menu_calc")],
        [InlineKeyboardButton(get_text(lang, "btn_classes"), callback_data="menu_classes")],
        [InlineKeyboardButton(get_text(lang, "btn_contact"), callback_data="menu_contact")],
        [InlineKeyboardButton(get_text(lang, "btn_faq"), callback_data="menu_faq")],
        [InlineKeyboardButton(get_text(lang, "btn_about"), callback_data="menu_about")],
        [InlineKeyboardButton(get_text(lang, "btn_change_lang"), callback_data="menu_lang")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_lang_keyboard() -> InlineKeyboardMarkup:
    """Til tanlash klaviaturasi"""
    keyboard = [
        [InlineKeyboardButton("🇺🇿 Oʻzbek", callback_data="lang_uz")],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_back_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Orqaga qaytish tugmasi"""
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)


# ============================================
# /start COMMAND
# ============================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot boshlanishi"""
    if not await check_rate(update, context):
        return
    
    user = update.effective_user
    logger.info(f"User {user.id} ({user.first_name}) started the bot")
    
    # Birinchi marta bo'lsa, til tanlashga taklif
    if 'lang' not in context.user_data:
        await update.message.reply_text(
            get_text("uz", "welcome"),
            reply_markup=get_lang_keyboard(),
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        # Til tanlangan bo'lsa, asosiy menyu
        lang = get_user_lang(context)
        await update.message.reply_text(
            get_text(lang, "main_menu_title"),
            reply_markup=get_main_menu_keyboard(lang),
            parse_mode=ParseMode.MARKDOWN
        )


# ============================================
# LANGUAGE SELECTION
# ============================================
async def lang_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Til tanlash"""
    if not await check_rate(update, context):
        return
    
    query = update.callback_query
    await query.answer()
    
    lang = query.data.replace("lang_", "")
    if lang not in TRANSLATIONS:
        lang = "uz"
    
    context.user_data['lang'] = lang
    logger.info(f"User {query.from_user.id} selected language: {lang}")
    
    await query.edit_message_text(
        get_text(lang, "main_menu_title"),
        reply_markup=get_main_menu_keyboard(lang),
        parse_mode=ParseMode.MARKDOWN
    )


# ============================================
# MAIN MENU HANDLER
# ============================================
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Asosiy menyuga qaytish"""
    if not await check_rate(update, context):
        return
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    
    # Calculator/contact data ni tozalash
    for key in ['calc_data', 'contact_data', 'contact_type']:
        context.user_data.pop(key, None)
    
    await query.edit_message_text(
        get_text(lang, "main_menu_title"),
        reply_markup=get_main_menu_keyboard(lang),
        parse_mode=ParseMode.MARKDOWN
    )


async def menu_lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Til o'zgartirish menyusi"""
    if not await check_rate(update, context):
        return
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    await query.edit_message_text(
        get_text(lang, "welcome"),
        reply_markup=get_lang_keyboard(),
        parse_mode=ParseMode.MARKDOWN
    )


# ============================================
# CALCULATOR
# ============================================
async def calc_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kalkulyatorni boshlash"""
    if not await check_rate(update, context):
        return ConversationHandler.END
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    context.user_data['calc_data'] = {}
    
    keyboard = [
        [
            InlineKeyboardButton(get_text(lang, "calc_individual"), callback_data="calc_app_individual"),
            InlineKeyboardButton(get_text(lang, "calc_legal"), callback_data="calc_app_legal")
        ],
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    await query.edit_message_text(
        get_text(lang, "calc_step1"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    return CALC_APPLICANT


async def calc_applicant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Arizachi turi tanlandi"""
    query = update.callback_query
    await query.answer()
    
    applicant = query.data.replace("calc_app_", "")
    context.user_data['calc_data']['applicant'] = applicant
    
    lang = get_user_lang(context)
    
    keyboard = [
        [
            InlineKeyboardButton(get_text(lang, "calc_ordinary"), callback_data="calc_mark_ordinary"),
            InlineKeyboardButton(get_text(lang, "calc_collective"), callback_data="calc_mark_collective")
        ],
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    await query.edit_message_text(
        get_text(lang, "calc_step2"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    return CALC_MARK_TYPE


async def calc_mark_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Belgi turi tanlandi"""
    query = update.callback_query
    await query.answer()
    
    mark_type = query.data.replace("calc_mark_", "")
    context.user_data['calc_data']['mark_type'] = mark_type
    
    lang = get_user_lang(context)
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    await query.edit_message_text(
        get_text(lang, "calc_step3"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    return CALC_CLASSES


async def calc_classes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sinflar soni"""
    if not update.message:
        return CALC_CLASSES
    
    if not await check_rate(update, context):
        return CALC_CLASSES
    
    lang = get_user_lang(context)
    text = update.message.text.strip()
    
    try:
        classes = int(text)
        if classes < 1 or classes > 45:
            raise ValueError()
    except ValueError:
        await update.message.reply_text(
            get_text(lang, "calc_step3_invalid"),
            parse_mode=ParseMode.MARKDOWN
        )
        return CALC_CLASSES
    
    context.user_data['calc_data']['classes'] = classes
    context.user_data['calc_data']['stages'] = []
    
    await update.message.reply_text(
        get_text(lang, "calc_step4"),
        reply_markup=get_stages_keyboard(lang, []),
        parse_mode=ParseMode.MARKDOWN
    )
    return CALC_STAGES


def get_stages_keyboard(lang: str, selected: list) -> InlineKeyboardMarkup:
    """Bosqichlar uchun klaviatura"""
    stages = [
        ("application", "calc_stage_application"),
        ("express", "calc_stage_express"),
        ("certificate", "calc_stage_certificate"),
        ("extension", "calc_stage_extension")
    ]
    
    keyboard = []
    for stage_id, text_key in stages:
        prefix = "✅ " if stage_id in selected else "☐ "
        keyboard.append([
            InlineKeyboardButton(
                prefix + get_text(lang, text_key),
                callback_data=f"calc_stage_{stage_id}"
            )
        ])
    
    keyboard.append([
        InlineKeyboardButton(get_text(lang, "calc_btn_done"), callback_data="calc_done"),
        InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")
    ])
    
    return InlineKeyboardMarkup(keyboard)


async def calc_toggle_stage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bosqichni belgilash/olib tashlash"""
    query = update.callback_query
    await query.answer()
    
    stage = query.data.replace("calc_stage_", "")
    selected = context.user_data['calc_data'].get('stages', [])
    
    if stage in selected:
        selected.remove(stage)
    else:
        selected.append(stage)
    
    context.user_data['calc_data']['stages'] = selected
    lang = get_user_lang(context)
    
    await query.edit_message_text(
        get_text(lang, "calc_step4"),
        reply_markup=get_stages_keyboard(lang, selected),
        parse_mode=ParseMode.MARKDOWN
    )
    return CALC_STAGES


async def calc_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hisoblash"""
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    data = context.user_data.get('calc_data', {})
    stages = data.get('stages', [])
    
    if not stages:
        await query.answer(get_text(lang, "calc_no_stages"), show_alert=True)
        return CALC_STAGES
    
    # Hisoblash
    result = calculate_total(
        stages=stages,
        applicant=data['applicant'],
        mark_type=data['mark_type'],
        classes=data['classes']
    )
    
    # Natija matnini tayyorlash
    text_parts = [
        get_text(lang, "calc_result_title"),
        "",
        f"*{get_text(lang, 'calc_applicant')}:* {get_text(lang, 'calc_' + data['applicant'])}",
        f"*{get_text(lang, 'calc_mark_type')}:* {get_text(lang, 'calc_' + data['mark_type'])}",
        f"*{get_text(lang, 'calc_classes')}:* {data['classes']}",
        "",
        get_text(lang, "calc_breakdown"),
    ]
    
    for item in result['breakdown']:
        stage_name = get_text(lang, f"calc_stage_{item['stage']}")
        text_parts.append(f"• {stage_name}: *{format_money(item['amount'])}* {get_text(lang, 'calc_currency')}")
    
    text_parts.extend([
        "",
        "━━━━━━━━━━━━━━━",
        f"{get_text(lang, 'calc_total')}: *{format_money(result['total'])}* {get_text(lang, 'calc_currency')}",
        "━━━━━━━━━━━━━━━",
        "",
        get_text(lang, "calc_warning")
    ])
    
    result_text = "\n".join(text_parts)
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "calc_btn_apply"), callback_data="menu_contact")],
        [InlineKeyboardButton(get_text(lang, "calc_btn_recalc"), callback_data="menu_calc")],
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    await query.edit_message_text(
        result_text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    
    return ConversationHandler.END


# ============================================
# CLASSES (45 ta klass)
# ============================================
async def classes_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Klasslar menyusi"""
    if not await check_rate(update, context):
        return
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "classes_btn_goods"), callback_data="classes_goods")],
        [InlineKeyboardButton(get_text(lang, "classes_btn_services"), callback_data="classes_services")],
        [InlineKeyboardButton(get_text(lang, "classes_btn_search"), callback_data="classes_search")],
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    await query.edit_message_text(
        get_text(lang, "classes_title"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )


async def classes_show_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tovarlar yoki xizmatlar ro'yxatini ko'rsatish"""
    if not await check_rate(update, context):
        return
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    
    if query.data == "classes_goods":
        classes = get_classes_by_type("tovar")
        title = get_text(lang, "classes_btn_goods")
    else:
        classes = get_classes_by_type("xizmat")
        title = get_text(lang, "classes_btn_services")
    
    text_parts = [f"*{title}*\n"]
    for cls in classes:
        name = cls[1].get(lang, cls[1]["uz"])
        text_parts.append(f"*{cls[0]}.* {name}")
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "classes_btn_search"), callback_data="classes_search")],
        [InlineKeyboardButton(get_text(lang, "btn_back"), callback_data="menu_classes")],
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    await query.edit_message_text(
        "\n".join(text_parts),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )


async def classes_search_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Klasslarda qidirishni boshlash"""
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    context.user_data['searching_classes'] = True
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_back"), callback_data="menu_classes")]
    ]
    
    await query.edit_message_text(
        get_text(lang, "classes_search_prompt"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )


async def classes_search_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Qidiruv natijasini ko'rsatish"""
    if not update.message or not context.user_data.get('searching_classes'):
        return
    
    if not await check_rate(update, context):
        return
    
    lang = get_user_lang(context)
    query_text = sanitize_text(update.message.text, max_length=50)
    
    results = search_classes(query_text, lang)
    
    if not results:
        keyboard = [
            [InlineKeyboardButton(get_text(lang, "classes_btn_search_more"), callback_data="classes_search")],
            [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
        ]
        await update.message.reply_text(
            get_text(lang, "classes_no_results"),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return
    
    # Natijalarni ko'rsatish
    text_parts = [f"*{get_text(lang, 'classes_results_title')}* ({len(results)})\n"]
    
    for cls in results[:15]:  # Maksimum 15 ta
        type_label = (get_text(lang, "classes_type_goods") if cls[3] == "tovar" 
                      else get_text(lang, "classes_type_services"))
        name = cls[1].get(lang, cls[1]["uz"])
        desc = cls[2].get(lang, cls[2]["uz"])
        text_parts.append(f"\n{type_label} *{cls[0]}-sinf:* {name}\n_{desc}_")
    
    if len(results) > 15:
        text_parts.append(f"\n_...va yana {len(results) - 15} ta natija_")
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "classes_btn_search_more"), callback_data="classes_search")],
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    context.user_data.pop('searching_classes', None)
    
    await update.message.reply_text(
        "\n".join(text_parts),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )


# ============================================
# CONTACT FORM
# ============================================
async def contact_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bog'lanish menyusi"""
    if not await check_rate(update, context):
        return
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "contact_btn_search"), callback_data="contact_start_search")],
        [InlineKeyboardButton(get_text(lang, "contact_btn_consult"), callback_data="contact_start_consult")],
        [InlineKeyboardButton(get_text(lang, "contact_btn_help"), callback_data="contact_start_help")],
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    text = get_text(lang, "contact_menu") + "\n\n" + get_text(lang, "contact_direct")
    
    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )


async def contact_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Aloqa formasini boshlash"""
    if not await check_rate(update, context):
        return ConversationHandler.END
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    contact_type = query.data.replace("contact_start_", "")
    
    context.user_data['contact_type'] = contact_type
    context.user_data['contact_data'] = {}
    
    intro_key = f"contact_{contact_type}_intro"
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_cancel"), callback_data="main_menu")]
    ]
    
    await query.edit_message_text(
        get_text(lang, intro_key),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    return CONTACT_NAME


async def contact_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ism qabul qilish"""
    if not update.message:
        return CONTACT_NAME
    
    if not await check_rate(update, context):
        return CONTACT_NAME
    
    lang = get_user_lang(context)
    name = update.message.text
    
    is_valid, cleaned = validate_name(name)
    if not is_valid:
        await update.message.reply_text(
            get_text(lang, "contact_invalid_name"),
            parse_mode=ParseMode.MARKDOWN
        )
        return CONTACT_NAME
    
    context.user_data['contact_data']['name'] = cleaned
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_cancel"), callback_data="main_menu")]
    ]
    
    await update.message.reply_text(
        get_text(lang, "contact_ask_phone"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    return CONTACT_PHONE


async def contact_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Telefon qabul qilish"""
    if not update.message:
        return CONTACT_PHONE
    
    if not await check_rate(update, context):
        return CONTACT_PHONE
    
    lang = get_user_lang(context)
    phone = update.message.text
    
    is_valid, cleaned = validate_phone(phone)
    if not is_valid:
        await update.message.reply_text(
            get_text(lang, "contact_invalid_phone"),
            parse_mode=ParseMode.MARKDOWN
        )
        return CONTACT_PHONE
    
    context.user_data['contact_data']['phone'] = cleaned
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_cancel"), callback_data="main_menu")]
    ]
    
    await update.message.reply_text(
        get_text(lang, "contact_ask_brand"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    return CONTACT_BRAND


async def contact_brand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Brend nomi"""
    if not update.message:
        return CONTACT_BRAND
    
    if not await check_rate(update, context):
        return CONTACT_BRAND
    
    lang = get_user_lang(context)
    brand = sanitize_text(update.message.text, 200)
    
    if brand and brand != "-":
        context.user_data['contact_data']['brand'] = brand
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_cancel"), callback_data="main_menu")]
    ]
    
    await update.message.reply_text(
        get_text(lang, "contact_ask_message"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    return CONTACT_MESSAGE


async def contact_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Yakuniy xabar va adminga jo'natish"""
    if not update.message:
        return CONTACT_MESSAGE
    
    if not await check_rate(update, context):
        return CONTACT_MESSAGE
    
    lang = get_user_lang(context)
    msg = sanitize_text(update.message.text, 1000)
    
    if msg and msg != "-":
        context.user_data['contact_data']['message'] = msg
    
    # Adminga jo'natish
    await send_application_to_admin(context, update.effective_user)
    
    # Foydalanuvchiga tasdiq
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    await update.message.reply_text(
        get_text(lang, "contact_success"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )
    
    # Tozalash
    context.user_data.pop('contact_data', None)
    context.user_data.pop('contact_type', None)
    
    return ConversationHandler.END


async def send_application_to_admin(context: ContextTypes.DEFAULT_TYPE, user):
    """Adminga ariza yuborish"""
    contact_type = context.user_data.get('contact_type', 'help')
    data = context.user_data.get('contact_data', {})
    lang = get_user_lang(context)
    
    type_names = {
        'search': '🆓 Bepul brend tekshiruvi',
        'consult': '💬 Konsultatsiya',
        'help': '❓ Yordam soʻrovi'
    }
    
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    parts = [
        "🆕 YANGI ARIZA — Goldpatent Bot",
        "",
        f"📋 Tur: {type_names.get(contact_type, contact_type)}",
        f"👤 Ism: {data.get('name', '—')}",
        f"📞 Telefon: {data.get('phone', '—')}",
    ]
    
    # Telegram username (avtomatik bot orqali)
    if user.username:
        parts.append(f"✈️ Telegram: @{user.username}")
    else:
        parts.append(f"✈️ Telegram: tg://user?id={user.id}")
    
    if data.get('brand'):
        parts.append(f"🔍 Brend: {data['brand']}")
    
    if data.get('message'):
        parts.append(f"💬 Izoh: {data['message']}")
    
    parts.extend([
        f"🌐 Til: {lang.upper()}",
        f"🤖 Manba: Telegram Bot",
        "",
        f"⏰ {now}"
    ])
    
    text = "\n".join(parts)
    
    try:
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=text
        )
        logger.info(f"Application sent to admin from user {user.id}")
    except Exception as e:
        logger.error(f"Failed to send to admin: {e}")


# ============================================
# ABOUT
# ============================================
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Patent vakili haqida"""
    if not await check_rate(update, context):
        return
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    
    await query.edit_message_text(
        get_text(lang, "about_text"),
        reply_markup=get_back_keyboard(lang),
        parse_mode=ParseMode.MARKDOWN
    )


# ============================================
# FAQ
# ============================================
async def faq_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """FAQ menyusi"""
    if not await check_rate(update, context):
        return
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    
    keyboard = []
    for i in range(1, 7):
        keyboard.append([
            InlineKeyboardButton(
                get_text(lang, f"faq_q{i}"),
                callback_data=f"faq_a{i}"
            )
        ])
    keyboard.append([InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")])
    
    await query.edit_message_text(
        get_text(lang, "faq_menu"),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )


async def faq_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """FAQ javob"""
    if not await check_rate(update, context):
        return
    
    query = update.callback_query
    await query.answer()
    
    lang = get_user_lang(context)
    answer_key = query.data.replace("faq_a", "faq_a")
    
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_back"), callback_data="menu_faq")],
        [InlineKeyboardButton(get_text(lang, "btn_main_menu"), callback_data="main_menu")]
    ]
    
    await query.edit_message_text(
        get_text(lang, answer_key),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.MARKDOWN
    )


# ============================================
# CANCEL HANDLER
# ============================================
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bekor qilish"""
    lang = get_user_lang(context)
    
    # Tozalash
    for key in ['calc_data', 'contact_data', 'contact_type']:
        context.user_data.pop(key, None)
    
    await update.message.reply_text(
        get_text(lang, "main_menu_title"),
        reply_markup=get_main_menu_keyboard(lang),
        parse_mode=ParseMode.MARKDOWN
    )
    return ConversationHandler.END


# ============================================
# ERROR HANDLER
# ============================================
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Xatolarni tutib olish"""
    logger.error(f"Exception while handling update: {context.error}", exc_info=context.error)
    
    if isinstance(update, Update) and update.effective_message:
        try:
            lang = get_user_lang(context) if hasattr(context, 'user_data') else 'uz'
            await update.effective_message.reply_text(
                get_text(lang, "error_general")
            )
        except Exception:
            pass


# ============================================
# MAIN
# ============================================
def main():
    """Botni ishga tushirish"""
    logger.info("Starting Goldpatent Bot...")
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    # /start command
    application.add_handler(CommandHandler("start", start))
    
    # Calculator conversation
    calc_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(calc_start, pattern="^menu_calc$")],
        states={
            CALC_APPLICANT: [CallbackQueryHandler(calc_applicant, pattern="^calc_app_")],
            CALC_MARK_TYPE: [CallbackQueryHandler(calc_mark_type, pattern="^calc_mark_")],
            CALC_CLASSES: [MessageHandler(filters.TEXT & ~filters.COMMAND, calc_classes)],
            CALC_STAGES: [
                CallbackQueryHandler(calc_toggle_stage, pattern="^calc_stage_"),
                CallbackQueryHandler(calc_done, pattern="^calc_done$")
            ]
        },
        fallbacks=[
            CallbackQueryHandler(main_menu, pattern="^main_menu$"),
            CommandHandler("start", start),
            CommandHandler("cancel", cancel)
        ],
        per_message=False
    )
    application.add_handler(calc_conv)
    
    # Contact conversation
    contact_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(contact_start, pattern="^contact_start_")],
        states={
            CONTACT_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_name)],
            CONTACT_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_phone)],
            CONTACT_BRAND: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_brand)],
            CONTACT_MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_message)]
        },
        fallbacks=[
            CallbackQueryHandler(main_menu, pattern="^main_menu$"),
            CommandHandler("start", start),
            CommandHandler("cancel", cancel)
        ],
        per_message=False
    )
    application.add_handler(contact_conv)
    
    # Other handlers
    application.add_handler(CallbackQueryHandler(lang_handler, pattern="^lang_"))
    application.add_handler(CallbackQueryHandler(main_menu, pattern="^main_menu$"))
    application.add_handler(CallbackQueryHandler(menu_lang, pattern="^menu_lang$"))
    application.add_handler(CallbackQueryHandler(classes_menu, pattern="^menu_classes$"))
    application.add_handler(CallbackQueryHandler(classes_show_list, pattern="^classes_(goods|services)$"))
    application.add_handler(CallbackQueryHandler(classes_search_start, pattern="^classes_search$"))
    application.add_handler(CallbackQueryHandler(contact_menu, pattern="^menu_contact$"))
    application.add_handler(CallbackQueryHandler(about, pattern="^menu_about$"))
    application.add_handler(CallbackQueryHandler(faq_menu, pattern="^menu_faq$"))
    application.add_handler(CallbackQueryHandler(faq_answer, pattern="^faq_a"))
    
    # Class search input handler
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, 
        classes_search_handle
    ))
    
    # Error handler
    application.add_error_handler(error_handler)
    
    # Start polling
    logger.info("Bot is running. Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
