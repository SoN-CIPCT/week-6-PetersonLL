web_users = ["j.anderson", "m.chen", "r.patel", "s.williams", "k.oconnor", "t.rodriguez"]
new_users = ["m.chen", "r.patel", "a.johnson", "l.martinez", "d.kim"]
for user in new_users:
    if user in web_users:
        print("This user name is already in use. Please choose a different user name.")
    else:
        print("This user name is available.")

cities = {}

cities["tokyo"] = {"country": "Japan",
        "population": 37_400_000,
        "fact": "Home to the world's busiest pedestrian crossing at Shibuya"}
cities["paris"] = {"country": "France",
        "population": 11_020_000,
        "fact": "The Eiffel Tower was initially meant to be temporary"}
cities["new york"] = {"country": "United States",
        "population": 18_800_000,
        "fact": "Times Square was originally called Longacre Square"}
for city, info in cities.items():
    print(f"City: {city.title()} Country: {info['country']} Population: {info['population']:,} Fact: {info['fact']}", end=" ")