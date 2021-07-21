# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name=name1+name2
tRUE=name.count('t')+name.count('r')+name.count('u')+name.count('e') 

lOVE=name.count('l')+name.count('o')+name.count('v')+name.count('e') 
LOVE=str(lOVE)
TRUE=str(tRUE)
trueLove=TRUE+LOVE
print(trueLove)
score=int(trueLove)
if score < 10 or score > 90:
  print("you are alright together")
elif score > 40 and score < 50:
  print("you go together like coke and mentos")
