# Stem plot chart and change bottom
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [6,2,3,5,1,3]

plt.stem(x,y , linefmt=":", markerfmt="r" , bottom=4)
plt.show()