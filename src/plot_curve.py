import matplotlib.pyplot as plt
from inequality_checker import is_x_y_greater
from data_generator import x_values, y_values

plt.plot(x_values, y_values, label=r'$x^y > y^x$', color='blue')
plt.fill_between(x_values, 1, y_values, color='blue', alpha=0.3)

plt.title('Curve Plot of x^y > y^x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

