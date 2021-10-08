import math

i = open("input").read()

# part 1

f = sorted(map(int,i.split('\n')))

for j in reversed(range(len(f)-1)):
	f[j+1] -= f[j]

f.append(3)
print(f"part 1: {f.count(1) * f.count(3)}")

# part 2

s = "3"+"".join(map(str,f)).replace("3","33")+"3"
r = 2 ** s.count("3113") * 4 ** s.count("31113") * 7 ** s.count("311113")
#r = 2 ** len(s.replace("13", "").replace("3", ""))

print(f"part 2: {r}")

# part 1 golfed

r=sum(map(lambda x:x.count(1)*x.count(3),[[1,*map(lambda f:f[1][f[0]+1]-f[1][f[0]],enumerate(i.count('\n')*[sorted(map(int,i.split('\n')))])),3]]))
print(f"part 1: {r}")

# part 2 golfed

r=sum(map(lambda s:2**s.count("11")*4**s.count("111")*7**s.count("1111"),["".join(map(str,[1,*map(lambda f:f[1][f[0]+1]-f[1][f[0]],enumerate(i.count('\n')*[sorted(map(int,i.split('\n')))])),3])).split("3")]))
print(f"part 2: {r}")