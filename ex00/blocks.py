def main1337():
	import sys

	if len(sys.argv) != 2:
		print("Expected number of lines as one numeric argument")
		return
	if not sys.argv[1].isdigit():
		print("Expected number of lines as one numeric argument")
		return

	lines = int(sys.argv[1])

	for i in range(lines):
		line = input()
		if len(line) == 32 and line.startswith('00000') and line[5] != '0':
			print(line)


if __name__ == "__main__":
	main1337()
