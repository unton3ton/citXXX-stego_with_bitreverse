from PIL import Image
from math import sqrt
from functools import reduce
import operator

h1 = Image.open("img/1.jpg").histogram()
h2 = Image.open("img/1.png").histogram()
# h3 = Image.open("img/new.png").histogram()
h3 = Image.open("img/result.png").histogram()

rms = sqrt(reduce(operator.add,	map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
print("1.jpg - 1.png = ", rms)

rms1 = sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h3))/len(h1))
print("1.jpg - new (result).png = ", rms1)