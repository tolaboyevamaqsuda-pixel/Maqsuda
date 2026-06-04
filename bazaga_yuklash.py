import os
import django
import pandas as pd

# Django muhitini sozlash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medcluster.settings')
django.setup()

from documents.models import Document

def import_csv():
    file_path = 'Tibbiyot.csv'
    if not os.path.exists(file_path):
        print("Tibbiyot.csv topilmadi!")
        return

    print("CSV o'qilmoqda...")
    # Matnli ustunlarni aniq o'qish uchun dtype dan foydalanamiz
    df = pd.read_csv(file_path)
    
    # Bizga kerakli ustun nomi: 'Matn'
    col_name = 'Matn' 
    
    if col_name not in df.columns:
        print(f"Xato: CSV ichida '{col_name}' ustuni topilmadi!")
        print(f"Mavjud ustunlar: {list(df.columns)}")
        return

    print(f"Ma'lumotlar '{col_name}' ustunidan olinmoqda...")

    objects_to_create = []
    count = 0

    for index, row in df.iterrows():
        # Matnni olamiz va uni stringga o'tkazamiz
        val = str(row[col_name]).strip()
        
        # Bo'sh yoki 'nan' matnlarni tashlab ketamiz
        if val.lower() == 'nan' or len(val) < 3:
            continue

        objects_to_create.append(
            Document(
                id=index + 1,
                matn=val
            )
        )
        
        if len(objects_to_create) >= 2000:
            Document.objects.bulk_create(objects_to_create, ignore_conflicts=True)
            count += len(objects_to_create)
            objects_to_create = []
            print(f"{count} ta haqiqiy matn yuklandi...")

    if objects_to_create:
        Document.objects.bulk_create(objects_to_create, ignore_conflicts=True)
        count += len(objects_to_create)
    
    print(f"\nMUVAFFAQIYATLI! Bazada jami {Document.objects.count()} ta matnli hujjat saqlandi.")

if __name__ == '__main__':
    import_csv()