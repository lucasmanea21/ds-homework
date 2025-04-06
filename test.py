import time
#from algorithms.merge_sort import merge_sort
#from algorithms.quick_sort import quick_sort
from algorithms.timSort import timSort
from algorithms.shellSort import shellSort
from algorithms.bucketSort import bucketSort
from algorithms.radixSort import radixSort


test_file = "all_tests.txt"

def load_tests_from_file(filename):
    tests = []
    with open(filename, "r") as f:
        lines = f.readlines()

    T = int(lines[0].split('=')[1].strip())
    i = 1
    for _ in range(T):
        test_type = lines[i].strip().lstrip('#').strip()
        N, MAX = map(int, lines[i+1].strip().split())
        data = list(map(float, lines[i+2:i+2+N]))  # float to support real numbers
        
        tests.append((test_type, N, MAX, data))
        i += 2 + N

    return tests

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def benchmark_algorithms(algorithms):
    tests = load_tests_from_file(test_file)

    for idx, (test_type, N, MAX, data) in enumerate(tests, 1):
        print(f"\n=== Test {idx}: {test_type} | N={N}, MAX={MAX} ===")

        for name, sort_fn in algorithms.items():
            arr = data.copy()
            try:
                start = time.time()

                result = sort_fn(arr)
                if result is not None:
                    arr = result

                end = time.time()
                duration = end - start

                correct = is_sorted(arr)
                status = "✅" if correct else "❌"
                print(f"{status} {name:20s} | {duration:.4f} sec")
                
            except Exception as e:
                print(f"💥 {name:20s} | Crashed: {e}")


sorting_algorithms = {
    "Tim Sort": timSort,
    "Shell Sort": shellSort,
    "Bucket Sort": bucketSort,
    "Radix Sort": radixSort,
    #"Quick Sort": quick_sort,
}

benchmark_algorithms(sorting_algorithms)