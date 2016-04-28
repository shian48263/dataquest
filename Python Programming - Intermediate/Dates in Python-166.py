## 1. The time module ##

import time
current_time = time.time()

## 2. Converting timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
print(current_hour)

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.now()
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime
today = datetime.datetime.now()
diff = datetime.timedelta(days = 1)
tomorrow = today + diff
yesterday = today - diff

## 5. Formatting dates ##

import datetime
mystery_date_formatted_string = mystery_date.strftime('%I:%M%p on %A %B %d, %Y')
print(mystery_date_formatted_string)

## 6. Parsing dates ##

import datetime
mystery_date = datetime.datetime.strptime(mystery_date_formatted_string, '%I:%M%p on %A %B %d, %Y')

## 8. Reformatting our data ##

import datetime
for row in posts:
    row[2] = datetime.datetime.fromtimestamp(float(row[2]))

## 9. Counting posts in March ##

march_count = 0
for row in posts:
    if row[2].month == 3:
        march_count += 1

## 10. Counting posts in any month ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1
        
def count_posts_in_month(m):
    count = 0
    for row in posts:
        if row[2].month == m:
            count += 1
    return count
feb_count = count_posts_in_month(2)
aug_count = count_posts_in_month(8)