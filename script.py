# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

from pprint import pprint

def format_damages(lst):
    conversion = {"M": 1000000,
                  "B": 1000000000}
    res_lst = []
    for item in lst:
        if item[0].isdigit():
            digits = item[:-1]
            res = float(digits) * conversion[item[-1]]
        else:
            res = item
        res_lst.append(res)
    return res_lst

damages = format_damages(damages)



# write your construct hurricane dictionary function here:
def construct_dict(name, month, year,max_sustained_wind, areas_affected, damage, death):
    res_dict = {}
    for i, key in enumerate(name):
        hur_dict = {
            "Name" : name[i],
            "Month" : month [i],
            "Year" : year[i],
            "Max Sustained Wind" : max_sustained_wind[i],
            "Areas Affected" : areas_affected[i],
            "Damage" : damage[i],
            "Death": death[i]
        }
        res_dict.update({key:hur_dict})
    return res_dict

hurr_dict = construct_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

#pprint(hurr_dict)











# write your construct hurricane by year dictionary function here:
def hurrs_by_year(hurr_dict):
    res_dict = {}
    for hur in hurr_dict.values():
        res_dict.setdefault(hur["Year"], [])
        res_dict[hur["Year"]].append(hur)
    return  res_dict


hurr_by_year = hurrs_by_year(hurr_dict)

#pprint(hurr_by_year)




# write your count affected areas function here:
def count_areas(hurr_dict):
    res_dict = {}
    for hur in hurr_dict.values():
        for area in hur["Areas Affected"]:
            res_dict.setdefault(area,0)
            res_dict[area] += 1
    return res_dict

areas_count = count_areas(hurr_dict)

#pprint(areas_count)







# write your find most affected area function here:
def max_area_affected(areas_dict):
    return {k:v for k,v in areas_dict.items() if v == max(areas_dict.values())}

max_area = max_area_affected(areas_count)

#print(max_area)




# write your greatest number of deaths function here:
def max_deaths(hurr_dict):
    return max(hurr_dict.items(), key = lambda h: h[1]["Death"])

max_death_cane = max_deaths(hurr_dict)

#print(max_death_cane)






# write your catgeorize by mortality function here:

hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

#pprint(hurr_dict)

def mortality_rate_function(hurr_dict):


    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}

    for key_h, value_h in hurr_dict.items():
        #pprint(hurr)
        hurr_deaths = value_h["Death"]

        for key, value in reversed(mortality_scale.items()):
            #pass
            if hurr_deaths > value:
                hurricanes_by_mortality[key+1].append({key_h:value_h})


mortality_rate_function(hurr_dict)

#pprint(hurricanes_by_mortality)



# write your greatest damage function here:

def max_damage(hurr_dict):
    max_key = ""
    max_dmg = 0
    for key, value in hurr_dict.items():
        if isinstance(value["Damage"], float):
            #print(f"{value['Damage']:,}")
            if value["Damage"] > max_dmg:
                max_dmg = value["Damage"]
                max_key = key
    #print(f"{max_dmg:,}")
    return {max_key:hurr_dict[max_key]}

max_damage_cane = max_damage(hurr_dict)

pprint(max_damage_cane)

'''
for dmg in damages:
    if isinstance(dmg, float):
        print(f"{dmg:,.0f}")
'''







# write your catgeorize by damage function here:
hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}

def damage_rate_function(hurr_dict):

    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}

    for key_h, value_h in hurr_dict.items():
        #pprint(hurr)
        hurr_dmg = value_h["Damage"]

        if not isinstance(hurr_dmg, float):
            continue

        for key, value in reversed(damage_scale.items()):
            #pass
            if hurr_dmg > value:
                hurricanes_by_damage[key+1].append({key_h:value_h})


damage_rate_function(hurr_dict)

pprint(hurricanes_by_damage)