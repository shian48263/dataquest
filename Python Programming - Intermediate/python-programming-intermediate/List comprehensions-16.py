## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ships[i])
    print(cars[i])

## 3. Adding columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, thing in enumerate(things):
    thing.append(trees[i])

## 4. List comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [price * 2 for price in apple_prices]
apple_prices_lowered = [price - 100 for price in apple_prices]

## 5. Counting up female names ##

name_counts = {}
for row in legislators:
    if row[3] == 'F' and row[7] > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1


## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = [value is not None and value > 30 for value in values]

## 8. Highest female name count ##

max_value = None
for count in name_counts:
    if max_value is None or name_counts[count] > max_value:
        max_value = name_counts[count]

## 9. The items method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for name, kind in plant_types.items():
    print(name)
    print(kind)

## 10. Finding the most common female names ##

top_female_names = []
top_female_names = [name for name, count in name_counts.items() if count == 2]

## 11. Finding the most common male names ##

top_male_names = []
male_name_counts = {}
for legis in legislators:
    if legis[3] is 'M' and legis[7] > 1940:
        if legis[1] in male_name_counts:
            male_name_counts[legis[1]] += 1
        else:
            male_name_counts[legis[1]] = 1
highest_male_count = None
for name, count in male_name_counts.items():
    if highest_male_count is None or highest_male_count < count:
        highest_male_count = count
top_male_names = [name for name, count in male_name_counts.items() if count is highest_male_count]