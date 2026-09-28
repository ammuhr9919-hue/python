cities={
    "bengaluru":"bisi bele bath",
    "davngere":"bene dosa",
    "shivamoga":"rice"
}
print("original cities:")
print(cities)
cities["udupi"]="udupi masala dosa"
print("after adding:")
print(cities)
cities["bengaluru"]="sweet"
print("after dish change:")
print(cities)
cities.pop("shivamoga")
print("after removing:")
print(cities)
print("all cities name:")
print(cities.keys())
print("all dishes:")
print("famous dish:")
print(cities.values())      