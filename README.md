# Türkiye Adres Scraper Projesi

Bu proje, e-icisleri.gov.tr adresinden il, ilçe, mahalle ve posta kodu bilgilerini çekerek JSON formatında veri üretir.
Python + Selenium ile yapılmıştır.
# 📌 Türkiye Adres Scraper

Bu proje, [e-İçişleri Bakanlığı](https://www.e-icisleri.gov.tr/Anasayfa/MulkiIdariBolumleri.aspx) web sitesinden Türkiye'deki **il**, **ilçe**, **mahalle** ve **posta kodu** bilgilerini çekerek JSON formatında bir veri seti oluşturur.

## 🎯 Proje Amacı

E-İçişleri sitesindeki güncel adres bilgilerini programatik olarak çekmek ve yazılımlarda kullanılabilecek bir yapıya dönüştürmek.

---

## 🛠 Kullanılan Teknolojiler

- 🐍 Python 3
- 🌐 Selenium
- 🧭 Chrome WebDriver (otomatik tarayıcı kontrolü)
- 📦 JSON formatı (veri kaydı)
- ⚙️ `webdriver-manager` (driver yönetimi)

---

## 🔧 Kurulum

1. Bu projeyi klonlayın:

```bash
git clone https://github.com/Rana12408/adres-scraper.git
cd adres-scraper
Gerekli Python paketlerini yükleyin:
pip install selenium webdriver-manager
Script'i çalıştırın:
python main.py

📁 JSON Veri Yapısı:
[
  {
    "il_id": "1",
    "il_adi": "ADANA",
    "ilceler": [
      {
        "ilce_id": "12",
        "ilce_adi": "ALADAĞ",
        "mahalleler": [
          {
            "mahalle_id": "1_2",
            "mahalle_adi": "AKÖREN MAH",
            "posta_kodu": "01722"
          }
        ]
      }
    ]
  }
]
Not: Yukarıdaki sadece örnek bir yapıdır, script çalıştırıldığında tüm iller ve ilçeler için veri elde edilir.
⚠️ Uyarılar
Site yapısı değişirse script yeniden uyarlanmalıdır.

Web scraping işlemleri sırasında sunucuya çok sık istek gönderilmemesine dikkat edilmelidir.

Bu proje yalnızca eğitim ve kişisel kullanım amaçlıdır.
