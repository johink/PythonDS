"""OBJECT-ORIENTED PROGRAMMING"""
#Define the class
class BankAccount(object):
    #Define the constructor.  "self" is a reference to the current instance.
    def __init__(self, acctno, bal):
        self.AccountNumber = acctno
        self.Balance = bal
    
    #Define instance methods.  Since these operate on instances, they must have the "self" parameter.
    def MakeDeposit(self, amt):
        self.Balance += amt
        return self.Balance
    
    def MakeWithdrawal(self, amt):
        if amt <= self.Balance:
            self.Balance -= amt
        else:
            raise Exception("Your balance is less than ${}.".format(amt))
        return self.Balance
        
    def __str__(self):
      return "Account {} has a balance of ${}".format(self.AccountNumber, self.Balance)

#%%
my_acct = BankAccount(5124125, 200)
your_acct = BankAccount(2234134, 5000)
accounts = [my_acct, your_acct]

for account in accounts:
    print("Account {} has a balance of ${}".format(account.AccountNumber, account.Balance))
    
#%%
#Be careful, this does not make a copy of my_acct, rather temp points to the same BankAccount as my_acct:
temp = my_acct
temp.MakeWithdrawal(100)

print(my_acct.Balance)

#%%
#Define __str__ function and all you have to do is this
for account in accounts:
  print(account)
  
  
#%%
#Now let's implement our own classes!
class Dog(object):
    def fetch(self, toy):
        self.Happiness += len(toy)
        print("Dog {} fetched the {}.".format(self.Name, toy))
        
    def __init__(self, name, happiness, cuteness, breed):
        self.Name = name
        self.Happiness = happiness
        self.Cuteness = cuteness
        self.Breed = breed
    
    def bark(self):
        print("Bark!")
        
    def __str__(self):
        return "{}: {} / {}".format(self.Name, self.Happiness, self.Cuteness)
        
    def __sort__(dog1, dog2):
        if dog1.Cuteness > dog2.Cuteness:
            1
        elif dog1.Cuteness < dog2.Cuteness:
            -1
        else:
            0
#%%
my_dog = Dog("Roger", 721, 644, "Shiba-Inu / Akita Mix")
your_dog = Dog("Spike", 333, 235, "Bulldog")
their_dog = Dog("Sandy",1000, 1000, "Goldador")
chase_dog = Dog("Hershey",235, 892, "Shih-Tzu / Poodle Mix")

list_of_dogs = [my_dog, your_dog, their_dog, chase_dog]

my_dog.bark()
my_dog.Happiness
my_dog.fetch("Rope Knot")
my_dog.Happiness

sorted(list_of_dogs)

print(my_dog)

#%%
class Vehicle(object):
    def __init__(self, num_doors, num_wheels, color, year):
        self.Doors = num_doors
        self.Wheels = num_wheels
        self.Color = color
        self.Year = year
    
    def score(self):
        return (18000 * .95 ** (2016 - self.Year) + 50 * self.Doors - (15 if self.Wheels < 4 else 0)) * (2 if self.Color == "blue" or self.Color == "orange" else 1)

#%%
my_vehicle = Vehicle(18, 2, "blue", 1999)
your_vehicle = Vehicle(4, 4, "orange", 2014)        
your_vehicle.score()
my_vehicle.score()        
#%%

class Truck(Vehicle):
    def __init__(self, num_doors, num_wheels, color, year, tow_capacity, engine_size):
        self.Tow_Cap = tow_capacity
        self.Engine_Size = engine_size
    
#%%
my_truck = Truck(3, 6, "grey", 2007, 12000, 6)
my_truck.score()
        
        