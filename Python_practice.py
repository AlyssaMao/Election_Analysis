
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for county,voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
for i in range (len(voting_data)):
    print(voting_data[i])

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")