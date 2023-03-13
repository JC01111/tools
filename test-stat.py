import numpy as np
import math

# Input
# input1 = input("List 1 seperated by space:").split()
# input1 = input("List 2 seperated by space:").split()
# arr1 = np.array(list(map(float, input1)))
# arr2 = np.array(list(map(float, input1)))

arr1=np.array([43.8, 64.1, 51.7, 63.3, 70.1, 35.6])
arr2=np.array([41.9, 63.2, 48.9, 65, 65.9, 38.5])
miu_d = 0
tc = 2.571

# Calculation
diff = arr1 - arr2
sum_diff = sum(arr1 -arr2)

# Round mean of the differences to 4 decimals
mean_diff = round(sum_diff / len(arr1), 4)

sum_di_min_d = sum((diff - mean_diff) ** 2)

Sd = round(np.sqrt(sum_di_min_d / (len(arr1) -1)), 4)

test_stat = round((mean_diff - miu_d) / (Sd / np.sqrt(len(arr1))), 2)

# Confidence interval
lower_bound = round(mean_diff - tc * (Sd / np.sqrt(len(arr1))), 4)
upper_bound = round(mean_diff + tc * (Sd / np.sqrt(len(arr1))), 4)

# Output
# print(arr1)
# print(arr2)
print("mean difference:", mean_diff)
print("Standard Deviation:", Sd)
print("test stat:", test_stat)

print("lower_bound:", lower_bound)
print("upper_bound:", upper_bound)

# Notes:
"""
If 95% confidence, tc = 2.360
If 99% confidence, tc = 4.032

Need to parse input

test stat works well
"""