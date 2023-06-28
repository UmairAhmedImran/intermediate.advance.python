#import random
#a = random.random() # random number in range 0 to 1
#a = random.uniform(1, 100) # random number in range 1 to 100
#a = random.randint(1, 10) # random integer but include upper range
#a = random.randrange(1, 10) # random integer but not include upper range
#a = random.normalvariate(0, 1) # mean and standard deviation
#mylist = list("ABCDEFGH")
#a = random.choice(mylist) # select a random value from mylist
#a = random.sample(mylist, 4) # select random value as much statted in 2nd argument
#a = random.choices(mylist, k=3) # can choice same alphabet twice
#random.shuffle(mylist) # shuffle the actual list
#print(mylist)

#random.seed(1) # seed method keeping track of the numbers produce under this seed
#print(random.random())
#print(random.randint(1, 10))

#random.seed(2)
#print(random.random())
#print(random.randint(1, 10))

#random.seed(1)
#print(random.random())
#print(random.randint(1, 10))

#random.seed(2)
#print(random.random())
#print(random.randint(1, 10))