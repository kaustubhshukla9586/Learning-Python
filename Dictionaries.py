dict = {
    "India": "New Delhi",
    "United States": "Washington, D.C.",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Japan": "Tokyo",
    "China": "Beijing",
    "Russia": "Moscow",
    "Canada": "Ottawa",
    "Brazil": "Brasília",
    "Australia": "Canberra",
    "South Africa": "Pretoria",
}
#print(dict.items())
#if dict.get("Na"):
 #   print("That Capitals Exists")
#else:
#    print("That Capitals Doesn't Exist")

#dict.update({"Russia": "Berlin"})
#print(dict.get("Russia"))
#dict.pop("United States")
#print(dict.get("United States"))
#keys = [dict.keys()]
#print(keys)

values = dict.values()
keys = dict.keys()

for key, value in dict.items():
    print(f"The Captial of {key} is: {value}")


