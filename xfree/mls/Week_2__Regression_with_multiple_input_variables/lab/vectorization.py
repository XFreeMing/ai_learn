import time
import numpy as np
count = 1000000
vector1 = np.random.rand(count)
vector2 = np.random.rand(count)
start_tine = time.time()
result = np.dot(vector1, vector2)
print(f"Time taken for vectorized operation: {time.time() - start_tine}")
for_start_time = time.time()
for i in range(count):
    result = 0
    
    result += vector1[i] * vector2[i]

print(f"Time taken for for loop operation: {time.time() - for_start_time}")