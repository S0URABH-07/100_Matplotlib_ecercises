# Use Top diffrent parameters and Draw Bar Graph
import matplotlib.pyplot as plt

algorithms = ["Logistic Regression","Decision Tree","Random Forest","XGBoost"]

accuracy = [84, 88, 93, 95]

bars = plt.bar(algorithms,accuracy,color=["gray", "orange", "green", "blue"],edgecolor="black",linewidth=1.5)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height()}%",
        ha="center",
        va="bottom"
    )

plt.ylim(0, 100)
plt.ylabel("Accuracy (%)")
plt.title("Machine Learning Model Accuracy")
plt.grid(axis="y", linestyle=":")

plt.show()