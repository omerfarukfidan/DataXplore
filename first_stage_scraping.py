import requests
from bs4 import BeautifulSoup

url = "https://tr.wikipedia.org/wiki/T%C3%BCrk_dizileri_listesi"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find_all('table', {'class': 'wikitable'})

    data_list = []

    for table in tables:

        rows = table.find_all('tr')

        for row in rows[1:]:  
            columns = row.find_all(['th', 'td'])
            
            title = columns[0].text.strip()
            
            link = columns[0].find('a')['href'] if columns[0].find('a') else None
            
            if link is None:
                continue
            
            if '/w/index' in link:
                continue
            else:
                link = "https://tr.wikipedia.org/" + link

            data_list.append({
                "Dizi Adı": title,
                "Link": link
            })

    with open("diziler.txt", "w", encoding="utf-8") as file:
        for data in data_list:
            file.write(f"Dizi Adı: {data['Dizi Adı']}, Link: {data['Link']}\n")

    print("Veriler 'diziler.txt' dosyasına yazıldı.")

else:
    print(f"Hata: {response.status_code}")