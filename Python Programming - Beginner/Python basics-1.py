## 3. Variables ##

b = 5
b=6

## 4. Comments ##

# Here's a comment!
b = 5 # Assign 5 to b
# Here's another comment! Neither of these comments are evaluated by Python!

## 5. Print function ##

b = 6
print(b)
print(500)

## 6. Types ##

# Integer
i = 1
# String
s = "Hello World"
# Float
f = 55.55
hundred_integer = 100
hundred_string = "hundred"
hundred_float = 100.5

## 7. Type function ##

a = type(5)
# The type is assigned to a. When you print the type, it is abbreviated to `str`
print(a)

c = type(10)
print(c)

## 8. Arithmetic operators ##

five = 5
twenty_five = five * five
negative_five = five - five * 2

## 9. Converting types ##

ten = "10"
eight = 8
str_eight = str(eight)
int_ten = int(ten)

## 11. Lists ##

l = []

# Print the type of `l` to confirm it's a list.
print(type(l))
l.append("January")
l.append("February")
print(l)
l.append('March')
l.append('April')
print(l)

## 12. Creating lists with values ##

l = ["January", "February", "March", "April"]
m = [0,1,2,3]
years = [2010, 2011, 2012, 2013, 2014]

## 13. Multiple types in list ##

o = ['Jan', 5.0, 1.0, 'uary', 10]

## 14. List index ##

int_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
index_four = int_months[4]
last_value = int_months[-1]

## 15. List length ##

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
second_last = months[-2]
print(second_last)

## 16. List slicing ##

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
eight_eleven = months[8:12]
ending_index = len(months)
eight_eleven = months[8:ending_index]
five_nine = months[5:10]
print(months[0:5])