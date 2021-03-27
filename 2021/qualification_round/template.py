def solve(dim, numbers):
	print('solving for dim: {} and numbers: {}'.format(dim,numbers))


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

	

