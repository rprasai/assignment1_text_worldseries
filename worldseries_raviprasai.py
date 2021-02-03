winners = open("WorldSeriesWinners.txt", "r")
year = int(input("Enter the Year between 1903-2009: "))
# year = 1907
champ = winners.read()
champ = champ.split("\n")
# print(champ)

# Creating a dictionary with years as key and team as vlaue
year_winners = {}
years = 1903
for team in champ:
    year_winners[years] = team
    if years == 1903 or years == 1993:
        years += 2
    else:
        years += 1
# print(year_winners)


# Creating a dictionary with team as key and numeber of times won as value
win_count = {}
for team in champ:
    win_count[team] = win_count.get(team, 0) + 1
# print(win_count)

# displaying the output
print(year, ": ", year_winners[year], ": ", win_count[year_winners[year]], "times")
