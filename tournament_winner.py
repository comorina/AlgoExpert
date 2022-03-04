def tournament(competition, results):
    currentScore = ""    
    score = {currentScore:0}


    for indx, teambr in enumerate(competition):
        result = results[indx]
        hometeam, awayteam = teambr

        winnerteam = hometeam if result == 1 else awayteam
        print(winnerteam+"-")
        updateScore(winnerteam, 3, score)
        print(winnerteam)
        if score[winnerteam] > score[currentScore]:
            currentScore = winnerteam

    return currentScore


def updateScore(team, points, score):
    if team not in score:
        score[team] = 0
    
    score[team]+=points



if __name__ == '__main__':
    competition = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0,0,1]
    print(tournament(competition, results))