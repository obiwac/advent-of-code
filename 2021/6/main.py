f = open(0).read()

print(sum([(lambda r,*a:r(r,*a))(lambda r,d,f:r(r,d+1,[*map(lambda i:(f[i],f[i]+f[0],f[0])[1+(7,9).index(i)if i in(7,9)else 0],range(10))][1:]+[0])if d!=257else f,0,[[int(x)for x in map(str.strip,f.split(','))].count(k)for k in range(10)])[x]for x in range(8)]))