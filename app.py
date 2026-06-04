import os
import pandas as pd

def import_csv():
    file_path = 'Tibbiyot.csv'

    if not os.path.exists(file_path):
        print("Tibbiyot.csv topilmadi!")
        return

    print("CSV o'qilmoqda...")

    df = pd.read_csv(file_path)

    col_name = 'Matn'

    if col_name not in df.columns:
        print(f"Xato: CSV ichida '{col_name}' ustuni topilmadi!")
        print(f"Mavjud ustunlar: {list(df.columns)}")
        return

    print(f"Ma'lumotlar '{col_name}' ustunidan olinmoqda...")

    clean_texts = []
    count = 0

    for index, row in df.iterrows():

        val = str(row[col_name]).strip()

        if val.lower() == 'nan' or len(val) < 3:
            continue

        clean_texts.append(val)
        count += 1

        if count % 2000 == 0:
            print(f"{count} ta matn tayyorlandi...")

    print(f"\nTAYYOR! Jami {len(clean_texts)} ta matn olindi.")

    return clean_texts


if __name__ == '__main__':
    data = import_csv()
    print(data[:5])