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
                    elif "Başrol" in header_text:
                        ozellikler["Başrol"] = data_text
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
                    elif "Tema müziği bestecisi" in header_text:
                        ozellikler["Tema Müziği Bestecisi"] = data_text
                    elif "Ülke" in header_text:
                        ozellikler["Ülke"] = data_text
            konu_icerigi = soup.find('div', {'id': 'mw-content-text'}).find('p')
            if konu_icerigi:
                ozellikler["Konu"] = konu_icerigi.text.strip()

            return ozellikler
        else:
            print(f"Link: {link} - Öznitelik bilgileri bulunamadı.")
            return None
    else:
        print(f"Hata: {response.status_code}")
        print(f"{link}")
        return None


def main():
    with open("diziler.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("öznitelik.txt", "w", encoding="utf-8") as output_file:
        for line in lines:
            link_start = line.find("Link: ") + len("Link: ")
            link_end = line.find("\n", link_start)
            link = line[link_start:link_end].strip()

            dizi_adi_start = line.find("Dizi Adı: ") + len("Dizi Adı: ")
            dizi_adi_end = link_start - 2
            dizi_adi = line[dizi_adi_start:dizi_adi_end].strip()

            output_file.write(f"\nDizi Adı: {dizi_adi}\n")

            ozellikler = get_dizi_ozellikleri(link)

            if ozellikler:
                for key, value in ozellikler.items():
                    output_file.write(f"{key}: {value}\n")

    print("\nÖznitelikler 'öznitelik.txt' dosyasına yazıldı.")

if __name__ == "__main__":
    main()
