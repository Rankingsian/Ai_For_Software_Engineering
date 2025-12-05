import time
import random
from operator import itemgetter

# Generate a large list of dictionaries for testing
def generate_data(size=10000):
    return [{'id': i, 'value': random.randint(1, 10000), 'name': f'Item {i}'} for i in range(size)]

# Manual Implementation: Bubble Sort (Inefficient but demonstrates manual logic)
# Note: A better manual implementation would be Merge Sort or Quick Sort, 
# but often "manual" implies writing the logic yourself vs using built-ins.
# For a fair comparison of "efficient manual" vs "AI/Built-in", we could use a custom Merge Sort.
# Let's use a custom Merge Sort for a respectable manual attempt.
def manual_sort_by_key(data, key):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = manual_sort_by_key(data[:mid], key)
    right = manual_sort_by_key(data[mid:], key)
    
    return merge(left, right, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# AI-Suggested/Pythonic Implementation: Using built-in sorted() or list.sort()
def ai_suggested_sort(data, key):
    return sorted(data, key=lambda x: x[key])

# Alternative AI suggestion using itemgetter (often slightly faster)
def ai_suggested_sort_optimized(data, key):
    return sorted(data, key=itemgetter(key))

def main():
    data_size = 10000
    data = generate_data(data_size)
    
    print(f"Sorting {data_size} items by 'value' key...\n")
    
    # Test Manual Implementation
    data_copy_1 = data.copy()
    start_time = time.time()
    sorted_manual = manual_sort_by_key(data_copy_1, 'value')
    manual_duration = time.time() - start_time
    print(f"Manual Implementation (Merge Sort): {manual_duration:.6f} seconds")
    
    # Test AI Suggested Implementation
    data_copy_2 = data.copy()
    start_time = time.time()
    sorted_ai = ai_suggested_sort(data_copy_2, 'value')
    ai_duration = time.time() - start_time
    print(f"AI Suggested (sorted + lambda):     {ai_duration:.6f} seconds")

    # Verify results match
    assert sorted_manual == sorted_ai
    print("\nVerification: Both methods produced the same sorted result.")
    
    if manual_duration > 0:
        speedup = manual_duration / ai_duration
        print(f"AI version is {speedup:.2f}x faster.")

if __name__ == "__main__":
    main()
