## 1. Introduction to the data ##

import csv
nfl_suspensions = list(csv.reader(open('nfl_suspensions_data.csv', 'r')))
nfl_suspensions = nfl_suspensions[1:]
years = {}
for nfl in nfl_suspensions:
    if nfl[5] in years:
        years[nfl[5]] += 1
    else:
        years[nfl[5]] = 1
print(years)

## 2. Unique values ##

unique_teams = set([nfl[1] for nfl in nfl_suspensions])
unique_games = set([nfl[2] for nfl in nfl_suspensions])
print(unique_teams, unique_games)

## 3. Suspension class ##

class Suspension():
    def __init__(self, row):
        nfl = nfl_suspensions[row]
        self.name = nfl[0]
        self.team = nfl[1]
        self.team = nfl[2]
        self.team = nfl[5]

third_suspension = Suspension(2)

## 4. Tweaking the Suspension class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)
        
missing_year = Suspension(nfl_suspensions[23])
twenty_fourth_year = missing_year.get_year()