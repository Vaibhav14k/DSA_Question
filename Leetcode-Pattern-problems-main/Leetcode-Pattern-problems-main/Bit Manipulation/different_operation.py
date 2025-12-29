def set_bit(n, pos):
    return n | (1<<pos)

def clear_bit(n,pos):
    return n & ~(1<<pos)

def toggle_bit(n,pos):
    return n ^ (1<<pos)

def check_bit(n,pos):
    return (n & (1<<pos)) != 0

n = 9
print("n-->",bin(n)[2:])
print("set_bit(n, 2)-->",bin(set_bit(n, 2))[2:])
print("n-->",bin(n)[2:])
print("clear_bit(n, 0)-->",bin(clear_bit(n, 0))[2:])
print("n-->",bin(n)[2:])
print("toggle_bit(n, 1)-->",bin(toggle_bit(n, 1))[2:])
print("n-->",bin(n)[2:])
print("check_bit(n, 2)-->",check_bit(n, 2))
