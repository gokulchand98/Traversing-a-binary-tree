from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BalancedBSTHashTable:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, value):
        if not self.root:
            self.root = Node((key, value))
        else:
            self._insert_recursive(self.root, key, value)
        self.size += 1

    def _insert_recursive(self, node, key, value):
        if key < node.value[0]:
            if node.left:
                self._insert_recursive(node.left, key, value)
            else:
                node.left = Node((key, value))
        else:
            if node.right:
                self._insert_recursive(node.right, key, value)
            else:
                node.right = Node((key, value))

    def get(self, key):
        return self._get_recursive(self.root, key)

    def _get_recursive(self, node, key):
        if not node:
            return None
        if key == node.value[0]:
            return node.value[1]
        elif key < node.value[0]:
            return self._get_recursive(node.left, key)
        else:
            return self._get_recursive(node.right, key)

def traverse_alternating(root):
    result = []
    queue = deque([root])
    dfs = True
    while queue:
        if dfs:
            node = queue.pop()
            result.append(node.value)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        else:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        dfs = not dfs
    return result

def sum_and_concatenate(values):
    total_sum = 0
    concatenated_string = ''
    for value in values:
        if isinstance(value, int):
            total_sum += value
        elif isinstance(value, str):
            concatenated_string += value
    return total_sum, concatenated_string

def max_subarray_sum(arr):
    def max_crossing_sum(arr, low, mid, high):
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, low-1, -1):
            current_sum += arr[i]
            if current_sum > left_sum:
                left_sum = current_sum

        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid+1, high+1):
            current_sum += arr[i]
            if current_sum > right_sum:
                right_sum = current_sum

        return left_sum + right_sum

    def max_subarray_sum_recursive(arr, low, high):
        if low == high:
            return arr[low]

        mid = (low + high) // 2
        left_sum = max_subarray_sum_recursive(arr, low, mid)
        right_sum = max_subarray_sum_recursive(arr, mid+1, high)
        crossing_sum = max_crossing_sum(arr, low, mid, high)

        return max(left_sum, right_sum, crossing_sum)

    max_sum = max_subarray_sum_recursive(arr, 0, len(arr)-1)
    return max_sum

# Example usage:
tree = Node(1)
tree.left = Node('a')
tree.right = Node(3)
tree.left.left = Node('b')
tree.left.right = Node(5)
tree.right.left = Node('c')
tree.right.right = Node(7)

values = traverse_alternating(tree)
total_sum, concatenated_string = sum_and_concatenate(values)
print(f'Total sum: {total_sum}')
print(f'Concatenated string: {concatenated_string}')

arr = [2, -3, 4, -1, -2, 1, 5, -3]
max_sum = max_subarray_sum(arr)
print(f'Maximum subarray sum: {max_sum}')
