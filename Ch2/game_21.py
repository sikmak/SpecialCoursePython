# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:40:03 2016

@author: Никита
"""
from numpy import random

numberOfPlayers = int(input("Введите колличество игроков:\n"))
cardSequences = []
cardSequence=[]
for i in range(numberOfPlayers):
    for j in range(21):
        cardSequence.append(random.randint(1,11))
    cardSequences.append(cardSequence)
score = [0 for i in range(numberOfPlayers)]
count = 0
players = [1 for i in range(numberOfPlayers)]
i = 0
j = -1
flag = True
numberWinner=-1
while count!=numberOfPlayers:
    if players[i]!=0:
        print("\nИгрок №"+str(i+1))
        j+=1
        print("Твой счёт:")
        print(score[i])
        answer = int(input("Если хотите взять ещё карту введите 1, прекратить 0:\n"))
        if answer==0:
            print("Вы спасовали. Ожидайте окончания для выяснения результата.")
            print("Твой счёт:")
            print(score[i])
            count+=1
            players[i]=0
        elif answer==1:
            score[i]+=cardSequences[i][j]
            if score[i]>21:
                print("Твой счёт:")
                print(score[i])
                print("Вы проиграли...")
                count+=1
                players[i]=0
            elif score[i]==21:
                print("Твой счёт:")
                print(score[i])
                print("Вы выиграли!!!")
                numberWinner=i+1
                flag = False
                break
            else:
                print("Твой счёт:")
                print(score[i])
    if i == len(players)-1:
        i=0
    else:
        i+=1
max=-1
numberWinners = []
if flag==False:
    print("\nПобедил игрок №"+str(numberWinner))
    print("\nЗаходите ещё:)")
else:
    for i in range(numberOfPlayers):
        if score[i]>max and score[i]<=21:
            max=score[i]
            numberWinner = i+1
    for i in range(numberOfPlayers):
        if score[i]==max and i+1!=numberWinner:
            numberWinners.append(i+1)
    numberWinners.append(numberWinner)
    print("\nПобедил игрок №"+str(numberWinners))
    print("\nЗаходите ещё:)")