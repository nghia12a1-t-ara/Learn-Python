                        # BOWLING GAME #

#------------- Define Functions to Calculate Score ------------#
'''------------------- isStrike Function --------------------***
*** @brief: Function to check if a frame is Strike
*** @param: myFrame is a list type, contain knocked pin of a frame
*** @reval: True/False
'''
def isStrike(myFrame):
    if int(myFrame[0]) == 10:
        return True
    return False

'''-------------------- isSpare Function --------------------***
*** @brief: Function to check if a frame is Spare
*** @param: myFrame is a list type, contain knocked pin of a frame
*** @reval: True/False
'''
def isSpare(myFrame):
    if len(myFrame) == 2:
        if (int(myFrame[0]) + int(myFrame[1]) == 10):
            return True
    return False

'''------------------- frameScore Function ------------------***
*** @brief: Calculate Score of myFrame
*** @param: myFrame is a list type, contain knocked pin of a frame
*** @reval: (integer) Score of myFrame
'''
def frameScore(frame, index):
    score = 0
    myFrame = frame[index]
    #--- Basic Score of myFrame ---#
    for i in range(len(myFrame)):
        score += int(myFrame[i]) 

    #--- If myFrame is Strike ---#
    if isStrike(myFrame) == True:
        nextFrame = frame[index+1]
        #--- nextFrame is Strike ---#
        if isStrike(nextFrame) == True:
            score += 10
            next2Frame = frame[index+2]
            if isStrike(next2Frame) == True:
                score += 10
            else:
                score += int(next2Frame[0])
        else:
            for i in range(len(nextFrame)):
                score += int(nextFrame[i])
                
    #--- If myFrame is Spare ---#
    elif isSpare(myFrame) == True:
        nextFrame = frame[index+1]
        score += int(nextFrame[0])
        
    return score

'''------------------ Total_Score Function -----------------***
*** @brief: Calculate total score of bowling game
*** @param: frame is a list type, contain knocked pin of a frame
*** @reval: (integer) total score of frames
'''
def Total_Score(frame):
    totalScore = 0
    for myTurn in range(10):
        totalScore += frameScore(frame, myTurn)
    return totalScore

#------------------ Get Input Data from keyboard ----------------#
FRAME = []
bonus_index = 10

for myTurn in range(10):
    FRAME.append([])
    inputData1 = input("Frame %d:\n\tTurn 1: " % (myTurn + 1))
    FRAME[myTurn].append(inputData1)
    if int(inputData1) == 10:
        print("\tStrike!!!")
    elif 0 <= int(inputData1) < 10:
        inputData2 = input("\tTurn 2: ")
        FRAME[myTurn].append(inputData2)
    
    '''----- If Turn 10 is Strike or Spare -----'''
    if myTurn == 9:
        FRAME.append([])
        if isStrike(FRAME[myTurn]) == True:
            bonus1 = input("\tStrike!!!\n\tBonus 1: ")
            bonus2 = input("\tBonus 2: ")
            FRAME[bonus_index].append(bonus1)
            if bonus1 == 10:
                FRAME.append([])
                FRAME[bonus_index + 1].append(bonus2)
            else:
                FRAME[bonus_index].append(bonus2)
        elif isSpare(FRAME[myTurn]) == True:
            bonus = input("\tSpare!!!\n\tBonus: ")
            FRAME[bonus_index].append(bonus)

#-------------------- Calculate & Print Score -----------------#

TOTAL_SCORE = Total_Score(FRAME)
print("Total score of bowling game = %d" % TOTAL_SCORE)

#------------------------------ END ---------------------------#
