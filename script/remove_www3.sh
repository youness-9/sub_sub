#!/bin/bash

file_path="../sub_sub/3.txt"

# قم بقراءة الملف وحذف الكلمة "www." من كل سطر
sed -i 's/www\.//g' "$file_path"

# قم بطباعة رسالة تأكيد الانتهاء
echo "تم حذف الكلمة 'www.' من الملف بنجاح"