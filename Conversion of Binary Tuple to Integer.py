tup = (1,1,0,1,0,1)
print("The original tuple is : " + str(tup))
res = int("".join(str(ele) for ele in tup), 2)
print("Decimal number is : " + str(res))
