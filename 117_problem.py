# Subplots -> one Chart have 4 Diffrent plot's
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,3,4,5,6]
plt.subplot(2,2,1)
plt.plot(x,y,color="r")

x1 = [1,3,5,7]
y1 = [2,4,6,8]
plt.subplot(2,2,2)
plt.step(x1,y1)

z = [10,20,30,40]
lvl = ["Python","Java","C","C++"]
plt.subplot(2,2,3)
plt.pie(z,labels=lvl)

z1 = ["a","b","c","d"]
z2 = [10,20,40,30]
plt.subplot(2,2,4)
plt.bar(z1,z2)

plt.savefig("COMBINE",dpi=1000,facecolor="y")
plt.show()