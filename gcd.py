# Uses python3
def gcd_best(a, b):
    if b==0:
        return a
    a1=a%b
    return gcd_best(b,a1)

a, b = list(map(int, input().split(' ')))
print(gcd_best(a, b))
