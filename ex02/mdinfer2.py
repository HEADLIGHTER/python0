def is_m(s_img: str) -> bool:
	exp_str = "*000*\n**0**\n*0*0*\n"
	if s_img == exp_str:
		return True
	else:
		return False


def is2dimg(img) -> bool:
	img_len = len(img)
	if img_len != 3:
		return False
	for i in range(img_len):
		if len(img[i].replace('\n', '')) != 5:
			return False
	return True


def to_zero(img, img_ln) -> list:
	for i in range(img_ln):
		for j in range(len(img[i])):
			if img[i][j] != '*' and img[i][j] != '0' and img[i][j] != '\n':
				img[i] = img[i].replace(img[i][j], '0')
	return img


def main1337():
	import sys

	try:
		with open(sys.argv[1]) as f:
			img = f.readlines()
		f.close()
	except IOError:
		print('File error!')
		return

	img_ln = len(img)
	img[img_ln - 1] += '\n'

	for i in range(img_ln):
		if len(img[i]) != 6 and i < 3:
			print("Error! Expected 3 lines with 5 characters per line!")
			return
		elif len(img[i]) > 0 and i >= 3:
			print("Error! Expected 3 lines with 5 characters per line!")

	if is2dimg(img):
		img = to_zero(img, img_ln)
		print(is_m(''.join(img)))
	else:
		print("Error! Expected 3 lines with 5 characters per line!")


if __name__ == "__main__":
	main1337()
