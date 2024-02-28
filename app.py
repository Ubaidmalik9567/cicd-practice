import matplotlib.pyplot as plt

# Sample fruits data
fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango']
quantities = [33, 50, 40, 25, 35]

# Create bar plot
plt.figure(figsize=(8, 6))
plt.bar(fruits, quantities, color='skyblue')
plt.xlabel('Fruits')
plt.ylabel('Quantities')
plt.title('Quantities of Fruits (Bar Plot)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()

# Save bar plot image
plt.savefig('fruits_bar_plot.png')

# Show bar plot
plt.show()

# Create line plot
plt.figure(figsize=(8, 6))
plt.plot(fruits, quantities, marker='o', color='green', linestyle='-')
plt.xlabel('Fruits')
plt.ylabel('Quantities')
plt.title('Quantities of Fruits (Line Plot)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()

# Save line plot image
plt.savefig('fruits_line_plot.png')

# Show line plot
plt.show()
