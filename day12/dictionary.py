cities={
    "bengaluru":123,
    "mysuru":12,
    "davangere":10,
    "udupi":9,
    "shivamoga":8
}
small_cities={
    city:population
    for city,population in 
    cities.items()
    if population<10
    }
print("cities below to 10 laks:")
print(small_cities)