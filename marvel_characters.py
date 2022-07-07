marvel_characters=[
"Thor 1962",
"Spider-Man 1962",
"Deadpool 1986",
"Iron Man 1963",
"Hulk 1962",
"Wolverine 1974",
"Captain America 1941",
"Doctor Strange 1963",
"Black Panther 1966",
"Groot 2007",
"Scarlet Witch 1964",
"Rocket Raccoon 1982",
"Ant-Man 1962",
"Black Widow 1940",
"Punisher 1974",
"Silver Surfer 1966",
"Ghost Rider 1972",
"Star-Lord 2004",
"Vision 1940",
"Hawkeye 1964",
"Gambit 1990",
"Phoenix 1963",
"Ms. Marvel 1968",
"Nightcrawler 1975",
"Professor X 1963",
"Bucky Barnes 1941",
"Cable 1990",
"Colossus 1975",
"Captain Marvel 1967",
"Human Torch 1939",
"Nova 1976",
"Gamora 1975",
"Odin 1962",
"Blade 1973",
"Drax the Destroyer 1973",
"War Machine 1979",
"Thing 1961",
"Nick Fury 1963",
"Daredevil 1962",
"Moon Knight 1975",
"Beast 1963",
"Iceman 1963",
"Quicksilver 1964",
"Valkyrie 1970",
"Wasp 1963",
"Psylocke 1976",
"Storm 1961",
"X-23 2004",
"Rogue 1981",
"Cyclops 1963"
]
marvel_characters_years_list = []
for character in marvel_characters:
    marvel_characters_years_list.append(character.split(" ")[-1])
print(marvel_characters_years_list)
# print(len(marvel_characters_years_list))
# print(len(marvel_characters))


#make a dictionary with new_year_list as the keys and marvel_characters as the values
marvel_characters_years_dict = {}
for i in range(len(marvel_characters_years_list)):
    marvel_characters_years_dict[marvel_characters[i]] =marvel_characters_years_list[i]
#print(marvel_characters_years_dict)
#reorder the dictionary by the numeric value of the keys
marvel_characters_years_dict_new = sorted(marvel_characters_years_dict, key=lambda i: int(marvel_characters_years_dict[i]))
for item in marvel_characters_years_dict_new:
    print('"'+" ".join(item.split(" ")[:-1])+'",')