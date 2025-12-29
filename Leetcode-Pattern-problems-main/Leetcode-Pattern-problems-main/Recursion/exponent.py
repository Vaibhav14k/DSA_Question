def exponent(a:int,b:int) -> int:
    if b == 0:
        return 1
    if b %2 == 0:
        return exponent(a*a,b//2)
    else:
        return a * exponent(a*a,b//2)



a = 3
b = 2
print(exponent(a,b)) 