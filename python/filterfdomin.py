import os
import chardet

script_dir = os.path.dirname(os.path.abspath(__file__))  # مسار السكريبت الحالي
input_file = os.path.join(script_dir, "..", "sub_sub", "1.txt")  # المسار الكامل للملف النصي الأصلي
output_file = input_file  # يحفظ النتائج في نفس المسار واسم الملف الأصلي
keywords_file = os.path.join(script_dir, "..", "list.txt")  # المسار الكامل لملف الكلمات

# قراءة ملف الكلمات
with open(keywords_file, "r", encoding="utf-8") as keywords_file:
    keywords = keywords_file.read().splitlines()

# تحديد ترميز الملف النصي الأصلي
with open(input_file, "rb") as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result["encoding"]

# قراءة الملف النصي الأصلي واحتفاظ بالأسطر التي تحتوي على الكلمات المطلوبة
with open(input_file, "r", encoding=encoding, errors="ignore") as file:
    lines = file.readlines()
    filtered_lines = [line for line in lines if any(keyword in line for keyword in keywords)]

# حفظ النتائج في نفس الملف الأصلي
with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(filtered_lines)

print("تم حفظ النتائج في الملف", output_file)