def solve(dim, array):
	pos_start = 0
	cost = 0

	while pos_start < dim - 1:
		#print("pos_start: "  + str(pos_start))

		# Find min index in array[start_index, end]
		mini = min(array[pos_start:])
		pos_mini = array.index(mini)
		#print("pos_mini: " + str(pos_mini))
		
		# Update cost
		cost += pos_mini - pos_start + 1

		# Invert array [index start .. index_mini]
		array[pos_start : pos_mini + 1] = array[pos_start : pos_mini + 1][::-1]
		
		# Increment start index, repeat
		pos_start += 1

		#print(array)
	return cost


def main():
	with open("input") as f:
		
		T = int(f.readline().split()[0])

		for t in range(1, T+1):
			dim = int(f.readline())
			numbers = [int(x) for x in f.readline().split()]

			sol = solve(dim, numbers)
			print ("Case #{}: {}".format(t, sol))


if __name__ == "__main__":
	main()

	

