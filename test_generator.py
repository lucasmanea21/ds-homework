import random

def generate_random_integers(n, max_val):
    return [random.randint(0, max_val) for _ in range(n)]

def generate_sorted(n):
    return list(range(n))

def generate_reversed(n):
    return list(range(n, 0, -1))

def generate_nearly_sorted(n, swaps=10):
    arr = list(range(n))
    
    # swap some random values
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def generate_all_equal(n, value=91):
    return [value] * n

def generate_many_duplicates(n, unique_vals=10):
    values = [random.randint(0, 1000) for _ in range(unique_vals)]
    return [random.choice(values) for _ in range(n)]

def generate_random_floats(n, max_val):
    return [random.uniform(0, max_val) for _ in range(n)]

def write_all_tests_to_file(filename, test_cases):
    with open(filename, "w") as f:
        f.write(f"T = {len(test_cases)}\n")
        
        for N, MAX, data in test_cases:
            f.write(f"{N} {MAX}\n")
            for num in data:
                f.write(f"{num}\n")
                
test_cases = []

sizes = [1_000, 100_000, 1_000_000, 5_000_000]
max_val = 10**6

for n in sizes:
    test_cases.append((n, max_val, generate_random_integers(n, max_val)))
    test_cases.append((n, max_val, generate_sorted(n)))
    test_cases.append((n, max_val, generate_reversed(n)))
    test_cases.append((n, max_val, generate_nearly_sorted(n, swaps=50)))
    test_cases.append((n, max_val, generate_all_equal(n)))
    test_cases.append((n, max_val, generate_many_duplicates(n)))

# floats
test_cases.append((10_000, 1000, generate_random_floats(10_000, 1000)))
test_cases.append((100_000, 1000, generate_random_floats(100_000, 1000)))

write_all_tests_to_file("all_tests.txt", test_cases)
print(f"Generated {len(test_cases)} tests into all_tests.txt")
