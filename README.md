# SMS4Jawaly Python SDK

## 🇬🇧 English

Python library for sending SMS messages through the 4jawaly SMS Gateway with support for parallel sending and batch processing.

### Features
- Parallel SMS sending with automatic batch processing
- Support for large number of recipients (automatically split into chunks)
- Comprehensive error handling and reporting
- Balance checking and sender names management

### Installation
```bash
pip install sms4jawaly-py
```

### Usage
```python
from sms4jawaly_py import SMS4JawalyClient

# Initialize client
client = SMS4JawalyClient(
    api_key='your_api_key',
    api_secret='your_api_secret'
)

# Send to multiple numbers (automatically handled in parallel)
numbers = ['966500000000', '966500000001']
result = client.send_sms(
    message='Test message from 4jawaly!',
    numbers=numbers,
    sender='YOUR_SENDER_NAME'
)

# Check results
print(f'Success: {result["total_success"]} messages')
print(f'Failed: {result["total_failed"]} messages')
if result["job_ids"]:
    print(f'Job IDs: {result["job_ids"]}')
if result["errors"]:
    print(f'Errors: {result["errors"]}')

# Check balance
balance = client.get_balance()
print(f'Current balance: {balance}')

# Get sender names
senders = client.get_senders()
print(f'Approved senders: {senders}')
```

## 🇸🇦 عربي

مكتبة Python لإرسال الرسائل النصية القصيرة عبر بوابة 4jawaly للرسائل مع دعم الإرسال المتوازي ومعالجة الدفعات.

### المميزات
- إرسال الرسائل بشكل متوازٍ مع معالجة تلقائية للدفعات
- دعم لعدد كبير من المستلمين (تقسيم تلقائي إلى مجموعات)
- معالجة شاملة للأخطاء وإعداد التقارير
- التحقق من الرصيد وإدارة أسماء المرسلين

### التثبيت
```bash
pip install sms4jawaly-py
```

### الاستخدام
```python
from sms4jawaly_py import SMS4JawalyClient

# تهيئة العميل
client = SMS4JawalyClient(
    api_key='your_api_key',
    api_secret='your_api_secret'
)

# إرسال لعدة أرقام (معالجة متوازية تلقائياً)
numbers = ['966500000000', '966500000001']
result = client.send_sms(
    message='رسالة تجريبية من 4jawaly!',
    numbers=numbers,
    sender='YOUR_SENDER_NAME'
)

# التحقق من النتائج
print(f'نجاح: {result["total_success"]} رسالة')
print(f'فشل: {result["total_failed"]} رسالة')
if result["job_ids"]:
    print(f'معرفات المهام: {result["job_ids"]}')
if result["errors"]:
    print(f'الأخطاء: {result["errors"]}')
```

## 🇫🇷 Français

Bibliothèque Python pour l'envoi de SMS via la passerelle 4jawaly avec support pour l'envoi parallèle et le traitement par lots.

### Caractéristiques
- Envoi parallèle de SMS avec traitement automatique par lots
- Support pour un grand nombre de destinataires (division automatique en lots)
- Gestion complète des erreurs et rapports
- Vérification du solde et gestion des noms d'expéditeur

### Installation
```bash
pip install sms4jawaly-py
```

### Utilisation
```python
from sms4jawaly_py import SMS4JawalyClient

# Initialiser le client
client = SMS4JawalyClient(
    api_key='your_api_key',
    api_secret='your_api_secret'
)

# Envoi à plusieurs numéros (traitement parallèle automatique)
numbers = ['966500000000', '966500000001']
result = client.send_sms(
    message='Message test de 4jawaly!',
    numbers=numbers,
    sender='YOUR_SENDER_NAME'
)

# Vérifier les résultats
print(f'Succès: {result["total_success"]} messages')
print(f'Échec: {result["total_failed"]} messages')
```

## 🇵🇰 اردو

4jawaly SMS گیٹ وے کے ذریعے SMS پیغامات بھیجنے کے لیے پائتھن لائبریری، متوازی بھیجنے اور بیچ پروسیسنگ کی سہولت کے ساتھ۔

### خصوصیات
- خودکار بیچ پروسیسنگ کے ساتھ متوازی SMS بھیجنا
- بڑی تعداد میں وصول کنندگان کی سہولت (خودکار طور پر حصوں میں تقسیم)
- جامع غلطی کی نشاندہی اور رپورٹنگ
- بیلنس چیکنگ اور بھیجنے والے ناموں کا انتظام

### انسٹالیشن
```bash
pip install sms4jawaly-py
```

### استعمال
```python
from sms4jawaly_py import SMS4JawalyClient

# کلائنٹ کو شروع کریں
client = SMS4JawalyClient(
    api_key='your_api_key',
    api_secret='your_api_secret'
)

# متعدد نمبروں پر بھیجیں (خودکار متوازی پروسیسنگ)
numbers = ['966500000000', '966500000001']
result = client.send_sms(
    message='4jawaly سے ٹیسٹ پیغام!',
    numbers=numbers,
    sender='YOUR_SENDER_NAME'
)

# نتائج چیک کریں
print(f'کامیاب: {result["total_success"]} پیغامات')
print(f'ناکام: {result["total_failed"]} پیغامات')
