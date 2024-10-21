import matplotlib.pyplot as plt

# Data for the chart
labels = ['Nodule','pneumonia', 'infiltration', 'pneumothorax','Normal']
values = [1.4,6.52, 3.455, 98.222,6.978]

# Creating the column chart
plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['red', 'orange', 'yellow', 'green'])

# Adding titles and labels
plt.title('result level')
plt.xlabel('Categories')
plt.ylabel('Percentage')

# Display the chart
plt.show()
