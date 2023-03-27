def main1337():
	import sys
	if len(sys.argv) != 2:
		print("Expected string as single quoted sentence")
		return

	sys.argv[1] = sys.argv[1].strip().replace('\n', ' ').replace('\t', ' ')
	message = sys.argv[1].split()

	for i in message:
		if i[0].isalpha():
			print(i[0], end='')
	print()


if __name__ == "__main__":
	main1337()
