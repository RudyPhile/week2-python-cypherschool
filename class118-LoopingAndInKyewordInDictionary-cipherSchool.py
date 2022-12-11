# in keyword and iteration in dictionary

user_info = {
    "name" : "harshit",
    "age" : 24,
    "fav_movies":["coco","kimi no na wa"],
    "fav_tunes" : ["awakening","fairy tale"],
    }

    # check if key existy in dictionary

# if "name" in user_info:
#     print("present")
# else:
#     print("not present")


    # check if value exists in dictionary
# if "harshit" in user_info.values():
#     print("present")
# else:
#     print("not present")
 
    # loop in dictionaries
# for i in user_info.value():
#     print(i)

# value method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# loops in dictionaries
# for i in user_info:
    # print(user_info[i])

# item method
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))
# [("name", "Harshit"),("age",24),("fav_movies":["coco","kimi no na wa"]),("fav_tunes" : ["awakening","fairy tale"])]

for key, value in user_info.item():
    # print(f"key is {key} and value is {value}")
    print(key)
