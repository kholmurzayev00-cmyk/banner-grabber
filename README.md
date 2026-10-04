# banner-grabber
Python Banner Grabber - socket orqali servis bannerini o'qish (o'quv loyihasi)
# 🛡️ Banner Grabber – Network & Security Tools

Tarmoq va xavfsizlikni tekshirish uchun yaratilgan 3 ta kichik vosita to'plami.

**Tillar:** Python, Bash, PowerShell

---

## 📁 Loyihalar

| Vosita | Fayl | Til | Vazifasi |
|--------|------|-----|----------|
| Banner Grabber | `banner_grabber.py` | Python | Ochiq portlardan xizmat bannerlarini olish |
| Ping Sweeper | `ping-sweeper.ps1` | PowerShell | Tarmoqdagi faol hostlarni aniqlash |
| LinuxSecTool | `LinuxSecTool` | Bash | Linux tizimining xavfsizlik holatini tekshirish |

---

## 1️⃣ Banner Grabber (Python)

Berilgan IP manzil va port bo'yicha ulanib, xizmat (service) yuborgan **banner**ni o'qiydi. Banner orqali serverda qaysi dastur va qaysi versiya ishlayotganini bilish mumkin (masalan: SSH, FTP, HTTP).

**Ishga tushirish:**
```bash
python3 banner_grabber.py
```

**Namuna:**
```
IP: 192.168.1.10
Port: 22
Banner: SSH-2.0-OpenSSH_8.9
```

---

## 2️⃣ Ping Sweeper (PowerShell)

IP diapazonidagi barcha manzillarga ping yuborib, qaysi qurilmalar **onlayn** ekanini aniqlaydi. Tarmoqni skanerlashning birinchi bosqichi sifatida ishlatiladi.

**Ishga tushirish:**
```powershell
.\ping-sweeper.ps1
```

**Namuna natija:**
```
192.168.1.1   - Faol
192.168.1.5   - Faol
192.168.1.20  - Faol
```

---

## 3️⃣ LinuxSecTool (Bash)

Linux tizimida asosiy xavfsizlik tekshiruvlarini avtomatik bajaradi (masalan: ochiq portlar, foydalanuvchilar, fayl ruxsatlari va boshqalar).

**Ishga tushirish:**
```bash
chmod +x LinuxSecTool
./LinuxSecTool
```

---

## ⚙️ Talablar

- **Python 3.x** – banner_grabber uchun
- **PowerShell 5.1+** – ping-sweeper uchun
- **Linux (Bash)** – LinuxSecTool uchun

## 📥 O'rnatish

```bash
git clone https://github.com/kholmurzayev00-cmyk/banner-grabber.git
cd banner-grabber
```

## ⚠️ Ogohlantirish

Bu vositalar faqat **o'quv maqsadlarida** va **o'zingizga tegishli yoki ruxsat olingan** tarmoqlarda ishlatilishi kerak. Ruxsatsiz skanerlash qonunga xilofdir. Muallif noto'g'ri foydalanish uchun javobgar emas.

## 👤 Muallif

**kholmurzayev00-cmyk**
