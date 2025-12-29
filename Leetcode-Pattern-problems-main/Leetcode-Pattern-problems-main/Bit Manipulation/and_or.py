
a = 5
b = 3
print(bin(a))
print(bin(b))

print(a&b)
print(bin(a&b))

print("<"+"--"*30+">")
# To check number is odd or not
def is_odd(a):
    return (a & 1) == 1

print(bin(a)[2:])
print(is_odd(a))

print("<"+"--"*30+">")
print(a | b)