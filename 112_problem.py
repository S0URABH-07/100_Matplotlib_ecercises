# Stem plot chart and change base clr or add label
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [6,2,3,5,1,3]

plt.stem(x,y , linefmt=":", markerfmt="r" , bottom=4, basefmt="g", label="Stem plot")
plt.legend(loc=2)

plt.savefig("Stemplot",facecolor="r")
plt.show()