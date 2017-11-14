#Este es un programa que calcula el umbral binario en un intervalo de 63 a 191 para negro
from scipy import misc
nameFile = input('Este programa requiere de su elección entre una "casa" o un "leon", escriba su elección ')
nameFile += '.jpg'

image = misc.imread(nameFile)
print(image.shape)
height, width, channel = image.shape

for row in range(height):
    for column in range(width):
        color = image[row, column][0]
        if color > 62 and color < 192:
            image[row, column] = [0,0,0]
        else:
            image[row, column] = [255,255,255]

misc.imsave('res'+nameFile, image)
print('Listo')
