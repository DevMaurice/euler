# 	Multiples of 3 and 5
multiples = [j for j in range(1000) if j % 5 == 0 or j % 3 == 0]
print(sum(multiples))
