from perlin_noise import *
from texture_gen import *

from texture_gen import Gradient

# Generates a simple cloud texture from perlin_noise
def generate_sample_textures():
	w = h = 1024
	octaves = 7

	# generate cloud texture
	gradient = Gradient((1, 1, 1, 1), ((135.0/255.0), (206.0/255.0), (250.0/255.0), 1))
	p_noise = perlin_noise_2d(w, h, octaves, .25)
	color_grid = map_gradient(gradient, p_noise)
	generate_texture(color_grid, 'cloud_texture.png')

	# generate wood texture
	# gradient = Gradient((.62, .32, .17, 1), (.38, .13, .07, 1))
	# p_noise = wood_texture(512, 512, 9)
	# color_grid = map_gradient(gradient, p_noise)
	# generate_texture(color_grid, gradient)


# writes perlin noise values to a text file. Each value is delimited by
# a ' ' character and each row is delimited by a '\n' character
def write_perlin_to_file(perlin, width, height):
	f = open('perlin.txt', 'w')
	for i in range(width):
		for j in range(height):
			if(j == height - 1):
				f.write(str(perlin[i][j]))
			else:
				f.write(str(perlin[i][j]) + ' ')
		f.write('\n')

	f.close()

def make_snowy_ground():
	grass = Image.open('textures/grass.png', 'r')
	print 'generating perlin noise...'
	p_noise = perlin_noise_2d(512, 512, 6, .25)
	print 'blending textures'
	blend_textures(grass, p_noise, 512, 512)

# Simple prompt which gives user the option to generate sample perlin noise texture
# or generate a text file with perlin noies values.
def prompt():
	print("please choose an option")
	print("\t1 - Generate sample texture")
	print("\t2 - Output perlin values to text file")
	print("\t3 - Blend grass and snow texture")

	selected = input('>')
	if (selected == 1):
		print("Generating texture, please wait...")
		generate_sample_textures()
	elif(selected == 2):
		width = input("specify width: ")
		height = input("specify height: ")
		persistence = input("specify persistence: ")
		print("Generting perlin noise values please wait")
		p_noise = perlin_noise_2d(width, height, 9, persistence)
		write_perlin_to_file(p_noise, width, height)
	elif(selected == 3):
		make_snowy_ground()
	else:
		prompt()

	print("Done")

prompt()
