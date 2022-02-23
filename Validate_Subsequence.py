import sys
# Solution 1:-

# def isValidSubsequence(array, sequence):
#     validate={}
#     for i in sequence:
#         if i in array:
#             validate[i] = True
#         else:
#             validate[i] = False
    
#     for j in sequence:
#         if validate[j] == False:
#             return False
#     # print(validate)

#     return True

#Solution 2:-

# def isValidSubsequence(array, sequence):
#     # Write your code here.
# 	index = 0
	
# 	for i in array:
# 		if index == len(sequence):
# 			break
# 		if sequence[index] == i:
# 			index +=1
		
# 	return index == len(sequence)

#Solution 3:-

def isValidSubsequence(array, sequence):
    # Write your code here.
	index = 0
	
	for i in array:
		if index == len(sequence):
			break
		if sequence[index] == i:
			index +=1
		
	return index == len(sequence)

if __name__ == '__main__':


    for _ in range(int(input("Test case: "))):
        array = list(map(int,input().split()))
        sequence = list(map(int,input().split()))
        x= isValidSubsequence(array, sequence)
        print(x)