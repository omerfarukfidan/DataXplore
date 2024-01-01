import pandas as pd

def txt_to_csv(txt_filename, csv_filename):
    with open(txt_filename, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    data_list = []
    current_data = {}

    for line in lines:
        line = line.strip()
        if line.startswith("Dizi Adı:"):
            if current_data:
                data_list.append(current_data)
            current_data = {"Dizi Adı": line.split(":")[1].strip()}
        else:
            parts = line.split(":")
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                current_data[key] = value

    if current_data:
        data_list.append(current_data)

    df = pd.DataFrame(data_list)
    df.to_csv(csv_filename, index=False, encoding='utf-8')

if __name__ == "__main__":
    txt_to_csv("öznitelik.txt", "öznitelik.csv")
    print("Veriler 'öznitelik.csv' dosyasına dönüştürüldü.")