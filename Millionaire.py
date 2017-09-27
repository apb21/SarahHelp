#! /usr/bin/python
# -*- coding: UTF-8 -*-

#above I have defined the path to the python binary (in linux anyway, this will probably be different in windows) and the encoding used in this file. It was required to declare encoding in order to be able to print £ signs.

#the following code defines the ending process for the game. As this is always the same it is defined seperately to avoid repetition later on.
def ending(prizeMoney):
    #by passing the amount won to this bit of code as "prizeMoney" it prints out the final amount one before quitting the game.
    print("You win £"+str(prizeMoney)+" \n Thank you for playing!")
    quit()


def main():
    #this is the main part of the code in this file. it contains everything to run the game.
    #first I defined the data and other static variables all at the beginning to make tweaking the game easier if you need to.
    #The questionList is split over several lines to make it easier for a human to read, but there is no need to do this for it to still work.
    #questions sit in tuples seperate by comas. The format is ("question" \n "possible answers" \n, correct answer) where \n is a printed line break.
    questionList = [
    ("What is the Capital of England? \n A:Spain, B:Mexico, C:Paris, D:London? \n", "D"),
    ("How long is 5cm? \n A:9 miles, B:1 inch, C:5 cm, D:2 Light Years? \n ", "C"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A"),
    ("This questions answer is... \n A:A, B:A, C:A, D:A? \n ", "A")]
    #the answerList contains the possible answers that someone may input. Any other answer will be rejected as incorrectly answering the question. This deals with any inputs that are not A, B, C, or D.
    answerList = {"A":True,"B":True,"C":True,"D":True} #any other answer will be rejected as not valid.
    #The prizelist contains the list of prizes for answering each question correctly in order of the question being asked.
    prizeList = (100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000)
    #The minPrizes contains the list of the minimum amounts you win if you answer a question incorrectly in order of the question being asked.
    minPrizes = (0,0,0,0,1000,1000,1000,1000,1000,32000,32000,32000,32000,32000,32000)
    #The inital question number is 0 as arrays are 0 indexed (they start at 0 not 1)
    questionNumber = 0
    #You initially start with zero money...
    currentMoney = 0
    #and the initial minimum amount you can win is 0
    minPrize = 0
    #print a little welcome to start the game.
    print("Welcome to Who Wants to be a Millionaire?!")
    #while there are still questions in the question list that have not been answered.
    while (questionNumber)<len(questionList):
        #pick the next question from the question list
        thisQuestion = questionList[questionNumber][0]
        #get the answer from the contestant
        thisAnswer = raw_input(thisQuestion).upper() #upper() coverts lower case answers to upper case so it matches answerList.
        #try to make sure that the answer give is one of the valid answers, otherwise discount it.
        try:
            validAnswer = answerList[thisAnswer]
        except:
            validAnswer = False
            pass
        #if they have given a valid answer...
        if validAnswer:
            #...is it the right answer?
            if thisAnswer == questionList[questionNumber][1]:
                #if so, congratulate them...
                print(" Well Done. "+thisAnswer+" is the right answer")
                #...increase their prize money...
                currentMoney = prizeList[questionNumber]
                minPrize = minPrizes[questionNumber]
                #... and move on to the next question
                questionNumber+=1
            else:
                #if they did not give the right answer, commiserate them and end the game with their current minimum prize.
                print("Unfortunately, you got it wrong")
                print("You don't get £"+str(prizeList[questionNumber]))
                ending(minPrize)
        else:
            #if the did not give a valid answer, commiserate them and end the game with their current minimum prize.
            print(thisAnswer+" is not a valid choice. You have failed this question.")
            ending(minPrize)

        #give the contestant the choice to carry on or quit
        if questionNumber+1<len(questionList):
            #ask for their choice
            stayOrGo = raw_input(" Would you like to continue and possibly win £"+str(prizeList[questionNumber])+" on the next question, or quit and receive £"+str(currentMoney)+"?\n If you get the next question wrong you will receive £"+str(minPrize)+"\n Continue? Y/N \n ").upper()
            #if they continue by entering "Y", pass to start the loop again at the next question
            if stayOrGo == "Y":
                pass
            #or if they quit by pressing "N", end the game with their current prize money
            elif stayOrGo == "N":
                ending(currentMoney)
            #any other response counts as they wish to continue
            else:
                print("I guess that means you would like to continue.")
                pass
        else:
            #if you have reached the end of the questions, end the game with their current prize money (which will be the maximum prize)
            ending(currentMoney)

#this line makes sure the main loop is called to start the game if this file is run directly. If this file is included in another file using "import" then it will not immediately start the game.
if __name__ == '__main__':
    main()
