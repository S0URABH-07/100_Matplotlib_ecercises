import matplotlib.pyplot as plt
import numpy as np

# Categories
subjects = ["Math", "Science", "English", "History"]

# Data
student1 = [80, 75, 90, 85]
student2 = [70, 85, 88, 80]

# X-axis positions
x = np.arange(len(subjects))

# Width of each bar
width = 0.35

# Create two bars side by side
plt.bar(x - width/2, student1, width=width, label="Student 1")
plt.bar(x + width/2, student2, width=width, label="Student 2")

# Labels and title
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")
plt.xticks(x, subjects)
plt.legend()

plt.show()