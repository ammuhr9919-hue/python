city={
    "bengaluru":"peda",
    "davangere":"dosa",
    "chickmangaluru":"sweet"
}
print("original city:")
print(city)
city["ublli"]="roti"
city["bengaluru"]="sambar"
city.pop("shivamogga","sweet")
print("\ncity name:")
print(city.keys())
print("\ndishes:")
print(city.values())