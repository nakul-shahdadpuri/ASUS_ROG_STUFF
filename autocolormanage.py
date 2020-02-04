import cv2
import numpy
import os
import random


a = os.listdir('/home/nakul/Pictures/Wallpapers')
x = random.randrange(0,len(a))
image = a[x]

# myimg = cv2.imread('/home/nakul/Pictures/Wallpapers/'+image)
# avg_color_per_row = numpy.average(myimg, axis=0)
# avg_color = numpy.average(avg_color_per_row, axis=0)


cmd = 'gsettings set org.gnome.desktop.background picture-uri "/home/nakul/Pictures/Wallpapers/"' + image
os.system(cmd)

# red = avg_color[2]
# green = avg_color[1]
# blue = avg_color[0]
# output = 'white'
# if red > 100:
# 	output = 'red'
# if green > 100:
# 	output = 'green'
# if blue > 100:
# 	output = 'blue'
# if green > 100 and blue > 100:
# 	output = 'cyan'
# if red > 100 and green > 100:
# 	output = 'yellow'

color_list = [
'red',
'green',
'blue',
'yellow',
'cyan',
'magenta',
'white',
'black',
'rainbow']

y = random.randrange(0,len(color_list))
output = color_list[y]
comd = './rogauracore/rogauracore ' + output
os.system(comd)






