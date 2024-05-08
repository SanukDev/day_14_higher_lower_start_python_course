from replit import clear
from art import logo, vs
from game_data import data
import random


def random_number():
    number_r = random.randint(0,len(data))
    return number_r
def ver_more_folowers(num):
    number_followers = data[num]['follower_count']
    return number_followers

def calc_score(your_choice,numb_followerA,numb_followerB):
    score = 0
    if numb_followerA > numb_followerB and your_choice == "a":
        score +=1
        return score
    elif numb_followerB > numb_followerA and your_choice == "b":
        score += 1
        return score
    else:
        return 0
def endGame(your_choice,numb_followerA,numb_followerB):
    if numb_followerA > numb_followerB and your_choice == "a":
        gamend = 1
        return gamend
    elif numb_followerB > numb_followerA and your_choice == "b":
        gamend = 1
        return gamend
    else:
        gamend = 0
        return gamend
print(logo)
score = 0
numA = random_number()
end_game = False
while end_game == False:
    clear()
    numB = random_number()
    if score > 0:
        print(f"You're right! Curent score: {score} ")
    print(f"Compare A: {data[numA]['name']}, a {data[numA]['description']}, from {data[numA]['country']}")
    print(vs)
    print(f"Compare B: {data[numB]['name']}, a {data[numB]['description']}, from {data[numB]['country']}")
    numb_followerA:int = ver_more_folowers(numA)
    numb_followerB:int = ver_more_folowers(numB)
    your_choice = input("Who has more followers? Type 'A' or 'B':").lower()
    score = score + calc_score(your_choice,numb_followerA,numb_followerB)
    game = endGame(your_choice,numb_followerA,numb_followerB)
    if game == 0:
        end_game = True
        print(f"Sorry that is wrong. Final score: {score}")
    numA = numB
