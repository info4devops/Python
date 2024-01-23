# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

#Input Format: The first line contains . The second line contains an array   of  integers each separated by a space.

n = int(input())
arr = map(int, input().split())
sorted_scores = sorted(set(arr),reverse=True)
runner_up_score = sorted_scores[1]
print('The RUnner-Up Score:',runner_up_score)