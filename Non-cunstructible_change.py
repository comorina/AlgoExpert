import sys 
import datetime

def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    if len(coins)== 0:
    	return 1
    for coin in coins:
    	if coin > change+1:
    		return change+1
    	change+=coin
    return change+1


if __name__ == '__main__':
	x = datetime.datetime.now()
	sys.stdin = open("input.txt", "r")
	sys.stdout = open("output.txt","w")

	coins = list(map(int, input().split()))
	minChange =nonConstructibleChange(coins)
	print(minChange)
	print("Date and Time " + "->",x)