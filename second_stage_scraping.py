import requests
from bs4 import BeautifulSoup

def get_dizi_ozellikleri(link):
    response = requests.get(link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        infobox_table = soup.find('table', {'class': 'infobox'})

        if infobox_table:
            rows = infobox_table.find_all('tr')
            ozellikler = {"Link": link} 
            for row in rows:
                header = row.find('th')
                data = row.find('td')

                if header and data:
                    header_text = header.text.strip()
                    data_text = data.text.strip()

                    if "Yayın tarihi" in header_text:
                        ozellikler["Yayın tarihi"] = data_text
                    elif "Durumu" in header_text:
                        ozellikler["Durumu"] = data_text
                    elif "Kanal" in header_text:
                        ozellikler["Kanal"] = data_text
                    elif "Platform" in header_text:
                        ozellikler["Platform"] = data_text
                    elif "Sezon sayısı" in header_text:
                        ozellikler["Sezon Sayısı"] = data_text
                    elif "Bölüm sayısı" in header_text:
                        ozellikler["Bölüm Sayısı"] = data_text
                    elif "Yapımcı" in header_text:
                        ozellikler["Yapımcı"] = data_text
                    elif "Yönetmen" in header_text:
                        ozellikler["Yönetmen"] = data_text
                    elif "Senarist" in header_text:
                        ozellikler["Senarist"] = data_text

            return ozellikler
        else:
            print(f"Link: {link} - Öznitelik bilgileri bulunamadı.")
            return None
    else:
        print(f"Hata: {response.status_code}")
        print(f"{link}")
        return None

