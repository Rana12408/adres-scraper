from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# tarayıcıyı başlat belirtilen url ye git
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.e-icisleri.gov.tr/Anasayfa/MulkiIdariBolumleri.aspx")

wait = WebDriverWait(driver, 15)

data = []

# İlk il dropdown'u bul
for il_index in range(1, 82):  # Türkiye'deki 81 il olduğu için sabit sayıyı kullandım,
    # İl dropdown'u her döngüde yeniden bul
    il_dropdown = wait.until(EC.presence_of_element_located((By.ID, "ctl00_cph1_CografiBirimControl_DropDownListIl")))
    select_il = Select(il_dropdown)

    il_option = select_il.options[il_index]
    il_id = il_option.get_attribute("value")
    il_adi = il_option.text.strip()

    if il_id in ("", "-1"):
        continue

    select_il.select_by_value(il_id)
    time.sleep(1)  # Bekle, sayfa yenilensin

    # İlçe dropdown'u yeniden bul
    ilce_dropdown = wait.until(EC.presence_of_element_located((By.ID, "ctl00_cph1_CografiBirimControl_DropDownListIlce")))
    select_ilce = Select(ilce_dropdown)

    ilceler_list = []
    ilce_options_count = len(select_ilce.options)
    for ilce_index in range(1, ilce_options_count):
        ilce_dropdown = wait.until(EC.presence_of_element_located((By.ID, "ctl00_cph1_CografiBirimControl_DropDownListIlce")))
        select_ilce = Select(ilce_dropdown)

        ilce_option = select_ilce.options[ilce_index]
        ilce_id = ilce_option.get_attribute("value")
        ilce_adi = ilce_option.text.strip()

        if ilce_id in ("", "-1"):
            continue

        select_ilce.select_by_value(ilce_id)
        time.sleep(1)

        mahalle_dropdown = wait.until(EC.presence_of_element_located((By.ID, "ctl00_cph1_CografiBirimControl_DropDownListKoy")))
        select_mahalle = Select(mahalle_dropdown)

        mahalleler_list = []
        mahalle_options_count = len(select_mahalle.options)
        for mahalle_index in range(1, mahalle_options_count):
            mahalle_option = select_mahalle.options[mahalle_index]
            mahalle_id = mahalle_option.get_attribute("value")
            mahalle_adi = mahalle_option.text.strip()

            if mahalle_id in ("", "-1"):
                continue

            posta_kodu = ""

            mahalleler_list.append({
                "mahalle_id": mahalle_id,
                "mahalle_adi": mahalle_adi,
                "posta_kodu": posta_kodu
            })

        ilceler_list.append({
            "ilce_id": ilce_id,
            "ilce_adi": ilce_adi,
            "mahalleler": mahalleler_list
        })

    data.append({
        "il_id": il_id,
        "il_adi": il_adi,
        "ilceler": ilceler_list
    })

driver.quit()

# EKRANA YAZDIRMAK YERİNE .JSON DOSYASINA KAYDEDİYORUZ
with open("turkiye_il_ilce_mahalle.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ JSON dosyası başarıyla oluşturuldu: turkiye_il_ilce_mahalle.json")
