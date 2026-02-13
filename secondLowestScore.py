if __name__ == '__main__':
    completeList = []
    scoreList = []
    
    N = int(input())
    
    if ((N<2) or (N>5)):
        raise ValueError("N must be between 2 and 5.")
        
    for _ in range(N):
        name = input()
        score = float(input())
        scoreList.append(score)
        
        perStudentScore = [name,score]
        completeList.append(perStudentScore)
    
    sorted_completeList = sorted(completeList)
    sorted_scoreList = sorted(scoreList)
    secondLowestScore = sorted(list(set(sorted_scoreList)))[1]
    finalList=[]
    for i in range(len(sorted_completeList)):
        if sorted_completeList[i][1] == secondLowestScore:
            finalList.append(sorted_completeList[i][0])
    
    for name in finalList:
        print(name)
