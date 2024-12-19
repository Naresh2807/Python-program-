import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Sample predictions and true values
true_labels = ['FAKE', 'REAL']  # Labels
conf_matrix = [[589, 39], [45, 594]]  # Replace with your confusion matrix

# Plotting the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=true_labels, yticklabels=true_labels)

# Add labels, title, and axis ticks
plt.title('Confusion Matrix', fontsize=16)
plt.xlabel('Predicted Label', fontsize=14)
plt.ylabel('True Label', fontsize=14)
plt.show()
