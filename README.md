# Goldpatent Telegram Bot

Tovar belgisini ro'yxatdan o'tkazish uchun davlat bojini hisoblash boti.

## 🎯 Xususiyatlar

- 💰 Davlat bojlari kalkulyatori (real vaqt rejimida)
- 📋 45 ta Nitsa klassi to'liq ro'yxati (qidiruv bilan)
- 🌐 3 til: O'zbek / Rus / Ingliz
- ✉️ Bog'lanish formasi (admin'ga avtomatik yuboriladi)
- ❓ Tez-tez beriladigan savollar
- 🛡️ Rate limiting (spam himoyasi)
- 🔐 Token environment variable orqali xavfsiz saqlanadi

## 📦 O'rnatish

### Lokal sinov uchun:

1. Python 3.10+ o'rnatilgan bo'lishi kerak

2. Virtual environment yarating:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Kutubxonalarni o'rnating:
```bash
pip install -r requirements.txt
```

4. `.env.example` ni `.env` ga ko'chiring:
```bash
cp .env.example .env
```

5. `.env` faylini tahrirlang:
```
BOT_TOKEN=sizning_bot_tokeningiz
ADMIN_CHAT_ID=sizning_chat_id
```

6. Botni ishga tushiring:
```bash
python bot.py
```

## 🚀 Railway'ga Deploy

### 1. Railway akkaunti yarating
- https://railway.app
- GitHub orqali kiring

### 2. Yangi loyiha yarating
- "New Project" → "Deploy from GitHub repo"
- Yoki "Empty Project" → "Add service" → "Empty Service"

### 3. Environment Variables qo'shing
Railway dashboard'da:
- `BOT_TOKEN` = sizning bot tokeningiz
- `ADMIN_CHAT_ID` = sizning Telegram chat ID

### 4. Deploy qiling
- Code'ni Railway'ga upload qiling (yoki GitHub'dan)
- Avtomatik ishga tushadi

## 📁 Loyiha tarkibi

```
goldpatent-bot/
├── bot.py                  # Asosiy bot kodi
├── requirements.txt        # Python kutubxonalari
├── Procfile               # Railway uchun
├── .env.example           # Environment variables namunasi
├── .gitignore
├── data/
│   ├── tariffs.py         # Davlat bojlari tariflari
│   ├── translations.py    # 3 tilli tarjimalar
│   └── classes.py         # 45 ta Nitsa klassi
└── utils/
    └── security.py        # Xavfsizlik (rate limiting, validatsiya)
```

## 🛡️ Xavfsizlik

- ✅ Token kodda yo'q (environment variable)
- ✅ Rate limiting: 1 minutda 20 ta xabar
- ✅ Foydalanuvchi ma'lumotlari validatsiyasi
- ✅ XSS/Injection himoyasi (sanitize_text)
- ✅ Logging (xatolar yoziladi, shaxsiy ma'lumotlar emas)

## 👨‍💼 Bot egasi

**Dostonbek Ergashev**  
Goldpatent ta'sischisi · Yurist va advokat  
📞 +998 94 150 12 00  
✈️ @Dostonbek_Shavkatovich  
🌐 goldpatent.uz

## 📜 Litsenziya

Ushbu kod faqat Goldpatent loyihasi uchun yaratilgan.
