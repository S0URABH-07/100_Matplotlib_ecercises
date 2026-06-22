# Stem plot chart and change line format or marker color
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [2,2,3,5,4,3]

plt.stem(x,y , linefmt=":", markerfmt="r")
plt.show()