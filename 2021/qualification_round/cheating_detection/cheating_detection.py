import collections
import operator

from sigma import inverse_sigmoid

def solve(f):
	P = int(f.readline().split()[0])
	
	Ss = []
	answers = []
	Qs = []

	# Calculate player skill (S)
	for i in range (1, 101):
		s = f.readline()

		# save answers
		currAnswers = list(map(int, list(s)[:-1]))
		answers.append(currAnswers)

		# Calc players skill (S)
		player_int = currAnswers.count(1) / 10000 
		#print("player int: {}".format(player_int))
		S = inverse_sigmoid(player_int)
		#print("player skill : {}".format(S))
		Ss.append(S)


	# Calc difficulty of answers (Q)
	# accumulate number of times each answer was answered correctly
	acc = [0] * 10000
	for currAnswers in answers:
		for i, ans in enumerate(currAnswers):
			acc[i] += ans


	#print("acc: {}".format(acc[:20]))
	# for each answer, calc num of correct guesses on all guesses (from 100 players)
	answers_percentages = list(map(lambda x: x/100, acc))
	#print("answers_percentages: {}".format(answers_percentages[:20]))

	# calc Q
	Qs = list(map(inverse_sigmoid, answers_percentages))

	#print("skills (Ss): {}".format(Ss))
	#print("difficulties (qs): {}".format(Qs))
	qs_dict = {x:Qs.count(x) for x in Qs}
	
	print("difficulties map: {}".format(qs_dict ))
	od = collections.OrderedDict(sorted(qs_dict.items()))
	print(od)
		
	return 1


def main():
	with open("input") as f:
		
		T = int(f.readline().split()[0])
		
		for t in range(1, T+1):

			# probability of guessing the correct answer

			cheater = solve(f)
			print ("Case #{}: {}".format(t, cheater))
		

if __name__ == "__main__":
	main()
