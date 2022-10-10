def mpower(b,n,m):
    if n == 0:
        return 1
    elif n%2 == 0:
        return mpower(b,n/2,m)**2 % m
    else:
        return (b*mpower(b,(n-1)/2,m))**2 % m

res = mpower(7,644,645)
res1 = mpower(3,2003,99)
res2 = mpower(123,1001,101)
res3 = mpower(11,644,100)
res4 = mpower(23,1,23)

print(res)
print(res1)
print(res2)
print(res3)
print(res4)