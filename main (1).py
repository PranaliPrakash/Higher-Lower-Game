

import random
from game_data import data
from replit import clear
from art import  logo ,vs
print(logo)

def check_answer(guess,a_followers,b_followers):
  ''' It takes guess (userinput) and checks whether the
      user answer is correct or wrong.'''
  
  if a_followers>b_followers:
    return guess=="a"
  else:
    return guess=="b"  


num1= random.randint(0,len(data)-1)
dictA=(data[num1])


condition=True
score=0
while condition==True:
  num2=random.randint(0,len(data)-1)
  while num1==num2:
    num2=random.randint(0,len(data)-1)

  dictB=(data[num2])
  a_followers=dictA['follower_count']
  b_followers= dictB['follower_count']
  
  print(f"Compare A : {dictA['name']} , a {dictA['description']}, from {dictA['country']}")
  print(vs)
  print(f"Against B : {dictB['name']} , a {dictB['description']}, from {dictB['country']}")    

  guess=input("Who has more followers? Type 'a' or 'b':")

  answer= check_answer(guess,a_followers,b_followers)
  if answer==True:
    score+=1
    clear()
    print(logo)
    print(f"You are right current_score is {score}")
  else:
    clear()
    print(logo)
    print(f"You are wrong Final_score is {score}") 
    condition=False 
  
  num1=num2
  dictA= data[num1]
  







