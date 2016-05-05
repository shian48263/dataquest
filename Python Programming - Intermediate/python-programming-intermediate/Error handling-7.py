## 2. Sets ##

import csv
legislators = list(csv.reader(open('legislators.csv', 'r')))

gender = []
for legislator in legislators:
    gender.append(legislator[3])

gender = set(gender)
print(gender)

## 3. Exploring the dataset ##

import csv
legislators = list(csv.reader(open('legislators.csv', 'r')))

party = []
for legislator in legislators:
    party.append(legislator[6])

party = set(party)
print(party)
print(legislators)

## 4. Missing values ##

for legislator in legislators:
    if legislator[3] == '':
        legislator[3] = 'M'

## 5. Parsing birth years ##

birth_years = []
for legis in legislators:
    parts = legis[2].split('-')
    birth_years.append(parts[0])

## 6. Try/except blocks ##

try:
    float('hello')
except Exception:
    print('Error converting to float.')

## 7. Exception instances ##

try:
    int('')
except Exception as exc:
    print(type(exc), str(exc))

## 8. The pass keyword ##

converted_years = []

for year in birth_years:
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)

## 9. Convert birth years to integers ##

for row in legislators:
    birth_year = row[2].split('-')[0]
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    row.append(birth_year)

## 10. Fill in years without a value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]