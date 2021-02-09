hotels = [0, 195, 212, 370, 450, 530, 670, 700, 800, 920, 970, 1085, 1130, 1220, 1350, 1440, 1600]
P = [9E9] * len(hotels)
P[0] = 0
for i in range(1,len(hotels)):
    print(i)
    for j in range(0,i):
        print(f"\t{j}")
        penalty = (200-(hotels[i]-hotels[j]))**2
        if P[j]+penalty < P[i]:
            P[i] = P[j]+penalty
print (P)
x = len(hotels)-1
stops = [hotels[x]]
while x > 0:
    j=x-1
    while True:
        penalty = (200 - (hotels[x]-hotels[j]))**2
        if P[x]-penalty == P[j]:
            break
        j-=1

    stops.append(hotels[j])
    x=j
print (stops[::-1])