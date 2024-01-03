import time
import random
import matplotlib.pyplot as plt

SIMULATIONS = 5000
MAX_LENGTH  = 10000
INTERVAL    = 1000

def constructResultList(size):
    result = []
    for i in range(0, size):
        result.append([])
    return result

def drawGraph(functions, tests, results):
    for i, v in enumerate(functions):
        plt.plot(tests, results[i], "x-", label=v[1])
    plt.legend()
    plt.show()

def orderedListTest(functions):
    tests = range(INTERVAL, MAX_LENGTH + 1, INTERVAL)
    results = constructResultList(len(tests))
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
        print(f"{f"{function[1]}({maxValue})":>25} [{"DONE":=^20}]", end="\n")
    drawGraph(functions, tests, results)
    return results

