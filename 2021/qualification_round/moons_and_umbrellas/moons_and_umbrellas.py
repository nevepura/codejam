def solve(cost_cj, cost_jc ,mural):
	#print('cost_cj: {} cost_jc: {}, mural: {}'.format(cost_cj, cost_jc, mural))

	mural = cleaner(mural)
	#print('mural: {}'.format(mural))

	count_cj = mural.count("CJ")
	#print('count_cj: {}'.format(count_cj))

	count_jc = mural.count("JC")
	#print('count_jc: {}'.format(count_jc))

	cost = count_cj * cost_cj + count_jc * cost_jc
	#print('cost: {}'.format(cost))

	return cost



def cleaner(mural):
	mural = list(mural)

	outlist = []

	for ch in mural:
		if ch not in  ('?', '\n'):
			outlist.append(ch)

	# return (outlist)
	out = ''.join(outlist)
	return out


def main():
	with open("input") as f:
		
		T = int(f.readline().split()[0])
		
		for t in range(1, T + 1):
			
			line = [x for x in f.readline().split(" ")]
			x = int(line[0])
			y = int(line[1])
			mural = line[2]

			sol = solve(x, y, mural)
			print ("Case #{}: {}".format(t, sol))
		

if __name__ == "__main__":
	main()

	

