# =================
# NUMPY OPERATORS
# =================

import numpy as np

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** 2)

# ===========================
# NUMPY AGGREGATE FUNCTIONS
# ===========================

import numpy as np

sales = np.array([100, 200, 300, 400, 500])

print(np.sum(sales))
print(np.mean(sales))
print(np.median(sales)) # middel value
print(np.min(sales))
print(np.max(sales))

# 6. STANDARD DEVIATION
print(np.std(sales))

# 7. VARIANCE
print(np.var(sales))

# 8. PRODUCT
print(np.prod(sales))

# 9. RANGE
print(np.ptp(sales))

# 10. COUNT NON-ZERO
data = np.array([10, 0, 20, 0, 30])

print(np.count_nonzero(data))

# 2-D ARRAY

import numpy as np

data = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

# Total
print(np.sum(data))

# Column-wise
print(np.sum(data, axis=0))

# Row-wise
print(np.sum(data, axis=1))

# Column average
print(np.mean(data, axis=0))

# Row average
print(np.mean(data, axis=1))

# Column minimum
print(np.min(data, axis=0))

# Row maximum
print(np.max(data, axis=1))

# ============================================================
# NUMPY ARRAY MODIFICATIONS — COMPLETE PRACTICE CODE
# ============================================================

import numpy as np

# Original 1D array
a = np.array([10, 20, 30, 40, 50, 60])

print("Original:", a)


# 1. RESHAPE
# Change 1D array into 2 rows × 3 columns
result = a.reshape(2, 3)
print("\n1. reshape():")
print(result)


# 2. FLATTEN
# Convert 2D array back to 1D
result = result.flatten()
print("\n2. flatten():")
print(result)


# 3. RAVEL
# Convert multidimensional array to 1D
matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])

result = matrix.ravel()
print("\n3. ravel():")
print(result)


# 4. RESIZE
# Changes the size/shape of the original array
b = np.array([10, 20, 30, 40])
b.resize(2, 2)

print("\n4. resize():")
print(b)


# 5. APPEND
# Add values at the end
a = np.array([10, 20, 30])

result = np.append(a, 40)

print("\n5. append():")
print(result)


# 6. INSERT
# Insert 99 at index 2
a = np.array([10, 20, 30, 40])

result = np.insert(a, 2, 99)

print("\n6. insert():")
print(result)


# 7. DELETE
# Delete value at index 2
a = np.array([10, 20, 30, 40])

result = np.delete(a, 2)

print("\n7. delete():")
print(result)


# 8. CONCATENATE
# Combine two arrays
a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.concatenate((a, b))

print("\n8. concatenate():")
print(result)


# 9. VSTACK
# Add arrays vertically → rows
a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.vstack((a, b))

print("\n9. vstack():")
print(result)


# 10. HSTACK
# Add arrays horizontally → columns
a = np.array([[10],
              [20],
              [30]])

b = np.array([[40],
              [50],
              [60]])

result = np.hstack((a, b))

print("\n10. hstack():")
print(result)


# 11. SORT
# Sort values in ascending order
a = np.array([50, 10, 40, 20, 30])

result = np.sort(a)

print("\n11. sort():")
print(result)


# 12. REVERSE
# Reverse the array using slicing
a = np.array([10, 20, 30, 40, 50])

result = a[::-1]

print("\n12. Reverse:")
print(result)


# 13. BOOLEAN FILTERING
# Select values greater than 30
a = np.array([10, 20, 30, 40, 50])

result = a[a > 30]

print("\n13. Boolean filtering:")
print(result)


# 14. REPLACE VALUES
# Replace values greater than 30 with 0
a = np.array([10, 20, 30, 40, 50])

a[a > 30] = 0

print("\n14. Replace:")
print(a)


# 15. WHERE
# IF value >= 30 → "High", otherwise → "Low"
a = np.array([10, 30, 50, 20, 80])

result = np.where(a >= 30, "High", "Low")

print("\n15. where():")
print(result)


# 16. UNIQUE
# Find unique values
a = np.array([10, 20, 10, 30, 20, 40])

result = np.unique(a)

print("\n16. unique():")
print(result)


# UNIQUE + COUNT
values, counts = np.unique(a, return_counts=True)

print("\nUnique values:", values)
print("Counts:", counts)


# 17. ASTYPE
# Change datatype
a = np.array([10, 20, 30])

result = a.astype(float)

print("\n17. astype():")
print(result)
print(result.dtype)


# 18. TRANSPOSE
# Convert rows into columns
a = np.array([[10, 20, 30],
              [40, 50, 60]])

result = a.T

print("\n18. Transpose (.T):")
print(result)


# 19. SQUEEZE
# Remove dimensions of size 1
a = np.array([[[10, 20, 30]]])

print("\n19. squeeze() - before:")
print(a.shape)

result = np.squeeze(a)

print("After:")
print(result)
print("Shape:", result.shape)


# 20. EXPAND_DIMS
# Add a new dimension
a = np.array([10, 20, 30])

result = np.expand_dims(a, axis=0)

print("\n20. expand_dims():")
print(result)
print("Shape:", result.shape)

# ========================
## HANDLING MISSING DATA
# ========================
## NAN VALUES

import numpy as np

# finding nan value using isnan
arr = ([10,20,np.nan,40,50,np.nan,70])
print(np.isnan(arr))

# replacing nan value using nan_to_num
cleaned_arr = np.nan_to_num(arr)
print(cleaned_arr)

## INFINITE VALUES

import numpy as np

# finding infinite value using isinf
arr = ([10,20,np.inf,40,50,-np.inf,70])
print(np.isinf(arr))

# replacing nan value using nan_to_num
cleaned_arr = np.nan_to_num(arr, posinf=0, neginf=0)
print(cleaned_arr)
