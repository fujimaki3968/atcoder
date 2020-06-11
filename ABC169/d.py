N = int(input())

def factorization(n):
    ans = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if  temp%i == 0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            ans.append([i, cnt])

    if temp != 1:
        ans.append([temp, 1])

    if ans == []:
        ans.append([n, 1])

    return ans

print(factorization(N))