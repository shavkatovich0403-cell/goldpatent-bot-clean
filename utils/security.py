"""
Xavfsizlik moduli:
- Rate limiting (spam himoyasi)
- Foydalanuvchi ma'lumotlarini validatsiya qilish
- Logging
"""

import time
import re
from collections import defaultdict
from typing import Tuple


# Rate limiting xotira
# {user_id: [(timestamp, ...), ...]}
_user_messages = defaultdict(list)

# Rate limit sozlamalari
RATE_LIMIT_WINDOW = 60  # 60 sekund
RATE_LIMIT_MAX_MESSAGES = 20  # 60 sekundda maksimum 20 ta xabar


def check_rate_limit(user_id: int) -> Tuple[bool, int]:
    """
    Rate limit tekshiradi.
    
    Returns:
        (allowed: bool, remaining_seconds: int)
        - allowed=True bo'lsa, foydalanuvchi davom etishi mumkin
        - allowed=False bo'lsa, qancha sekund kutish kerakligini qaytaradi
    """
    now = time.time()
    user_msgs = _user_messages[user_id]
    
    # Eski xabarlarni o'chirish (60 sekunddan eski)
    user_msgs[:] = [t for t in user_msgs if now - t < RATE_LIMIT_WINDOW]
    
    # Limit tekshirish
    if len(user_msgs) >= RATE_LIMIT_MAX_MESSAGES:
        oldest = user_msgs[0]
        wait_seconds = int(RATE_LIMIT_WINDOW - (now - oldest)) + 1
        return False, wait_seconds
    
    # Yangi xabarni qo'shish
    user_msgs.append(now)
    return True, 0


def cleanup_old_data():
    """Eski rate limit ma'lumotlarini tozalash (xotira tejash uchun)"""
    now = time.time()
    to_remove = []
    for user_id, msgs in _user_messages.items():
        msgs[:] = [t for t in msgs if now - t < RATE_LIMIT_WINDOW]
        if not msgs:
            to_remove.append(user_id)
    for user_id in to_remove:
        del _user_messages[user_id]


def validate_name(name: str) -> Tuple[bool, str]:
    """
    Ism validatsiyasi.
    
    Returns:
        (is_valid, cleaned_name)
    """
    if not name:
        return False, ""
    
    # Boshi va oxiridagi bo'shliqlarni olib tashlash
    name = name.strip()
    
    # Juda qisqa
    if len(name) < 2:
        return False, name
    
    # Juda uzun (xavfsizlik)
    if len(name) > 100:
        name = name[:100]
    
    # Faqat raqamlar bo'lsa, ism emas
    if name.isdigit():
        return False, name
    
    return True, name


def validate_phone(phone: str) -> Tuple[bool, str]:
    """
    Telefon raqami validatsiyasi.
    
    Returns:
        (is_valid, cleaned_phone)
    """
    if not phone:
        return False, ""
    
    # Bo'shliqlarni va boshqa belgilarni olib tashlash
    cleaned = re.sub(r'[\s\-\(\)]+', '', phone.strip())
    
    # +998 bilan boshlanishi kerak
    if not cleaned.startswith('+'):
        if cleaned.startswith('998'):
            cleaned = '+' + cleaned
        elif cleaned.startswith('8') and len(cleaned) == 10:
            # Boshqa formatdan o'zgartirish
            cleaned = '+998' + cleaned[1:]
        else:
            return False, phone
    
    # +998 dan keyin 9 raqam bo'lishi kerak (jami 13 belgi)
    if not re.match(r'^\+998\d{9}$', cleaned):
        return False, phone
    
    return True, cleaned


def sanitize_text(text: str, max_length: int = 1000) -> str:
    """
    Foydalanuvchi matnini xavfsizlash.
    HTML/Markdown maxsus belgilarini xavfsiz qilish.
    """
    if not text:
        return ""
    
    text = text.strip()
    
    # Juda uzun matnni qisqartirish
    if len(text) > max_length:
        text = text[:max_length] + "..."
    
    return text


def is_admin(user_id: int, admin_id: int) -> bool:
    """Foydalanuvchi admin ekanligini tekshiradi"""
    return user_id == admin_id
