## 2. Parsing the file ##

weather_data = []
for data in open('la_weather.csv', 'r').read().split('\n'):
    weather_data.append(data.split(','))


## 3. Getting a single column from the data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for data in weather_data:
    weather.append(data[1])

## 4. Counting the items in a list ##

count = 0
count = len(weather)

## 6. Practice slicing lists ##

slice_me = [7,6,4,5,6]
slice1 = slice_me[2:4]
slice2 = slice_me[1:2]
slice3 = slice_me[3:5]

## 7. Removing the header ##

new_weather = weather[1:]

## 8. The in statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = 'cat' in animals
space_monster_found = 'space_monster' in animals

## 9. Weather types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for weather in weather_types:
    weather_type_found.append(weather in new_weather)