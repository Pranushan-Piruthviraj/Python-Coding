# city_list  = []
# while True:
#     city = input("Which cities have you visisted (enter quit to exit): ")
#     if city != "quit":
#         print(city)
#     else:
#         print("Requested quit")
#         break
#     city_list.append(city)
# print(city_list)

# country_dictionary = {}
# while True:
#     country = input("Which countries have you visisted in the last 5 years? (enter quit to exit): ")
#     if country != "quit":
#         print(country)
#     else:
#         print("Requested quit")
#         break
#     city_list = []
#     while True:
#         cities = input("Which cities have you visisted? (enter quit to exit): ")
#         if cities != "quit":
#             print(cities)
#         else:
#             print("Requested quit")
#             break
#         city_list.append(cities) 
#     country_dictionary[country] = city_list
# print(country_dictionary)

# list_numbers = [0,2,5,6,9]
# for element in range(len(list_numbers)):
#     if list_numbers[element] %2 == 0:
#         continue
#     list_numbers[element] = list_numbers[element] * 2
# print(list_numbers)

country_dict = {"Canada": ["Toronto","Vancouver"], "U.S.": ["New York","Buffalo", "California"], "Europe": ["Germany","France"]}
for k in country_dict.keys():
    if k == "Canada":
        continue
    for c in range(len(country_dict[k])):
        if c == 0:
            print(country_dict[k][0])
        else:
            break