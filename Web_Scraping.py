import requests
from bs4 import BeautifulSoup

# URL tanımla
url = 'http://192.168.1.18/dvwa/'

# Sayfayı getir
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # 1. Sayfa başlığı
    title = soup.title.string if soup.title else "Başlık bulunamadı"
    print(f"Sayfa Başlığı: {title}")

    # 2. Sayfadaki tüm linkler
    print("\nSayfadaki Bağlantılar:")
    links = soup.find_all('a')
    if links:
        for link in links:
            href = link.get('href', 'Bağlantı yok')
            text = link.text.strip() or "Bağlantı metni yok"
            print(f"- Metin: {text}, URL: {href}")
    else:
        print("Sayfada bağlantı bulunamadı.")

    # 3. Sayfadaki formlar
    print("\nSayfadaki Formlar:")
    forms = soup.find_all('form')
    if forms:
        for form in forms:
            action = form.get('action', 'Action yok')
            method = form.get('method', 'Method yok')
            inputs = form.find_all('input')
            input_names = [inp.get('name', 'İsimsiz') for inp in inputs]
            print(f"- Action: {action}, Method: {method}, Input Alanları: {input_names}")
    else:
        print("Sayfada form bulunamadı.")

    # 4. Tablolar
    print("\nSayfadaki Tablolar:")
    tables = soup.find_all('table')
    if tables:
        for idx, table in enumerate(tables):
            print(f"\nTablo {idx + 1}:")
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all(['th', 'td'])
                print([col.text.strip() for col in cols])
    else:
        print("Sayfada tablo bulunamadı.")
else:
    print(f"Hata: {response.status_code}")
