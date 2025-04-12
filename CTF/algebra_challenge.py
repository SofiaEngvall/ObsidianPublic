from Crypto.Util.number import getPrime
from Crypto.Random import random

degree = 3  # You should start with trying to solve degree 1 and 2 locally, to understand the problem better
nbits = 128
secret_p, secret_q = getPrime(nbits), getPrime(nbits)
secret_n = secret_p*secret_q
secret_cs = [random.randrange(secret_n) for _ in range(degree)]
secret_d = random.randrange(secret_n)

def oracle(m: int) -> int:
	if not (1 < m < 2**(nbits-1)):
		print("no trivial solutions")
		exit()

	s = pow(m, secret_d, secret_n)  # This makes things difficult doesn't it ;)
	out = pow(s, degree, secret_n)
	for i in range(degree):
		out += secret_cs[i]*pow(s, i, secret_n)
	return out % secret_n

def main():
	while True:
		print("\nOptions:")
		print("1. Query oracle")
		print("2. Get flag")
		print("3. Quit")
		choice = input("Please choose an option: ")

		if choice == "1":
			m = int(input("Oracle input: "))
			print("Oracle output:", oracle(m))

		elif choice == "2":
			guess = int(input("Give me modulus: "))
			if guess != secret_n:
				print("Wrong!")
				break
			print("Your efforts have been rewarded:", open("flag.txt").read())
			break

		elif choice == "3":
			print("Goodbye!")
			break

		else:
			print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
	main()
