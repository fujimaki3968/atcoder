import math
from decimal import Decimal

A,B,H,M = map(int, input().split())

HD = (1/2) - ((H+(M/60))/6)
MD = (1/2) - (M/30)

Ax = A*math.cos(HD*math.pi)
Ay = A*math.sin(HD*math.pi)
Bx = B*math.cos(MD*math.pi)
By = B*math.sin(MD*math.pi)

ans = math.sqrt(((Bx - Ax)**2)+((By - Ay)**2))

print(ans)