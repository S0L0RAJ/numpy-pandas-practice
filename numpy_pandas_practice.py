import numpy as np
import pandas as pd

# NumPy Array Operations
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# Pandas DataFrame Operations
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [23, 25, 22],
    "Score": [85, 90, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nAverage Score:", df["Score"].mean())
