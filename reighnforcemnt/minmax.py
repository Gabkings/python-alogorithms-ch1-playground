def minmax(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        else:
            smallest = item
    return smallest , largest

print(minmax([1,23,45,68,70]))