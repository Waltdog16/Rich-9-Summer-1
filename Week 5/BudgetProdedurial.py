funds = 250
Budgets = {}
expenses = {}

def AddBudget(name, amount):
    global funds
    if name in Budgets:
        raise ValueError
    if amount > funds: 
     raise ValueError("no can do you are too broke")
    Budgets[name] = amount
    funds -= amount 
    expenses[name] = 0
    return funds

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("item not in budget")
    expenses[name] += amount
    budgeted = Budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
   print("Budget          Budgeted    Spent   Remaining ")
print("----------------------------------------------")
for name in Budgets:
      budgeted = Budgets[name]
      spent = expenses[name]
      remainingBudget = budgeted - spent 
      print(f'name, budgeted, spent, remainingBudget')
      
    

print(funds)
print(Budgets)
print(expenses)
print(funds)

AddBudget("Books", 100)

Spend("Books", 50)


PrintBudget()