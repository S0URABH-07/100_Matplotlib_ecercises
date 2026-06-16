import matplotlib.pyplot as plt
import numpy as np

subjects = ["Math", "Science", "English", "History"]

student1 = [80, 75, 90, 85]
student2 = [70, 85, 88, 80]

x = np.arange(len(subjects))
width = 0.35
plt.bar(x - width/2, student1, width=width, label="Student 1")
plt.bar(x + width/2, student2, width=width, label="Student 2")

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")
plt.xticks(x, subjects)
plt.legend()
plt.show()