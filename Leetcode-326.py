n = int(input())
mantiq = False
while(n/3):
    if n == 3 or n ==1:
        mantiq = True
        break
    n /= 3
    if n<3:
        break
print(mantiq)