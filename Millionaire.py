#!/usr/bin/python
# -*- coding: UTF-8 -*-

def main():
    questionList = [("What is the Capital of England? \n A:Spain, B:Mexico, C:Paris, D:London? \n", "D"), ("How long is 5cm? \n A:9 miles, B:1 inch, C:5 cm, D:2 Light Years? \n ", "C")]
    answerList = {"A":True,"B":True,"C":True,"D":True} #any other answer will be rejected as not valid.
    prizeList = (100,200,300,500,1000,2000,4000,8000,16000,32000,64000,125000,250000,500000,1000000)
    minPrizes = (0,0,0,0,1000,1000,1000,1000,1000,32000,32000,32000,32000,32000,32000)
    questionNumber = 0
    currentMoney = 0
    minPrize = 0
    while (questionNumber)<len(questionList):
        thisQuestion = questionList[questionNumber][0]
        thisAnswer = raw_input(thisQuestion).upper() #upper() coverts lower case to upper case so it matches answerList.
        try:
            validAnswer = answerList[thisAnswer]
        except:
            validAnswer = False
            pass
        if validAnswer:
            if thisAnswer == questionList[questionNumber][1]:
                print("Well Done. "+thisAnswer+" is the right answer")
                currentMoney = prizeList[questionNumber]
                minPrize = minPrizes[questionNumber]
                print("You now have £"+str(currentMoney))
                questionNumber+=1
                #handle carry on or quit
                stayOrGo = raw_input("Would you to continue, or quit and receive £"+str(minPrize)+"?\n Continue? Y/N").upper()
                if stayOrGo == "Y":
                    pass
                elif stayOrGo == "N":
                    print("You win £"+str(minPrize))
                    quit()
                else:
                    print("I think that means you would like to continue.")
                    pass
            else:
                print("You got it wrong. Try Again!")
                #handle error
        else:
            print(thisAnswer+" is not a valid answer. Try Again!")

if __name__ == '__main__':
    main()
