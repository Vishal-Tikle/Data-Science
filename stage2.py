import matplotlib.pyplot as plt
import pandas as pd

# Read data from a CSV file
data = pd.read_csv('House_Price.csv')

x = data["Location"]
y = data["Price"]
# Create a scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Display the plot
plt.show()



# Sample data
categories = data["Location"]
values = data["Price"]

# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')

# Display the plot
plt.show()

# Show the plot
plt.show()
''' Heat Map '''
data = data.corr()
plt.imshow(data)
plt.title("HeatMap")
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()