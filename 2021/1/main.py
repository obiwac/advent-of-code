f = [int(s) for s in open("input").readlines()]

# part 1

n = sum(f[i] > f[i - 1] for i in range(1, len(f)))

print(n)

# part 2

n = sum(sum(f[i - 2: i + 1]) < sum(f[i - 3: i]) for i in range(2, len(f) - 1))
print(list(zip(f, f[3:])))

print(n)