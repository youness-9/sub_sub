import threading
import requests
import os

def check(domain):
    try:
        response = requests.get('http://' + domain, timeout=5, allow_redirects=False,verify=False)
        status_code = response.status_code

        # اسم المجلد
        folder_name = "result_status"

        # إنشاء المجلد إذا لم يكن موجودًا
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # اسم الملف يعتمد على رمز حالة الاستجابة
        filename = f"{folder_name}/result_{status_code}.txt"

        # حفظ الروابط في ملفات بأسماء مختلفة
        with open(filename, 'a') as file:
            file.write(domain + '\n')

        print(f"تم حفظ الرابط {domain} في الملف {filename}.")
    except requests.exceptions.RequestException:
        print(f"فشلت زيارة النطاق {domain}.")

def process_domains(domains, num_threads):
    thread_pool = []
    for domain in domains:
        thread = threading.Thread(target=check, args=(domain,))
        thread_pool.append(thread)
        thread.start()

    for thread in thread_pool:
        thread.join()
        
script_dir = os.path.dirname(os.path.abspath(__file__))  
output_path = os.path.join(script_dir, "..", "hits.txt")


# افتح ملف النطاقات
with open(output_path, 'r') as file:
    domains = file.read().splitlines()

num_threads = int(input("أدخل عدد الخيوط: "))
process_domains(domains, num_threads)

print("تم حفظ الروابط في الملفات بناءً على رمز حالة الاستجابة.")