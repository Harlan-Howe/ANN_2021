# source = [20, 15, 30, 28, 33, 32, 18, 26, 41, 37, 50, 29 ]
import random
source = []
for i in range(50):
    source.append(random.randint(0,100))

print (f"source: {source}")

L = [1]*len(source)

L[0] = 1

for i in range(1,len(L)):
    for j in range (0,i):
        if source[i] > source[i-1-j] and L[i-1-j]>=L[i]:
            L[i] = L[i-1-j] + 1
            # break

print(f"L: {L}")


for i in range(len(L)):
    print(f"{source[i]}\t{L[i]}")
longest = 0
longest_end = 0
for i in range(len(L)):
    if L[i] > longest:
        longest = L[i]
        longest_end = i

print(f"Longest: {longest}\nLongest_end: {longest_end}")

sequence = [longest_end]
for i in range(longest_end-1,-1,-1):
    if L[i] == L[sequence[-1]]-1 and source[i] < source[sequence[-1]]:
        sequence.append(i)

result = []
for i in sequence:
    result.insert(0,source[i])

print(f"result: {result}")