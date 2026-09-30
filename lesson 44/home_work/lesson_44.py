# 1
def sp_eng(sentence):
    return "english" in sentence.lower()

# 2
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))

# 3

def count_sheeps(sheep):
    return sheep.count(True)

# 4

def area_or_perimeter(l, w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)


# 5
def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))
    