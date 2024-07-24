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

sort -u -o "$output_dir/1.txt" "$output_dir/1.txt"

echo "Duplicate entries removed from $output_dir/1.txt."
echo "100" | python3 200OK.py
echo "$num_threads" | bash king/bash1.sh
echo "100" | python3 king/200OK1.py

echo "$num_threads" | bash king/bash2.sh
echo "100" | python3 king/200OK2.py


