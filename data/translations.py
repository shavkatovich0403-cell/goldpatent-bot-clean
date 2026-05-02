"""
Goldpatent Bot - 3 tilli tarjimalar
"""

TRANSLATIONS = {
    "uz": {
        # Welcome
        "welcome": (
            "🤖 *Goldpatent botiga xush kelibsiz!*\n\n"
            "Men sizga tovar belgisini roʻyxatdan oʻtkazish narxini "
            "hisoblashda yordam beraman.\n\n"
            "_⚠️ Eslatma: Bot faqat davlat bojlarini hisoblaydi. "
            "Patent vakili xizmat haqi alohida hisoblanadi._\n\n"
            "Tilni tanlang / Выберите язык / Choose language:"
        ),
        "main_menu_title": "👋 *Asosiy menyu*\n\nQuyidagi imkoniyatlardan foydalaning:",
        "btn_calculator": "💰 Davlat bojini hisoblash",
        "btn_classes": "📋 Klasslar roʻyxati",
        "btn_contact": "✉️ Bogʻlanish / Ariza qoldirish",
        "btn_faq": "❓ Tez-tez beriladigan savollar",
        "btn_about": "👤 Patent vakili haqida",
        "btn_change_lang": "🌐 Tilni oʻzgartirish",
        "btn_back": "⬅️ Orqaga",
        "btn_main_menu": "🏠 Bosh menyu",
        "btn_cancel": "❌ Bekor qilish",
        
        # Calculator
        "calc_step1": "1️⃣ *Arizachi turini tanlang:*",
        "calc_individual": "Jismoniy shaxs",
        "calc_legal": "Yuridik shaxs",
        "calc_step2": "2️⃣ *Tovar belgisi turini tanlang:*",
        "calc_ordinary": "Oddiy",
        "calc_collective": "Jamoaviy",
        "calc_step3": (
            "3️⃣ *Sinflar sonini kiriting (1-45):*\n\n"
            "Iltimos, raqam yozing.\n"
            "_Klasslar haqida maʼlumot uchun \"📋 Klasslar roʻyxati\" tugmasini bosing._"
        ),
        "calc_step3_invalid": "❌ Iltimos, 1 dan 45 gacha boʻlgan raqam kiriting.",
        "calc_step4": "4️⃣ *Qaysi bosqichlarni hisoblayman?*\n\nBir nechtasini tanlashingiz mumkin:",
        "calc_stage_application": "Talabnoma topshirish",
        "calc_stage_express": "Tezkor ekspertiza",
        "calc_stage_certificate": "Guvohnoma berish",
        "calc_stage_extension": "Muddatni uzaytirish",
        "calc_btn_done": "✅ Hisoblash",
        "calc_no_stages": "❌ Kamida bitta bosqichni tanlang.",
        "calc_result_title": "💰 *HISOB-KITOB NATIJASI*",
        "calc_applicant": "Arizachi",
        "calc_mark_type": "Belgi turi",
        "calc_classes": "Sinflar",
        "calc_breakdown": "📊 *Bosqichlar:*",
        "calc_total": "💵 *JAMI*",
        "calc_currency": "soʻm",
        "calc_warning": (
            "⚠️ Faqat davlat bojlari hisoblandi.\n"
            "Patent vakili xizmati alohida belgilanadi.\n\n"
            "_Aniq summa va sizga mos klasslarni belgilash uchun "
            "patent vakili bilan bogʻlaning._"
        ),
        "calc_btn_apply": "💼 Ariza qoldirish",
        "calc_btn_recalc": "🔄 Qayta hisoblash",
        
        # Classes
        "classes_title": (
            "📋 *Tovar va xizmatlar tasnifi*\n"
            "_Nitsa tasnifi · 45 ta klass_\n\n"
            "Quyidagilardan birini tanlang yoki qidirish uchun "
            "klass raqami yoki soʻz yozing:"
        ),
        "classes_btn_goods": "📦 Tovarlar (1-34)",
        "classes_btn_services": "🔧 Xizmatlar (35-45)",
        "classes_btn_search": "🔍 Qidirish",
        "classes_search_prompt": (
            "🔍 *Qidirish*\n\n"
            "Klass raqami (masalan: 30) yoki "
            "soʻz (masalan: non, kiyim, IT) yozing:"
        ),
        "classes_no_results": "❌ Hech narsa topilmadi. Boshqa soʻz bilan urinib koʻring.",
        "classes_results_title": "🔍 Topilgan natijalar:",
        "classes_type_goods": "📦 Tovar",
        "classes_type_services": "🔧 Xizmat",
        "classes_btn_search_more": "🔍 Yana qidirish",
        
        # Contact
        "contact_menu": (
            "✉️ *Patent vakili bilan bogʻlanish*\n\n"
            "Quyidagilardan birini tanlang:"
        ),
        "contact_btn_search": "🆓 Bepul brend tekshiruvi",
        "contact_btn_consult": "💬 Konsultatsiya soʻrash",
        "contact_btn_help": "❓ Yordam kerak",
        "contact_direct": (
            "📞 *Toʻgʻridan-toʻgʻri bogʻlanish:*\n"
            "+998 94 150 12 00\n"
            "✈️ @Dostonbek\\_Shavkatovich\n"
            "📧 Shavkatovich0403@gmail.com"
        ),
        "contact_search_intro": (
            "🆓 *Bepul brend tekshiruvi*\n\n"
            "Brendingiz nomini kiriting — patent vakili reestrda mavjud "
            "boʻlmasligini bepul tekshirib, sizga aniq javob qaytaradi.\n\n"
            "Avval ismingizni yozing:"
        ),
        "contact_consult_intro": (
            "💬 *Konsultatsiya soʻrash*\n\n"
            "Tovar belgisi, klasslar, narx yoki jarayon haqida savollaringiz "
            "boʻlsa, ariza qoldiring — patent vakili siz bilan bogʻlanadi.\n\n"
            "Avval ismingizni yozing:"
        ),
        "contact_help_intro": (
            "❓ *Yordam soʻrovi*\n\n"
            "Savolingizni yozing — patent vakili tezda javob qaytaradi.\n\n"
            "Avval ismingizni yozing:"
        ),
        "contact_ask_phone": "📞 Endi telefon raqamingizni yozing:\n_(masalan: +998 90 123 45 67)_",
        "contact_ask_brand": (
            "🔍 Brend nomini yozing yoki \"-\" yuboring agar yoʻq boʻlsa:\n"
            "_(majburiy emas)_"
        ),
        "contact_ask_message": (
            "💬 Qoʻshimcha izoh yozing yoki \"-\" yuboring agar yoʻq boʻlsa:\n"
            "_(faoliyatingiz haqida qisqacha yoki savolingiz)_"
        ),
        "contact_invalid_name": "❌ Ism juda qisqa. Iltimos, toʻliq ismingizni yozing.",
        "contact_invalid_phone": (
            "❌ Telefon raqami notoʻgʻri.\n"
            "Iltimos, +998 bilan boshlanadigan toʻliq raqam kiriting.\n"
            "Masalan: +998 90 123 45 67"
        ),
        "contact_success": (
            "✅ *Rahmat!*\n\n"
            "Arizangiz qabul qilindi. Patent vakili tezda siz bilan bogʻlanadi.\n\n"
            "Tezkor bogʻlanish uchun:\n"
            "📞 +998 94 150 12 00\n"
            "✈️ @Dostonbek\\_Shavkatovich"
        ),
        
        # About
        "about_text": (
            "👤 *DOSTONBEK ERGASHEV*\n\n"
            "🎓 Goldpatent taʼsischisi\n"
            "⚖️ Yurist va advokat\n"
            "🏆 70+ muvaffaqiyatli patent\n"
            "📅 Patentlash sohasidagi tajriba: 2 yil\n\n"
            "_\"Ishonch sizdan, himoya bizdan\"_\n\n"
            "Tovar belgilarini Oʻzbekiston Respublikasi hududida hamda "
            "xalqaro darajada roʻyxatdan oʻtkazishga, brendga boʻlgan huquqingizni "
            "himoya qilishga ixtisoslashganman.\n\n"
            "📞 +998 94 150 12 00\n"
            "✈️ @Dostonbek\\_Shavkatovich\n"
            "📧 Shavkatovich0403@gmail.com\n"
            "🌐 goldpatent.uz"
        ),
        
        # FAQ
        "faq_menu": "❓ *Tez-tez beriladigan savollar*\n\nQiziqayotgan mavzuni tanlang:",
        "faq_q1": "Patent va tovar belgisining farqi nima?",
        "faq_q2": "Ro'yxatdan o'tkazish jarayoni qancha vaqt oladi?",
        "faq_q3": "Davlat boji nima va u qaytariladimi?",
        "faq_q4": "Qaysi klasslarni tanlash kerak?",
        "faq_q5": "Tezkor ekspertiza nima?",
        "faq_q6": "Brendni xalqaro darajada ham himoya qilsam bo'ladimi?",
        "faq_a1": (
            "*Patent va tovar belgisining farqi:*\n\n"
            "🔹 *Patent* — yangi ixtirolar, foydali modellar, sanoat namunalari uchun "
            "beriladigan huquq.\n\n"
            "🔹 *Tovar belgisi (brend)* — kompaniya yoki mahsulotning nomini, logotipini, "
            "shiorini boshqalardan farqlash uchun beriladigan huquq.\n\n"
            "Aksariyat tadbirkorlar uchun aynan *tovar belgisi* kerak boʻladi."
        ),
        "faq_a2": (
            "*Roʻyxatdan oʻtkazish jarayoni:*\n\n"
            "📅 Standart muddat: *taxminan 8 oy*\n\n"
            "Bosqichlar:\n"
            "• 1-oy — Rasmiy ekspertiza\n"
            "• 5 oy — Kutish muddati\n"
            "• 7-oy — Mohiyat boʻyicha ekspertiza\n"
            "• 8-oy — Guvohnoma berish\n\n"
            "⚡ *Tezkor tartib:* toʻlovdan boshlab 40 kungacha"
        ),
        "faq_a3": (
            "*Davlat boji haqida:*\n\n"
            "💰 Davlat boji — bu tovar belgisini roʻyxatdan oʻtkazish uchun "
            "davlat byudjetiga toʻlanadigan rasmiy toʻlov.\n\n"
            "⚠️ *MUHIM:* Agar ariza rad etilsa, davlat boji *qaytarilmaydi*.\n\n"
            "Shuning uchun avval professional patent vakili bilan maslahatlashish tavsiya etiladi."
        ),
        "faq_a4": (
            "*Klasslarni tanlash:*\n\n"
            "Klasslar — bu Nitsa tasnifi boʻyicha 45 ta toifa boʻlib, sizning faoliyatingiz "
            "qaysi klassga tegishliligini bildiradi.\n\n"
            "📦 *1-34 — Tovarlar* (kiyim, oziq-ovqat, mebel va h.k.)\n"
            "🔧 *35-45 — Xizmatlar* (reklama, IT, taʼlim va h.k.)\n\n"
            "Toʻgʻri klassni tanlash juda muhim — notoʻgʻri klassda roʻyxatdan oʻtkazsangiz, "
            "huquqingiz oʻsha sohada amal qilmaydi.\n\n"
            "_Patent vakili bilan maslahatlashishni tavsiya qilamiz._"
        ),
        "faq_a5": (
            "*Tezkor ekspertiza:*\n\n"
            "⚡ Standart 8 oy oʻrniga *40 kun ichida* roʻyxatdan oʻtish imkoniyati.\n\n"
            "Qachon foydali:\n"
            "• Brend tezda bozorga chiqishi kerak\n"
            "• Raqobatchilar bilan ulgurish kerak\n"
            "• Investorlar yoki sheriklar uchun guvohnoma kerak\n\n"
            "💰 Qoʻshimcha toʻlov: 5 600 000 soʻm (1 sinf uchun) + har qoʻshimcha sinf 470 000 soʻm"
        ),
        "faq_a6": (
            "*Xalqaro himoya:*\n\n"
            "🌍 Ha, brendingizni xalqaro darajada ham himoya qilishingiz mumkin.\n\n"
            "Variantlar:\n"
            "• *Madrid tizimi* — bir arizada bir nechta mamlakatda\n"
            "• *Har bir mamlakatda alohida* — milliy roʻyxatdan oʻtkazish\n\n"
            "Goldpatent xalqaro roʻyxatdan oʻtkazish bilan ham shugʻullanadi.\n\n"
            "📞 Konsultatsiya uchun bogʻlaning."
        ),
        
        # Errors / Common
        "error_general": "❌ Xatolik yuz berdi. Iltimos, qaytadan urinib koʻring.",
        "error_rate_limit": "⏳ Juda tez xabar yubordingiz. Iltimos, biroz kuting.",
        "language_changed": "✅ Til oʻzbekchaga oʻzgartirildi.",
        "cancelled": "❌ Bekor qilindi.",
    },
    
    "ru": {
        "welcome": (
            "🤖 *Добро пожаловать в Goldpatent бот!*\n\n"
            "Я помогу вам рассчитать стоимость регистрации товарного знака.\n\n"
            "_⚠️ Примечание: Бот рассчитывает только государственные пошлины. "
            "Услуги патентного поверенного оплачиваются отдельно._\n\n"
            "Tilni tanlang / Выберите язык / Choose language:"
        ),
        "main_menu_title": "👋 *Главное меню*\n\nВыберите одну из опций:",
        "btn_calculator": "💰 Расчёт госпошлины",
        "btn_classes": "📋 Список классов",
        "btn_contact": "✉️ Связаться / Оставить заявку",
        "btn_faq": "❓ Часто задаваемые вопросы",
        "btn_about": "👤 О патентном поверенном",
        "btn_change_lang": "🌐 Сменить язык",
        "btn_back": "⬅️ Назад",
        "btn_main_menu": "🏠 Главное меню",
        "btn_cancel": "❌ Отмена",
        
        "calc_step1": "1️⃣ *Выберите тип заявителя:*",
        "calc_individual": "Физ. лицо",
        "calc_legal": "Юр. лицо",
        "calc_step2": "2️⃣ *Выберите тип товарного знака:*",
        "calc_ordinary": "Обычный",
        "calc_collective": "Коллективный",
        "calc_step3": (
            "3️⃣ *Введите количество классов (1-45):*\n\n"
            "Пожалуйста, введите число.\n"
            "_Информацию о классах см. в \"📋 Список классов\"._"
        ),
        "calc_step3_invalid": "❌ Пожалуйста, введите число от 1 до 45.",
        "calc_step4": "4️⃣ *Какие этапы рассчитать?*\n\nМожно выбрать несколько:",
        "calc_stage_application": "Подача заявки",
        "calc_stage_express": "Ускоренная экспертиза",
        "calc_stage_certificate": "Выдача свидетельства",
        "calc_stage_extension": "Продление срока",
        "calc_btn_done": "✅ Рассчитать",
        "calc_no_stages": "❌ Выберите хотя бы один этап.",
        "calc_result_title": "💰 *РЕЗУЛЬТАТ РАСЧЁТА*",
        "calc_applicant": "Заявитель",
        "calc_mark_type": "Тип знака",
        "calc_classes": "Классы",
        "calc_breakdown": "📊 *Этапы:*",
        "calc_total": "💵 *ИТОГО*",
        "calc_currency": "сум",
        "calc_warning": (
            "⚠️ Рассчитаны только государственные пошлины.\n"
            "Услуги патентного поверенного оплачиваются отдельно.\n\n"
            "_Для точной суммы и определения подходящих классов "
            "свяжитесь с патентным поверенным._"
        ),
        "calc_btn_apply": "💼 Оставить заявку",
        "calc_btn_recalc": "🔄 Пересчитать",
        
        "classes_title": (
            "📋 *Классификация товаров и услуг*\n"
            "_Ниццкая классификация · 45 классов_\n\n"
            "Выберите одну из опций или введите номер класса/слово для поиска:"
        ),
        "classes_btn_goods": "📦 Товары (1-34)",
        "classes_btn_services": "🔧 Услуги (35-45)",
        "classes_btn_search": "🔍 Поиск",
        "classes_search_prompt": (
            "🔍 *Поиск*\n\n"
            "Введите номер класса (например: 30) или "
            "слово (например: хлеб, одежда, IT):"
        ),
        "classes_no_results": "❌ Ничего не найдено. Попробуйте другое слово.",
        "classes_results_title": "🔍 Найденные результаты:",
        "classes_type_goods": "📦 Товар",
        "classes_type_services": "🔧 Услуга",
        "classes_btn_search_more": "🔍 Искать ещё",
        
        "contact_menu": (
            "✉️ *Связь с патентным поверенным*\n\n"
            "Выберите одну из опций:"
        ),
        "contact_btn_search": "🆓 Бесплатная проверка бренда",
        "contact_btn_consult": "💬 Запросить консультацию",
        "contact_btn_help": "❓ Нужна помощь",
        "contact_direct": (
            "📞 *Прямая связь:*\n"
            "+998 94 150 12 00\n"
            "✈️ @Dostonbek\\_Shavkatovich\n"
            "📧 Shavkatovich0403@gmail.com"
        ),
        "contact_search_intro": (
            "🆓 *Бесплатная проверка бренда*\n\n"
            "Введите название вашего бренда — патентный поверенный бесплатно "
            "проверит его наличие в реестре.\n\n"
            "Сначала введите ваше имя:"
        ),
        "contact_consult_intro": (
            "💬 *Запрос консультации*\n\n"
            "Если у вас есть вопросы, оставьте заявку — патентный поверенный "
            "свяжется с вами.\n\n"
            "Сначала введите ваше имя:"
        ),
        "contact_help_intro": (
            "❓ *Запрос помощи*\n\n"
            "Напишите свой вопрос — патентный поверенный быстро ответит.\n\n"
            "Сначала введите ваше имя:"
        ),
        "contact_ask_phone": "📞 Теперь введите номер телефона:\n_(например: +998 90 123 45 67)_",
        "contact_ask_brand": (
            "🔍 Введите название бренда или отправьте \"-\":\n"
            "_(необязательно)_"
        ),
        "contact_ask_message": (
            "💬 Дополнительный комментарий или \"-\":\n"
            "_(кратко о деятельности или вопрос)_"
        ),
        "contact_invalid_name": "❌ Имя слишком короткое. Введите полное имя.",
        "contact_invalid_phone": (
            "❌ Неверный номер телефона.\n"
            "Введите номер начиная с +998.\n"
            "Например: +998 90 123 45 67"
        ),
        "contact_success": (
            "✅ *Спасибо!*\n\n"
            "Ваша заявка принята. Патентный поверенный свяжется с вами в ближайшее время.\n\n"
            "Для срочной связи:\n"
            "📞 +998 94 150 12 00\n"
            "✈️ @Dostonbek\\_Shavkatovich"
        ),
        
        "about_text": (
            "👤 *ДОСТОНБЕК ЭРГАШЕВ*\n\n"
            "🎓 Основатель Goldpatent\n"
            "⚖️ Юрист и адвокат\n"
            "🏆 70+ успешных патентов\n"
            "📅 Опыт в патентовании: 2 года\n\n"
            "_\"Доверие — от вас, защита — от нас\"_\n\n"
            "Специализируюсь на регистрации товарных знаков в Республике Узбекистан "
            "и на международном уровне, защите прав на бренд.\n\n"
            "📞 +998 94 150 12 00\n"
            "✈️ @Dostonbek\\_Shavkatovich\n"
            "📧 Shavkatovich0403@gmail.com\n"
            "🌐 goldpatent.uz"
        ),
        
        "faq_menu": "❓ *Часто задаваемые вопросы*\n\nВыберите интересующую тему:",
        "faq_q1": "В чём разница между патентом и товарным знаком?",
        "faq_q2": "Сколько времени занимает регистрация?",
        "faq_q3": "Что такое госпошлина и возвращается ли она?",
        "faq_q4": "Какие классы выбрать?",
        "faq_q5": "Что такое ускоренная экспертиза?",
        "faq_q6": "Можно ли защитить бренд на международном уровне?",
        "faq_a1": (
            "*Разница между патентом и товарным знаком:*\n\n"
            "🔹 *Патент* — право на изобретения, полезные модели, промышленные образцы.\n\n"
            "🔹 *Товарный знак (бренд)* — право на название, логотип, слоган "
            "вашей компании или продукта.\n\n"
            "Большинству предпринимателей нужен именно *товарный знак*."
        ),
        "faq_a2": (
            "*Процесс регистрации:*\n\n"
            "📅 Стандартный срок: *около 8 месяцев*\n\n"
            "Этапы:\n"
            "• 1-й месяц — Формальная экспертиза\n"
            "• 5 месяцев — Период ожидания\n"
            "• 7-й месяц — Экспертиза по существу\n"
            "• 8-й месяц — Выдача свидетельства\n\n"
            "⚡ *Ускоренный режим:* до 40 дней с момента оплаты"
        ),
        "faq_a3": (
            "*О госпошлине:*\n\n"
            "💰 Госпошлина — это официальный платёж в государственный бюджет.\n\n"
            "⚠️ *ВАЖНО:* Если заявка отклонена, госпошлина *не возвращается*.\n\n"
            "Поэтому рекомендуется сначала проконсультироваться с патентным поверенным."
        ),
        "faq_a4": (
            "*Выбор классов:*\n\n"
            "Классы — 45 категорий по Ниццкой классификации.\n\n"
            "📦 *1-34 — Товары* (одежда, продукты, мебель и т.д.)\n"
            "🔧 *35-45 — Услуги* (реклама, IT, образование и т.д.)\n\n"
            "Правильный выбор класса очень важен — иначе ваше право не будет действовать "
            "в нужной сфере.\n\n"
            "_Рекомендуем проконсультироваться с патентным поверенным._"
        ),
        "faq_a5": (
            "*Ускоренная экспертиза:*\n\n"
            "⚡ Вместо стандартных 8 месяцев — регистрация *за 40 дней*.\n\n"
            "Когда полезно:\n"
            "• Бренд срочно нужно вывести на рынок\n"
            "• Опередить конкурентов\n"
            "• Свидетельство нужно для инвесторов или партнёров\n\n"
            "💰 Доплата: 5 600 000 сум (1 класс) + 470 000 сум за каждый доп. класс"
        ),
        "faq_a6": (
            "*Международная защита:*\n\n"
            "🌍 Да, вы можете защитить ваш бренд и на международном уровне.\n\n"
            "Варианты:\n"
            "• *Мадридская система* — одна заявка для нескольких стран\n"
            "• *В каждой стране отдельно* — национальная регистрация\n\n"
            "Goldpatent занимается также международной регистрацией.\n\n"
            "📞 Свяжитесь для консультации."
        ),
        
        "error_general": "❌ Произошла ошибка. Пожалуйста, попробуйте ещё раз.",
        "error_rate_limit": "⏳ Слишком много сообщений. Подождите немного.",
        "language_changed": "✅ Язык изменён на русский.",
        "cancelled": "❌ Отменено.",
    },
    
    "en": {
        "welcome": (
            "🤖 *Welcome to Goldpatent Bot!*\n\n"
            "I'll help you calculate the cost of trademark registration.\n\n"
            "_⚠️ Note: The bot calculates only government fees. "
            "Patent attorney services are charged separately._\n\n"
            "Tilni tanlang / Выберите язык / Choose language:"
        ),
        "main_menu_title": "👋 *Main menu*\n\nChoose one of the options:",
        "btn_calculator": "💰 Calculate fees",
        "btn_classes": "📋 Class list",
        "btn_contact": "✉️ Contact / Submit request",
        "btn_faq": "❓ FAQ",
        "btn_about": "👤 About attorney",
        "btn_change_lang": "🌐 Change language",
        "btn_back": "⬅️ Back",
        "btn_main_menu": "🏠 Main menu",
        "btn_cancel": "❌ Cancel",
        
        "calc_step1": "1️⃣ *Select applicant type:*",
        "calc_individual": "Individual",
        "calc_legal": "Legal entity",
        "calc_step2": "2️⃣ *Select trademark type:*",
        "calc_ordinary": "Standard",
        "calc_collective": "Collective",
        "calc_step3": (
            "3️⃣ *Enter the number of classes (1-45):*\n\n"
            "Please enter a number.\n"
            "_For class info, see \"📋 Class list\"._"
        ),
        "calc_step3_invalid": "❌ Please enter a number from 1 to 45.",
        "calc_step4": "4️⃣ *Which stages to calculate?*\n\nYou can select multiple:",
        "calc_stage_application": "Filing application",
        "calc_stage_express": "Express examination",
        "calc_stage_certificate": "Certificate issuance",
        "calc_stage_extension": "Term extension",
        "calc_btn_done": "✅ Calculate",
        "calc_no_stages": "❌ Select at least one stage.",
        "calc_result_title": "💰 *CALCULATION RESULT*",
        "calc_applicant": "Applicant",
        "calc_mark_type": "Mark type",
        "calc_classes": "Classes",
        "calc_breakdown": "📊 *Stages:*",
        "calc_total": "💵 *TOTAL*",
        "calc_currency": "UZS",
        "calc_warning": (
            "⚠️ Government fees only.\n"
            "Patent attorney services charged separately.\n\n"
            "_For exact amount and class selection, contact a patent attorney._"
        ),
        "calc_btn_apply": "💼 Submit request",
        "calc_btn_recalc": "🔄 Recalculate",
        
        "classes_title": (
            "📋 *Classification of goods and services*\n"
            "_Nice Classification · 45 classes_\n\n"
            "Choose an option or enter a class number/word to search:"
        ),
        "classes_btn_goods": "📦 Goods (1-34)",
        "classes_btn_services": "🔧 Services (35-45)",
        "classes_btn_search": "🔍 Search",
        "classes_search_prompt": (
            "🔍 *Search*\n\n"
            "Enter class number (e.g., 30) or "
            "word (e.g., bread, clothing, IT):"
        ),
        "classes_no_results": "❌ Nothing found. Try a different word.",
        "classes_results_title": "🔍 Search results:",
        "classes_type_goods": "📦 Goods",
        "classes_type_services": "🔧 Service",
        "classes_btn_search_more": "🔍 Search more",
        
        "contact_menu": (
            "✉️ *Contact patent attorney*\n\n"
            "Choose one of the options:"
        ),
        "contact_btn_search": "🆓 Free brand check",
        "contact_btn_consult": "💬 Request consultation",
        "contact_btn_help": "❓ Need help",
        "contact_direct": (
            "📞 *Direct contact:*\n"
            "+998 94 150 12 00\n"
            "✈️ @Dostonbek\\_Shavkatovich\n"
            "📧 Shavkatovich0403@gmail.com"
        ),
        "contact_search_intro": (
            "🆓 *Free brand check*\n\n"
            "Enter your brand name — the patent attorney will check it for free.\n\n"
            "First, enter your name:"
        ),
        "contact_consult_intro": (
            "💬 *Request consultation*\n\n"
            "If you have questions, submit a request — the attorney will contact you.\n\n"
            "First, enter your name:"
        ),
        "contact_help_intro": (
            "❓ *Help request*\n\n"
            "Write your question — the attorney will reply quickly.\n\n"
            "First, enter your name:"
        ),
        "contact_ask_phone": "📞 Now enter your phone number:\n_(e.g., +998 90 123 45 67)_",
        "contact_ask_brand": (
            "🔍 Enter brand name or send \"-\":\n"
            "_(optional)_"
        ),
        "contact_ask_message": (
            "💬 Additional comment or \"-\":\n"
            "_(briefly about your activity or question)_"
        ),
        "contact_invalid_name": "❌ Name is too short. Please enter your full name.",
        "contact_invalid_phone": (
            "❌ Invalid phone number.\n"
            "Enter number starting with +998.\n"
            "E.g.: +998 90 123 45 67"
        ),
        "contact_success": (
            "✅ *Thank you!*\n\n"
            "Your request has been received. The patent attorney will contact you soon.\n\n"
            "For urgent contact:\n"
            "📞 +998 94 150 12 00\n"
            "✈️ @Dostonbek\\_Shavkatovich"
        ),
        
        "about_text": (
            "👤 *DOSTONBEK ERGASHEV*\n\n"
            "🎓 Founder of Goldpatent\n"
            "⚖️ Lawyer and attorney\n"
            "🏆 70+ successful patents\n"
            "📅 Patent experience: 2 years\n\n"
            "_\"Trust from you, protection from us\"_\n\n"
            "I specialize in registering trademarks in Uzbekistan and internationally, "
            "and protecting your brand rights.\n\n"
            "📞 +998 94 150 12 00\n"
            "✈️ @Dostonbek\\_Shavkatovich\n"
            "📧 Shavkatovich0403@gmail.com\n"
            "🌐 goldpatent.uz"
        ),
        
        "faq_menu": "❓ *Frequently asked questions*\n\nChoose a topic:",
        "faq_q1": "Difference between patent and trademark?",
        "faq_q2": "How long does registration take?",
        "faq_q3": "What is government fee and is it refundable?",
        "faq_q4": "Which classes to choose?",
        "faq_q5": "What is express examination?",
        "faq_q6": "Can I protect my brand internationally?",
        "faq_a1": (
            "*Patent vs Trademark:*\n\n"
            "🔹 *Patent* — right for inventions, utility models, industrial designs.\n\n"
            "🔹 *Trademark (brand)* — right for the name, logo, slogan of your company "
            "or product.\n\n"
            "Most entrepreneurs need a *trademark*."
        ),
        "faq_a2": (
            "*Registration process:*\n\n"
            "📅 Standard term: *about 8 months*\n\n"
            "Stages:\n"
            "• Month 1 — Formal examination\n"
            "• 5 months — Waiting period\n"
            "• Month 7 — Substantive examination\n"
            "• Month 8 — Certificate issuance\n\n"
            "⚡ *Express mode:* up to 40 days from payment"
        ),
        "faq_a3": (
            "*About government fees:*\n\n"
            "💰 Government fee — official payment to the state budget.\n\n"
            "⚠️ *IMPORTANT:* If the application is rejected, the fee is *not refundable*.\n\n"
            "Therefore it's recommended to first consult with a patent attorney."
        ),
        "faq_a4": (
            "*Choosing classes:*\n\n"
            "Classes — 45 categories per the Nice Classification.\n\n"
            "📦 *1-34 — Goods* (clothing, food, furniture, etc.)\n"
            "🔧 *35-45 — Services* (advertising, IT, education, etc.)\n\n"
            "Choosing the right class is very important — otherwise your right won't apply "
            "in the correct field.\n\n"
            "_We recommend consulting a patent attorney._"
        ),
        "faq_a5": (
            "*Express examination:*\n\n"
            "⚡ Instead of standard 8 months — registration *within 40 days*.\n\n"
            "When useful:\n"
            "• Brand needs to enter the market urgently\n"
            "• To stay ahead of competitors\n"
            "• Certificate needed for investors or partners\n\n"
            "💰 Additional fee: 5,600,000 UZS (1 class) + 470,000 UZS per additional class"
        ),
        "faq_a6": (
            "*International protection:*\n\n"
            "🌍 Yes, you can protect your brand internationally.\n\n"
            "Options:\n"
            "• *Madrid System* — one application for multiple countries\n"
            "• *Each country separately* — national registration\n\n"
            "Goldpatent also handles international registration.\n\n"
            "📞 Contact for consultation."
        ),
        
        "error_general": "❌ An error occurred. Please try again.",
        "error_rate_limit": "⏳ Too many messages. Please wait a moment.",
        "language_changed": "✅ Language changed to English.",
        "cancelled": "❌ Cancelled.",
    }
}


def get_text(lang: str, key: str) -> str:
    """Get translated text by language and key"""
    if lang not in TRANSLATIONS:
        lang = "uz"  # default
    return TRANSLATIONS[lang].get(key, TRANSLATIONS["uz"].get(key, key))
