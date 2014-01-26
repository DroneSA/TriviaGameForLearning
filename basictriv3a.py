from random import shuffle

###Opens two question banks, enabling you to have multi-genre support
with open("questions1.txt") as questionBank1:
    lines1 = questionBank1.readlines()

with open("questions2.txt") as questionBank2:
    lines2 = questionBank2.readlines()

shuffle(lines1)
shuffle(lines2)
numRight = 0
wrong = []

numQuestions = int(input("How many questions would you like to answer? "))
genre = input("Which question bank would you like: 1 or 2? ")

if genre == str(1):
    for line in lines1[:numQuestions]:
        question, rightAnswer = line.strip().split("\t")
        answer = input(question + " ")
        if answer.lower() == rightAnswer.lower():
            print("Right!")
            numRight += 1
        else:
            print("Wrong! The answer is", rightAnswer)
            wrong.append(question)
if genre == str(2):
    for line in lines2[:numQuestions]:
        question, rightAnswer = line.strip().split("\t")
        answer = input(question + " ")
        if answer.lower() == rightAnswer.lower():
            print("Right!")
            numRight += 1
        else:
            print("Wrong! The answer is", rightAnswer)
            wrong.append(question)

print("You got %d right!" % (numRight))
if (wrong):
    print("You got these wrong: ")
    for q in wrong:
        print(q)
