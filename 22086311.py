import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Read data from the CSV file
data = pd.read_csv("data1-1.csv" , header=None , names=["Salary"])

# Calculate mean and standard deviation of the salary data
mean_salary = np.mean(data["Salary"])
mean_salary = round(mean_salary , 2)
std_dev_salary = np.std(data["Salary"])
std_dev_salary = round(std_dev_salary , 2)

# Generate a range of values for the x-axis based on a normal distribution
x_values = np.linspace(mean_salary - 3 * std_dev_salary ,
                       mean_salary + 3 * std_dev_salary , 1000)

# Create a probability density function (PDF) using a normal distribution
pdf_values = norm.pdf(x_values , mean_salary , std_dev_salary)

# Plot the histogram and PDF
plt.hist(data["Salary"] , bins=30 , density=True , alpha=0.7 , label="Histogram" , color='olive')
plt.plot(x_values , pdf_values , label="Probability Density Function (PDF)" , color="red")
# Find the salary value (X) below which 33% of people fall
X = np.percentile(data["Salary"] , 33)
X = round(X , 2)

# Plot mean and X on the graph as dashed lines
plt.axvline(mean_salary , color='blue' , linestyle='dashed' , linewidth=2 ,
            label=f'Mean Salary: {mean_salary:.2f}')
plt.axvline(X , color='green' , linestyle='dashed' , linewidth=2 , label=f'X: {X:.2f}')

# Set up plot labels and title
plt.xlabel("Annual Salary (Euros)")
plt.ylabel("Probability Density")
plt.title("Probability Density Function of Salaries")

# Add legend to the plot
plt.legend()

print("mean salary =" , mean_salary)
print("X value =" , X)
# Display the plot
plt.show()
