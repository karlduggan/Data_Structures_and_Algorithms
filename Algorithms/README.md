# Alogrithms

### Sorting Algorithms - (Numerical or alphabetical order)

#### Bubble Sort

```
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr
```

#### Insertion Sort

```
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
    return arr
```

#### Merge Sort

```
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
```

#### Quicksort

```
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

```

Heapsort

### Searching Algorithms

Linear Search
Binary Search
Hash Tables

### Graph Algorithms

Depth-first Search
Breadth-first Search
Dijkstra’s Algorithm
Bellman-Ford Algorithm

### Encryption Algorithms
AES
RSA
Diffe-Hellman


### Compression Algorithms

Gzip
LZ 77
Lempel-Ziv-Welch (LZW)
Huffman coding

Run-Length Encoding (RLE)
```
def rle_compress(data):
    compressed = []
    count = 1
    prev_char = data[0]
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed.append((prev_char, count))
            prev_char = char
            count = 1
    compressed.append((prev_char, count))
    return compressed

def rle_decompress(compressed):
    data = ""
    for char, count in compressed:
        data += char * count
    return data

data = "AAABBBCCCDDDEEE"
compressed = rle_compress(data)
print(compressed)  # [('A', 3), ('B', 3), ('C', 3), ('D', 3), ('E', 3)]
decompressed = rle_decompress(compressed)
print(decompressed)  # AAABBBCCCDDDEEE

```