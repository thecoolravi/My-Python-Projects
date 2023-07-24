# create a program capable of displaying the questions to the users like KBC
#Use List data type to store the questions and their correct answers
# Author - Ravi Shankar
 
import os
from termcolor import colored


def greet(qlencount):
    os.system('cls')
    print(colored("\n<---------------------------------------------------------------------- Kaun Banega crorepati --------------------------------------------------------------------------------------->\n",'green'))
    name = input(f"\nHello May i know Your name Please: ")
    print(f"\nHello {name}, WELCOME TO KBC\t\t\t\tCreated by - MR. Ravi\n")
    matches = int(input(f"\nEnter The number of questions you would like to answer out of { qlencount } questions: "))
    return matches

def play(qnum,onum,correctOption):
    print(questions[qnum],"\n")
    print(options[onum],"\n")
    userans=int(input("Enter Your Option in NUMBER ONLY: "))
    global score
    if userans == correctOption:
        score += 10000
        print(f"\n\nLaa Jawab.... \nYou Won ₹{score}\n")
        enter = input("\n\n\tPress Enter for Next Question...")
        os.system('cls')
    else:
        score -= 5000
        print(f"\n\nGalat Jawab.... \nYou Have ₹{score}\n")
        print(f"\nThe Correct Answer was {answers[i]}\n")
        enter = input("\n\n\tPress Enter for Next Question...")
        os.system('cls')
    return score

questions = ["1) Who was the first prime minister of india?",
"2) What was First MCU movie?",
"3) Which programming language are we learning now ?",
"4) Who Discoverd gratity ?",
"5) what is the full form of lol ?",
"6) what is Bahubali festival is related to ?",
"7) Which of these sports requires you to shout out a word loudly during play?",
"8) Which of these countries is larger than India in territorial space?",
"9) September 27 is celebrated every year as?",
"10) Who among the following is one of the main characters of Ramayana who also appears in Mahabharata?",
"11) Veenapani is another name of which goddess?",
"12) Which of these diseases is also known as 'brain fever'?",
"13) According to astrology, how many zodiac signs are there in total?",
"14)  Which of the following can live without a head for a week or more?",
"15)  Nandyal is situated in?"]
qlencount = int(len(questions))

matches = greet(qlencount)
# global name 
score = 0
os.system('cls')


options = ["1) Jawaharlal Nehru\t\t 2) Indra Gandi\n3) Ravi shankar\t\t 4) Narendra modi",      
"1) Eternals\t\t 2) Avengers: Endgame\n3) Iron Man\t\t 4) Thor Love and thunder",
"1) English\t\t 2) Python\n3) Java\t\t 4) C++",
"1) Stephen Hawking \t\t 2) Galileo Galilei\n3) Albert Einstein\t\t 4) Sir Isaac Newton",
"1) Laugh out loud\t\t 2) Laughing Out Loud\n3) lots of love\t\t 4) Lots of Liars",
"1) Islam\t\t 2) Hinduism\n3) Buddhism\t\t 4) Jainism",
"1) Ludo\t\t 2) Kho-kho\n3) Playing cards\t\t 4) Chess",
"1) Australia\t\t 2) Argentina\n3) Kazakhstan\t\t 4) UAE",
"1) Teachers' Day\t\t 2) National Integration Day\n3) World Tourism Day\t\t 4) International Literacy Day",
"1) Hanuman\t\t 2) Vedavyasa\n3) Dasaratha\t\t 4) Duryodhana",
"1) Durga\t\t 2) Saraswati\n3) Sita\t\t 4) Lakshmi",
"1) Japanese encephalitis\t\t 2) Tetanus\n3) Dengue\t\t 4) Rabies",
"1) eight\t\t 2) ten\n3) twelve\t\t 4) fourteen",
"1) Spider\t\t 2) Cockroach\n3) Lizard\t\t 4) Caterpillar",
"1) Karnataka\t\t 2) AndhraPradesh\n3) Maharashtra\t\t 4) Madhya Pradesh"]

answers = [1,3,2,4,1,4,2,1,3,1,2,1,3,2,1]
for i in range(matches):
    score = play(i, i, answers[i])
    if score<=0:
        print(colored(f'''Oh No! you lost the game.... Work Harder


                                    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________ 
                            ______¶¶¶¶¶¶_____________¶¶¶¶¶¶________ 
                            _____¶¶¶¶¶_________________¶¶¶¶¶¶______ 
                            ____¶¶¶¶_____________________¶¶¶¶¶_____ 
                            ___¶¶¶¶_______________________¶¶¶¶¶____ 
                            __¶¶¶¶_____¶¶¶¶_______¶¶¶¶______¶¶¶____ 
                            __¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶___ 
                            _¶¶¶¶_____¶¶¶¶¶¶_____¶¶¶¶¶¶______¶¶¶___ 
                            _¶¶¶_______¶¶¶¶_______¶¶¶¶_______¶¶¶¶__ 
                            _¶¶¶______________________________¶¶¶__ 
                            _¶¶¶______________________________¶¶¶__ 
                            _¶¶¶______________________________¶¶¶__ 
                            _¶¶¶____________¶¶¶¶¶____________¶¶¶¶__ 
                            _¶¶¶¶________¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶___ 
                            __¶¶¶______¶¶¶¶¶_____¶¶¶¶¶______¶¶¶¶___ 
                            __¶¶¶¶____¶¶¶___________¶¶¶____¶¶¶¶____ 
                            ___¶¶¶¶___¶¶_____________¶¶___¶¶¶¶_____ 
                            ____¶¶¶¶____________________¶¶¶¶¶______ 
                            _____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______ 
                            _______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________

         ''','red'))
        break

print(colored(f'''\n\n\n\t\t\tTotally You Got ₹{score}.\n\n\n\t\t\t\t''','green'))