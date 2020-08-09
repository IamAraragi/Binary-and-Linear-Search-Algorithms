import random
from search import linear_search, binary_search
from time import time
import matplotlib.pyplot as plt

elapsed_linear = []
elapsed_binary = []
x = []

for i in range(10000, 100000, 10000):
        #Data
	data = random.sample(range(i), i)
	sorted_data = sorted(data)
	random_number = random.randint(0,len(data)-1)

	#For Linear Search
	start_linear = time()
	index_linear = linear_search(data, random_number)
	end_linear = time()
	elapsed_linear.append((end_linear - start_linear))

	#For Binary Search
	start_binary = time()
	index_binary = binary_search(sorted_data, 0, len(data)-1, random_number)
	end_binary = time()
	elapsed_binary.append((end_binary - start_binary))

	x.append(i)

plt.plot(x, elapsed_linear, label="linear_search")
plt.plot(x, elapsed_binary, label="binary_search")

plt.xlabel('Input size')
plt.ylabel('Execution time')

plt.title('Input size vs Execution-time graph')
plt.legend()

plt.show()

print("The best case for linear_search is: {} ".format(min(elapsed_linear)))
print("The worst case for linear_search is: {} ".format(max(elapsed_linear)))
print("The best case for binary search is: {} ".format(min(elapsed_binary)))
print("The worst case for binary search is: {} ".format(max(elapsed_binary)))