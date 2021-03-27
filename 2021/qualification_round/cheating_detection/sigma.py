import math

def sigmoid(x):
	return 1 / (1 + math.exp(-x))

def inverse_sigmoid(y):
	#print("exec log of {}".format(y))
	return round(math.log(y / (1 - y)), 3)


def main():
	n = float(input("calc sigmoid of n: "))

	sigm  = sigmoid(n)
	print("sigmoid of n: {}".format(sigm))

	S = inverse_sigmoid(sigm)
	print(S)
		



if __name__ == "__main__":
	main()
