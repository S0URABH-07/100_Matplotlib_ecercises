# Draw scatter chart and Add titles and axis labels and also set transparency
import matplotlib.pyplot as plt
x = ["R","S","N","Y"]
y = [5, 2, 7, 4]

plt.scatter(x, y,alpha=0.3)

plt.title("Student Scores")
plt.xlabel("Student ID")
plt.ylabel("Marks")

plt.show()