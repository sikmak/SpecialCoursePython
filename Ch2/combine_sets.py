# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:30:41 2016

@author: Никита
"""
import numpy as np

def decks():
    suit=["C",'D','H','S']
    number=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    deck=[]
    for i in range(4):
        for j in range(13):
            deckString=[]
            c=suit[i]+str(number[j])
            deckString.append(c)
            deck.append(deckString)
    print("Колода карт:")
    print(deck)
    
def number():
    figures=range(10)
    letters=['A','B','C','E','K','H','M','O','P','T','X']
    number=''
    for i in range(4):
        number+=str(np.random.choice(figures))
    for i in range(2):
        number+=str(np.random.choice(letters))
    print("Регистрационный номер:")
    print(number)
 
def dice():
    dice1=range(7)
    dice2=range(7)
    combinations=[]
    first=0
    second=0
    counter=0
    for i in dice1:  
        first=dice1[i]
        for j in dice2:
            combinationArr=[]
            second = dice2[j]
            if(first+second==7):
                counter+=1
            combinationArr.append(first)
            combinationArr.append(second)
            combinations.append(combinationArr)
    print("Все комбинации")
    print(combinations)
    print("Счётчик")
    print(counter)

decks()
number()
dice()