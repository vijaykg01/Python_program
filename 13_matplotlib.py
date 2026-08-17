# MATPLOTLIB

import matplotlib.pyplot as plt

# Quick test to confirm it works
month = [1, 2, 3, 4, 5]
sales = [1000, 2500, 1700, 2900, 3500]
plt.plot(month, sales, color='blue', linestyle='--', linewidth=2, marker='o', label='2025 sales data')
plt.xlabel('Months')
plt.ylabel('Sales per Month')
plt.legend(loc='upper left', fontsize=10)
plt.grid(color='gray', linestyle=':', linewidth=1)
plt.xlim(1,5)
plt.ylim(500,4000)
plt.xticks([1,2,3,4,5],['M1','M2','M3','M4','M5'])
plt.show()
