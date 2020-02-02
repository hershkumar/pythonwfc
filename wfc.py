from PIL import Image, ImageColor
import numpy as np

N = 3
# read in the input
im = Image.open('Dungeon.png','r')
input_width, input_height = im.size

imagelist = list(im.getdata())


def rgb2hex(r,g,b):
	return "#{:02x}{:02x}{:02x}".format(r,g,b)

def hex2rgb(hexcode):
	return tuple(map(ord,hexcode[1:].decode('hex')))

def countElement(list, element):
	count = 0
	for i in range(len(list)):
		if (np.array_equal(element, list[i])):
			count += 1
	return count

def checkMembership(list, element):
	for i in range(len(list)):
		if (np.array_equal(list[i],element)):
			return True
	return False

def unique(list):
	uniques = []
	for i in range(len(patterns_with_duplicates)):
		if not (checkMembership(uniques, patterns_with_duplicates[i])):
			uniques.append(patterns_with_duplicates[i])
	return uniques

color = [0 for x in range(input_width * input_height)]
for i in range(input_width * input_height):
	color[i] = rgb2hex(imagelist[i][0],imagelist[i][1],imagelist[i][2])

color = np.reshape(color, (input_width,input_height))

patterns_with_duplicates = []

cellsheet_width = input_width * N + input_width + 1
cellsheet_height = input_height * N + input_height + 1

image = Image.new('RGB',(cellsheet_width, cellsheet_height))

for i in range(input_width+1):
	for j in range(cellsheet_height):
		image.putpixel((i,j),(0,0,0))

for i in range(input_width+1):
	for j in range(cellsheet_height):
		image.putpixel((i * (N + 1),j),(0,150,0))

for j in range(input_height+1):
	for i in range(cellsheet_width):
		image.putpixel((i,(N + 1) * j),(0,150,0))


for i in range(input_width):
	for j in range(input_height):
		pattern = [[0 for x in range(N)] for x in range(N)]
		for k in range(N):
			for l in range(N):
				pattern[k][l] = color[(i+k) % input_width][(j+l) % input_height]
				patterns_with_duplicates.append(pattern)

				ii = i + 1 + i * N + k
				jj = j + 1 + j * N + l
				image.putpixel((ii,jj),ImageColor.getrgb(pattern[k][l]))

image.save("dungeonWithDupes.png")

num_total = input_height * input_width

patterns = unique(patterns_with_duplicates)

num_patterns = len(patterns)



probability = [0 for x in range(num_patterns)]
for i in range(len(patterns)):
	current_pattern = patterns[i]
	prob = countElement(patterns_with_duplicates, current_pattern) / num_total
	probability[i] = prob

