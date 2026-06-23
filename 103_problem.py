# SaveFigure 
# dpi -> dot per inch
import matplotlib.pyplot as plt 
x = [1,3,5,2,6]
y = [2,4,3,6,4]

plt.plot(x,y , color="r")
plt.savefig("Plotfigure")
# use dpi for better image quality
plt.show()