marks=[10,20,30,40,50,60,70,80,90,95]
############    SYNTAX---->fun_obj= lambda args : expression

def sqr(n):
    return n*n
print(sqr(4))    ###   equvalent to---->  sqr = lambda n:n*n

def inc(num):
    sqr=num*num
    final_num = sqr
    return final_num+1      ###  equvalent to---->  inc = lambda num:num+1

print(inc(11))
