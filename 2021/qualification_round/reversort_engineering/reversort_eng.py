import itertools

def calc_cost(dim, array):
	pos_start = 0
	cost = 0

	while pos_start < dim - 1:

		# Find min index in sub-array[start_index, end]
		mini = min(array[pos_start:])
		pos_mini = array.index(mini)
		
		# Update cost
		cost += pos_mini - pos_start + 1

		# Invert array [index start .. index_mini]
		array[pos_start : pos_mini + 1] = array[pos_start : pos_mini + 1][::-1]
		
		# Increment start index, repeat
		pos_start += 1

	return cost


def solve(N, C):
	print("N: "+str(N))
	print("C: "+ str(C))

	max_cost = (N * (N+1) / 2) - 1
	min_cost = N-1

	if C < min_cost or C > max_cost:
		return 'IMPOSSIBLE'
	else:
		# bruteforce: calc cost of all permutations
		perms = list(itertools.permutations(list(range(1,N+1)), N))
		
		for perm in perms:
			perm_cost = calc_cost(len(perm), list(perm))

			if perm_cost == C:
				return perm

		# in case it fails
		return 'IMPOSSIBILE'


def main():
	with open("input") as f:
		
		T = int(f.readline().split()[0])

		for t in range(1, T+1):
			
			numbers = [int(x) for x in f.readline().split()]

			dim = numbers[0]
			cost = numbers[1]

			sol = solve(dim, cost)

			print ("Case #{}: {}".format(t, sol))


if __name__ == "__main__":
	main()

	

