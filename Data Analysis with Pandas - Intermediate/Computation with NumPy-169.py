## 2. Array comparisons ##

countries_canada = world_alcohol[:,2] == 'Canada'
years_1984 = world_alcohol[:,0] == '1984'

## 3. Selecting elements ##

country_is_algeria = world_alcohol[:,2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria,:]

## 4. Comparisons with multiple conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]
print(rows_with_algeria_and_1986)

## 5. Replacing values ##

is_1986 = world_alcohol[:,0] == '1986'
is_wine = world_alcohol[:,3] == 'Wine'
print(world_alcohol[is_1986,:])
print(world_alcohol[is_wine,:])
world_alcohol[is_1986,0] = '2014'
world_alcohol[is_wine,3] = 'Grog'
is_2014 = world_alcohol[:,0] == '2014'
is_grog = world_alcohol[:,3] == 'Grog'
print(world_alcohol[is_2014,:])
print(world_alcohol[is_grog,:])

## 6. Replacing empty strings ##

is_value_empty = world_alcohol[:,4] == ''
print(world_alcohol[is_value_empty,:].shape)
world_alcohol[is_value_empty,4] = '0'

## 7. Converting data types ##

alcohol_consumption = world_alcohol[:,4].astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total alcohol consumption in a year ##

is_canada_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol_unformatted = canada_1986[:,4]
is_empty = canada_alcohol_unformatted == ''
canada_alcohol_unformatted[is_empty] = '0'
canada_alcohol = canada_alcohol_unformatted.astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating consumption for each country ##

totals = {}
is_1989 = world_alcohol[:,0] == '1989'
world_alcohol_1989 = world_alcohol[is_1989,:]
def find_total(country):
    is_country = world_alcohol_1989[:,2] == country
    country_alcohol = world_alcohol_1989[is_country,4]
    is_empty = country_alcohol == ''
    country_alcohol[is_empty] = '0'
    return country_alcohol.astype(float).sum()
for country in countries:
    totals[country] = find_total(country)

## 11. Finding the country that drinks the most ##

highest_value = 0
highest_key = None
for country in totals:
    if highest_value < totals[country]:
        highest_key = country
        highest_value = totals[country]