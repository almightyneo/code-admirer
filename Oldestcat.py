class Cat:

    species = 'mammal'

    def __init__(self, name, age):

        self.name = name

        self.age = age

# 1 Instantiate the Cat object with 3 cats

c1 = Cat('dosanaz',20)

c2 = Cat('sansa',10)

c3 = Cat('dtdc',5)

# 2 Create a function that finds the oldest cat

def oldest_cat(*args):

  a = [*args]

  return max(a)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print("The oldest cat is, {} years old".format(oldest_cat(c1.age,c2.age,c3.age)))
