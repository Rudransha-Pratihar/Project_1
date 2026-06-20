import random
import time
from Dataset import Question_Set

def Quizz(count):
    for i in range(count):
        input("Press Enter for next question...")
        Comp_Question=int(random.randrange(len(Question_Set)))
        Start_time=time.time()
        print("Question",i+1)
        print(Question_Set[Comp_Question]["Question"])
        print("\n")
        print(Question_Set[Comp_Question]["Options"])
        user_pick=input("\n"+"Enter the letter of which option you want to answer: ")
        Stop_time=time.time()
        Time_taken=Stop_time-Start_time
        if str(user_pick)==Question_Set[Comp_Question]["Answer"]:
            print("\n"+"corret answer")
            print("you did it in",Time_taken)
        else:
            print("\n"+"incorrct answer")
Num = input("Enter the number of question you want to be asked: ")
if 1 <= int(Num) <= len(Question_Set):
    Quizz(int(Num))
else:
    print("The Number is invalid")
    print("please enter a value between 1 to ",len(Question_Set),)