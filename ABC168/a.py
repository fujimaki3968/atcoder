N = str(input())

i = int(N[-1])

if i in [2,4,5,7,9]:
    print("hon")
elif i in [0, 1,6,8]:
    print("pon")
else:
    print("bon")