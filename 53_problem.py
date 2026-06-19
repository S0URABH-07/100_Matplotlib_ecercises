# Specify the Number of Bins
import matplotlib.pyplot as plt

marks = [45, 45,50,60,70,77, 70, 75, 80, 85, 90]

plt.hist(marks, bins=5)
# bins=5 ->It controls how many groups the data is divided into.
plt.show()