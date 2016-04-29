## 2. Lists of lists ##

import csv
world_alcohol = list(csv.reader(open('world_alcohol.csv', 'r')))
years = [row[0]for row in world_alcohol]
years = years[1:]
total = 0
for year in years:
    total += float(year)
avg_year = total/len(years)

## 4. Using NumPy ##

import numpy
world_alcohol = numpy.genfromtxt('world_alcohol.csv', delimiter = ',')
print(type(world_alcohol))

## 5. Creating arrays ##

vector = [10, 20, 30]
matrix = [[5, 10, 15], [20, 25, 30], [35, 40, 45]]
print(type(matrix))

## 6. Array shape ##

vector = numpy.array([10, 20, 30])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
vector_shape = vector.shape
matrix_shape = matrix.shape

## 7. Data types ##

world_alcohol_dtype = world_alcohol.dtype

## 9. Reading in the data properly ##

import numpy
world_alcohol = numpy.genfromtxt('world_alcohol.csv', delimiter=',', skip_header=True, dtype='U75')
print(world_alcohol)

## 10. Indexing arrays ##

uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]

## 11. Slicing arrays ##

countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]
print(countries, alcohol_consumption)

## 12. Slicing one dimension ##

first_two_columns = world_alcohol[:,0:2]
first_ten_years = world_alcohol[0:10,0]
first_ten_rows = world_alcohol[0:10,:]
print(first_two_columns, first_ten_years, first_ten_rows)
print(type(first_two_columns), type(first_ten_years), type(first_ten_rows))

## 13. Slicing arrays ##

first_twenty_regions = world_alcohol[0:20,1:3]