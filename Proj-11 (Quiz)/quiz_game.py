from quiz_db import ques_bank
from quiz_db import options
print("*********************************")
print("Welcome to quiz game")
score=0
def check_ans(guess,correct_ans):
    if guess==correct_ans:
        return True
    else:
        return False
for ques_num in range(len(ques_bank)):
    print("*********************************")
    print(ques_bank[ques_num]["text"])
    for i in options[ques_num]:
        print(i)
    guess=input("Choose ur ans [A/B/C/D]: ").upper()
    is_correct=check_ans(guess,ques_bank[ques_num]["ans"])
    if is_correct:
        print("Correct ans")
        score+=1
    else:
        print("Incorrect ans")
        print(f"Correct ans is {ques_bank[ques_num]['ans']}")
    print(f"Ur current score is {score}/{ques_num+1}")
print(f"U have given {score} correct ans")
print(f"Ur score is {(score/len(ques_bank))*100}%")

