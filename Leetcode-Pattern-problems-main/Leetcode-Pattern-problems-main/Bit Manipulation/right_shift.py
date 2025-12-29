a = 6
print("a-->",bin(a)[2:])
print("length of bits-->",a.bit_length())
right_shift = a>>1
print("right shift by 1 pos-->",bin(right_shift)[2:])

multiply_by_2 = a>>1
print("Multiply by 2-->",multiply_by_2)