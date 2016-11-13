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










