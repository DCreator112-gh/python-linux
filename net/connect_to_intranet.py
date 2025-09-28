import requests

try:
    very_good = requests.get("https://dcreator112.xyz")
    print(very_good)
    print("fing")
except NoIntranetError:
    print("oh yeah i was supposed to make this connect da user 2 zee intrenet")
    connnet_2_intrenat()
    very_good = requests.get("https://dcreator112.xyz")
    print(very_good)
    print("fing")