# Grouped Bar Graph show to bar Graph in one diagram
import matplotlib.pyplot as plt
import numpy as np

models = ["Model A", "Model B", "Model C"]

train_acc = [95, 92, 90]
test_acc = [91, 89, 88]

x = np.arange(len(models))
width = 0.35

plt.bar(x - width/2, train_acc, width=width, label="Train")
plt.bar(x + width/2, test_acc, width=width, label="Test")

plt.xticks(x, models)
plt.ylabel("Accuracy (%)")
plt.title("Model Performance")
plt.legend()

plt.show()