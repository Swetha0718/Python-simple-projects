import random 
import os
import game_art
import game_db
print(game_art.logo)
score=0
def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name} a {description} from {country}"
def check_ans(guess,followers_1,followers_2):
    if followers_1 < followers_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
account_2=random.choice(game_db.data)
continue_game=True
while continue_game:
    account_1=account_2
    account_2=random.choice(game_db.data)
    while account_1==account_2:
        account_2=random.choice(game_db.data)
    print(f"Compare 1: {display_accountinfo(account_1)}")
    print(game_art.vs)
    print(f"Compare 2: {display_accountinfo(account_2)}")
    guess=int(input("who has more followers? Type 1 or 2: "))
    followers_count_1=account_1['followers']
    followers_count_2=account_2['followers']
    is_correct=check_ans(guess,followers_count_1,followers_count_2)
    os.system("cls")
    print(game_art.logo)
    if is_correct:
        score+=1
        print(f"U are rigth..and ur score is {score}")
    else:
        print(f"U are wrong..and ur score is {score}")
        continue_game=False
    
    
