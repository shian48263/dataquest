## 3. Read the file into string ##

data = open('dq_unisex_names.csv', 'r').read()

## 4. Convert the string to a list ##

f = open('dq_unisex_names.csv', 'r')
data = f.read()
data_list = data.split('\n')

## 5. Convert the list of strings to a list of lists ##

f = open('dq_unisex_names.csv', 'r')
data = f.read()
data_list = data.split('\n')
string_data = []
for data in data_list:
    string_data.append(data.split(','))

## 6. Convert numerical values ##

print(string_data[0:5])
numerical_data = []
for data in string_data:
    numerical_data.append([data[0], float(data[1])])

## 7. Filter the list ##

# The last value is ~100 people
numerical_data[len(numerical_data)-1]
thousand_or_greater = []
for data in numerical_data:
    if data[1] >= 1000:
        thousand_or_greater.append(data[0])
print(thousand_or_greater[0:10])