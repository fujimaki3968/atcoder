from decimal import Decimal # 浮動小数点数のためのサムシング

a, b = input().split()
a = Decimal(a)
b = Decimal(b)
print(int(a*b))