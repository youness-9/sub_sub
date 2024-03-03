#!/bin/bash

read -p "Enter the number of threads: " num_threads

output_dir="sub_sub"
mkdir -p "$output_dir"

counter=0

while read -r domain || [[ -n "$domain" ]]; do
    echo "Processing domain: $domain"
    subfinder -d "$domain" >> "$output_dir/3.txt" &
    ((counter++))

    if ((counter % num_threads == 0)); then
        wait
    fi
done < "$output_dir/2.txt"

wait

echo "Subdomain enumeration completed. Results saved to $output_dir/2.txt."

# إزالة النتائج المكررة
sort -u -o "$output_dir/3.txt" "$output_dir/3.txt"

echo "Duplicate entries removed from $output_dir/3.txt."
