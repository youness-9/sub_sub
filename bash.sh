#!/bin/bash

read -p "Enter the number of threads: " num_threads

output_dir="sub_sub"
mkdir -p "$output_dir"

counter=0

while read -r domain || [[ -n "$domain" ]]; do
    echo "Processing domain: $domain"
    subfinder -d "$domain" >> "$output_dir/1.txt" &
    ((counter++))

    if ((counter % num_threads == 0)); then
        wait
    fi
done < list.txt

wait
echo "Subdomain enumeration completed. Results saved to $output_dir/1.txt."

# إزالة النتائج المكررة
python3 python/filterfdomin.py
wait
bash script/remove_www1.sh
sort -u -o "$output_dir/1.txt" "$output_dir/1.txt"
###############################################
echo "$num_threads" | bash king/bash1.sh
wait
python3 python/filterfdomin1.py
wait
bash script/remove_www2.sh
sort -u -o "$output_dir/2.txt" "$output_dir/2.txt"
################################################
echo "$num_threads" | bash king/bash2.sh
wait
python3 python/filterfdomin2.py
wait
bash script/remove_www3.sh
sort -u -o "$output_dir/3.txt" "$output_dir/3.txt"

python3 yo.py

input_file="all_in_one.txt"
output_file="all_in_one_unique.txt"
awk '!seen[$0]++' "$input_file" > "$output_file"

echo "تم إنشاء الملف $output_file بنجاح."

python3 filterfdomin.py
echo "800" | python3 king/200OK1.py
