from inequality_checker import is_x_y_greater
from data_generator import x_values, y_values
import matplotlib.pyplot as plt

# Example usage in main.py
x_first, y_first = x_values[0], y_values[0]
result = is_x_y_greater(x_first, y_first)

print(f"For the first data point (x={x_first}, y={y_first}):")
print(f"Raw data: x_values = {x_values}, y_values = {y_values}")
if result:
    print("Yes, x^y is greater than y^x!")
else:
    print("No, x^y is not greater than y^x.")

# Include the code for plotting if needed
plt.plot(x_values, y_values, label=r'$x^y > y^x$', color='blue')
plt.fill_between(x_values, 1, y_values, color='blue', alpha=0.3)

plt.title('Curve Plot of x^y > y^x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

