a = 5
print("a-->",bin(a)[2:])
print("length of bits-->",a.bit_length())
left_shift = a<<2
print("Left shift by 1 pos-->",bin(left_shift)[2:])

multiply_by_2 = a<<1
print("Multiply by 2-->",multiply_by_2)