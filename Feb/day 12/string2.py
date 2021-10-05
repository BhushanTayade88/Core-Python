l1 = ["M","na","i","Em"]
l2 = ["y","me","s","ma"]


l3=[l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3]]
print(l3)

l4=[l1[x]+l2[x] for x in range(len(l1))]
print(l4)