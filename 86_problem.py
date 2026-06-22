# Draw horizontal stem plot chart 
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [6,2,3,5,1,3]

plt.stem(x,y , linefmt=":", markerfmt="r" , bottom=4, basefmt="g", label="Stem plot" , orientation="horizontal")
plt.legend(loc=2)
plt.show()