#syntax : {new_key:new_value for (key,value) in dict.item() if condition}

import random
city_name=['Paris','London','Rome','Berlin','Madrid']
city_temp={city:random.randint(20,30) for city in city_name}
print(city_temp)

new_dict2={city:temp for (city,temp) in city_temp.items() if temp>25}
print(new_dict2)