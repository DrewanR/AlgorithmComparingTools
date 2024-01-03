import time
import random
import matplotlib.pyplot as plt

SIMULATIONS = 10000
MAX_LENGTH  = 20000
INTERVAL    = 1000

# # # FUNCTIONS # # # # # # # # # # # # # # # # # # # # # # # #

def linear_search(value, key):
    for i, v in enumerate(value):
        if v == key:
            return i
    return -1

def python_search(value, key):
    if key in value:
        return value.index(key)
    else:
        return -1

def binary_search(value, key, i=0, j=None):
    if j == None:
        j = len(value)-1
    if i >= j:
        if value[i] == key:
            return i
        else:
            return -1
    else:
        mid = round((i+j)/2)
        if value[mid] == key:
            return mid
        elif key < value[mid]:
            return binary_search(value, key, i, mid-1)
        else:
            return binary_search(value, key, mid+1, j)
    

# # # TESTING # # # # # # # # # # # # # # # # # # # # # # # # #
"""These tests make the following assumptions:"""""""""""""""""
" 1. That randint() takes negligable time                     "
" 2. Logging the results takes negliable time                 "
" 3. Background processes have negligable impact on run time  "
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

tests = range(INTERVAL, MAX_LENGTH, INTERVAL)
functions = [ (binary_search, "Binary Search"), (python_search, "Python Search")]
results = [[],[]]
for resultIndex, function in enumerate(functions):
    for i, maxValue in enumerate(tests):
        test_data = list(range(0, maxValue))
        start_time = time.perf_counter()
        for rep in range(0, SIMULATIONS):
            value  = random.randint(0, maxValue) # Note: the max value here represents something not present
            result = function[0](test_data, value)
        finish_time = time.perf_counter()
        results[resultIndex].append((finish_time - start_time) / SIMULATIONS)
        print(f"{f"{function[1]}({maxValue})":>25} [{"="*round((i/len(tests))*20):<20}]", end="\r")
    print(f"{f"Linear Search({MAX_LENGTH})":>25} [{"DONE":=^20}]", end="\n")

for i, v in enumerate(results):
    plt.plot(tests, v, "x-", label=functions[i][1])

plt.legend()
plt.show()
