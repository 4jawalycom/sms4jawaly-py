# SMS4Jawaly Python SDK

<div dir="rtl">

## 🇸🇦 عربي

مكتبة Python لإرسال الرسائل النصية القصيرة عبر بوابة 4jawaly للرسائل

### المتطلبات

- Python 3.6 أو أحدث
- pip

### التثبيت

```bash
pip install sms4jawaly-py
```

### الاستخدام

```python
from sms4jawaly_py import SMS4JawalyClient

# إنشاء نسخة من العميل
client = SMS4JawalyClient(
    api_key='your_api_key',
    api_secret='your_api_secret',
    sender='YOUR_SENDER_NAME'
)

# إرسال رسالة لرقم واحد
response = client.send_single_sms('966500000000', 'مرحباً من 4jawaly!')
print(f'تم إرسال الرسالة بنجاح: {response.success}')

# إرسال رسالة لعدة أرقام
numbers = ['966500000000', '966500000001']
response = client.send_sms(numbers, 'رسالة جماعية من 4jawaly!')
print(f'تم إرسال: {response.total_success}')
```

</div>

## 🇬🇧 English

Python library for sending SMS messages through the 4jawaly SMS Gateway

### Requirements

- Python 3.6 or later
- pip

### Installation

```bash
pip install sms4jawaly-py
```

### Usage

```python
from sms4jawaly_py import SMS4JawalyClient

# Create client instance
client = SMS4JawalyClient(
    api_key='your_api_key',
    api_secret='your_api_secret',
    sender='YOUR_SENDER_NAME'
)

# Send message to a single number
response = client.send_single_sms('966500000000', 'Hello from 4jawaly!')
print(f'Message sent successfully: {response.success}')

# Send message to multiple numbers
numbers = ['966500000000', '966500000001']
response = client.send_sms(numbers, 'Bulk message from 4jawaly!')
print(f'Sent: {response.total_success}')
```

## 🇫🇷 Français

Bibliothèque Python pour l'envoi de SMS via la passerelle SMS 4jawaly

### Prérequis

- Python 3.6 ou plus récent
- pip

### Installation

```bash
pip install sms4jawaly-py
```

### Utilisation

```python
from sms4jawaly_py import SMS4JawalyClient

# Créer une instance du client
client = SMS4JawalyClient(
    api_key='your_api_key',
    api_secret='your_api_secret',
    sender='YOUR_SENDER_NAME'
)

# Envoyer un message à un seul numéro
response = client.send_single_sms('966500000000', 'Bonjour de 4jawaly!')
print(f'Message envoyé avec succès: {response.success}')

# Envoyer un message à plusieurs numéros
numbers = ['966500000000', '966500000001']
response = client.send_sms(numbers, 'Message groupé de 4jawaly!')
print(f'Envoyé: {response.total_success}')
```

<div dir="rtl">

## 🇵🇰 اردو

4jawaly SMS گیٹ وے کے ذریعے SMS پیغامات بھیجنے کے لیے Python لائبریری

### ضروریات

- Python 3.6 یا اس سے نئی ورژن
- pip

### انسٹالیشن

```bash
pip install sms4jawaly-py
```

### استعمال

```python
from sms4jawaly_py import SMS4JawalyClient

# کلائنٹ انسٹنس بنائیں
client = SMS4JawalyClient(
    api_key='your_api_key',
    api_secret='your_api_secret',
    sender='YOUR_SENDER_NAME'
)

# ایک نمبر پر پیغام بھیجیں
response = client.send_single_sms('966500000000', '4jawaly سے سلام!')
print(f'پیغام کامیابی سے بھیج دیا گیا: {response.success}')

# متعدد نمبروں پر پیغام بھیجیں
numbers = ['966500000000', '966500000001']
response = client.send_sms(numbers, '4jawaly سے اجتماعی پیغام!')
print(f'بھیجے گئے: {response.total_success}')
```

</div>

## 📚 API Documentation / التوثيق / Documentation / دستاویزات

### SMS4JawalyClient

```python
class SMS4JawalyClient:
    def __init__(self, api_key: str, api_secret: str, sender: str):
        """
        Initialize the client
        تهيئة العميل
        Initialiser le client
        کلائنٹ کو شروع کریں
        """
        pass
    
    def send_single_sms(self, number: str, message: str) -> SMSResponse:
        """
        Send to single number
        إرسال لرقم واحد
        Envoyer à un seul numéro
        ایک نمبر پر بھیجیں
        """
        pass
    
    def send_sms(self, numbers: List[str], message: str) -> SMSResponse:
        """
        Send to multiple numbers
        إرسال لعدة أرقام
        Envoyer à plusieurs numéros
        متعدد نمبروں پر بھیجیں
        """
        pass
    
    def get_balance(self, is_active: Optional[int] = None) -> BalanceResponse:
        """
        Check balance
        فحص الرصيد
        Vérifier le solde
        بیلنس چیک کریں
        """
        pass

class SMSResponse:
    success: bool
    total_success: int
    total_failed: int
    job_ids: List[str]
    errors: Optional[Dict[str, List[str]]]

class BalanceResponse:
    balance: float
    packages: Optional[List[Package]]
```

## 📝 License / الترخيص / Licence / لائسنس

MIT License / رخصة MIT / Licence MIT / MIT لائسنس
