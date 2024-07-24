import threading
import requests
import os

def check(domain):
    try:
        response = requests.get('http://' + domain)
        status_code = response.status_code

        folder_name = "result_status"

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        filename = f"{folder_name}/result_{status_code}.txt"

        with open(filename, 'a') as file:
            file.write(domain + '\n')

        print(f"has been save{domain} in {filename}.")
    except requests.exceptions.RequestException:
        print(f"nor work {domain}.")

def process_domains(domains, num_threads):
    thread_pool = []
    for domain in domains:
        thread = threading.Thread(target=check, args=(domain,))
        thread_pool.append(thread)
        thread.start()

    for thread in thread_pool:
        thread.join()

output_path = 'sub_sub/3.txt'

# افتح ملف النطاقات
with open(output_path, 'r') as file:
    domains = file.read().splitlines()

num_threads = int(input("Enter the number of threads:"))
process_domains(domains, num_threads)

