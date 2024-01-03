import ComparisonTools as ct

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

# # # TESTS # # # # # # # # # # # # # # # # # # # # # # # # # #

functionData = [(linear_search, "Linear"), (binary_search, "Binary")]

results = ct.orderedListTest(functionData)