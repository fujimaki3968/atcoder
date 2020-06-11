K = int(input())
S = input()

ans = ""
for index, char in enumerate(S):
    if index < K:
        ans += char
    else:
        ans += "..."
        break

print(ans)