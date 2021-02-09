def candies():
    P = [0, 2, 7, 8, 13, 16, 18, 20, 22, 27, 28]
    R = [0] * 11
    S = [0] * 11
    for i in range (1,11):
        for j in range(0,i):
            print(f"{i}\t{j}")
            r = R[j] + P[i-j]
            if r > R[i]:
                R[i] = r
                S[i] = j
    print(f"P\t{P}\nR\t{R}\nS\t{S}")


if __name__ == '__main__':
    candies()