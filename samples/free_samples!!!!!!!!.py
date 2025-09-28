from world import Bag, User, candy

print("candy free samples!!!!!!!!!")

user = User()
bag = Bag(type=["nice", "huge"])
for i in range(500000):
    bag.insert(candy)

print("here u go :)")
user.give(bag)
