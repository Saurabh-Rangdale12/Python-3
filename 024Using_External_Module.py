import random   # importing random module :)

random_number = random.randint(0, 5)
print(random_number)  # gives any random number from 0 to 5 both included

rand = random.random() * 100  # random no. from 0 to 100
print(rand)

lst = ["Star", "DD1", "Aaj Tak", "India TV"]
choic = random.choice(lst)  # Gives random choice from the list
print(choic)