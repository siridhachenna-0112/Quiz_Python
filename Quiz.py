print("Welcome to my computer quiz!!")

playing=input("do you want to play?")

if playing.lower() != "yes":
    quit()

print("okay! Let's Play :)")
score=0

answer=input("what does CPU stand for?")
if answer.lower()=="central processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")

answer=input("What does GPU stand for?")
if answer.lower()=="graphics processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect!")

answer=input("what does RAM stand for?")
if answer.lower()=="random access memory":
    print("correct!")
    score+=1
else:
    print("incorrect!")

answer=input("what does PSU staand for?")
if answer.lower()=="power supply":
    print("correct!")
    score+=1
else:
    print("incorrect!")

print("You got "+ str(score) + " questions correct!")
print("You got "+ str((score / 4)*100)+ "%.")
