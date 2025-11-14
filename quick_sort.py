import random
import time
import sys

# Allow deeper recursion
sys.setrecursionlimit(50000)


# --------------------------------------------------
# Deterministic Quicksort (in-place Lomuto partition)
# --------------------------------------------------
def deterministic_quicksort(arr):

    def quicksort_helper(a, low, high):
        if low < high:
            p = partition(a, low, high)
            quicksort_helper(a, low, p - 1)
            quicksort_helper(a, p + 1, high)

    def partition(a, low, high):
        pivot = a[high]
        i = low
        for j in range(low, high):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[high] = a[high], a[i]
        return i

    arr_copy = arr[:]
    quicksort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


# --------------------------------------------------
# Randomized Quicksort
# --------------------------------------------------
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + mid + randomized_quicksort(right)


# --------------------------------------------------
# Timing helper
# --------------------------------------------------
def measure_time(sort_fn, arr):
    arr_copy = arr[:]
    start = time.time()
    try:
        sort_fn(arr_copy)
    except RecursionError:
        return None
    end = time.time()
    return end - start


# --------------------------------------------------
# Empirical comparison
# --------------------------------------------------
def empirical_test():
    sizes = [1000, 5000, 10000, 20000]
    results = []

    for n in sizes:
        random_arr = [random.randint(1, n) for _ in range(n)]
        sorted_arr = sorted(random_arr)
        reverse_arr = sorted_arr[::-1]

        results.append({
            "n": n,
            "random_det": measure_time(deterministic_quicksort, random_arr),
            "random_rand": measure_time(randomized_quicksort, random_arr),
            "sorted_det": measure_time(deterministic_quicksort, sorted_arr),
            "sorted_rand": measure_time(randomized_quicksort, sorted_arr),
            "reverse_det": measure_time(deterministic_quicksort, reverse_arr),
            "reverse_rand": measure_time(randomized_quicksort, reverse_arr),
        })

    return results


# --------------------------------------------------
# Save results to files
# --------------------------------------------------
def save_results(results):

    # TXT FILE -------------------------------------------------
    with open("results.txt", "w") as f:
        f.write("n, random_det, random_rand, sorted_det, sorted_rand, reverse_det, reverse_rand\n")
        for r in results:
            f.write(f"{r['n']}, {r['random_det']}, {r['random_rand']}, "
                    f"{r['sorted_det']}, {r['sorted_rand']}, "
                    f"{r['reverse_det']}, {r['reverse_rand']}\n")

    # CSV FILE -------------------------------------------------
    with open("results.csv", "w") as f:
        f.write("n,random_det,random_rand,sorted_det,sorted_rand,reverse_det,reverse_rand\n")
        for r in results:
            f.write(f"{r['n']},{r['random_det']},{r['random_rand']},"
                    f"{r['sorted_det']},{r['sorted_rand']},"
                    f"{r['reverse_det']},{r['reverse_rand']}\n")

    # MARKDOWN TABLE -------------------------------------------
    with open("results.md", "w") as f:
        f.write("| n | random_det | random_rand | sorted_det | sorted_rand | reverse_det | reverse_rand |\n")
        f.write("|---|------------|-------------|------------|-------------|-------------|--------------|\n")
        for r in results:
            f.write(f"| {r['n']} | {r['random_det']} | {r['random_rand']} | "
                    f"{r['sorted_det']} | {r['sorted_rand']} | "
                    f"{r['reverse_det']} | {r['reverse_rand']} |\n")


# --------------------------------------------------
# Print formatted table
# --------------------------------------------------
def print_table(results):
    print("\n" + "-"*95)
    print("{:<8} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        "n", "random_det", "random_rand", "sorted_det", "sorted_rand", "reverse_det", "reverse_rand"))
    print("-"*95)

    for r in results:
        print("{:<8} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(
            r["n"],
            r["random_det"],
            r["random_rand"],
            r["sorted_det"],
            r["sorted_rand"],
            r["reverse_det"],
            r["reverse_rand"]
        ))

    print("-"*95)


# --------------------------------------------------
# Main
# --------------------------------------------------
if __name__ == "__main__":
    results = empirical_test()

    print("\n--- Empirical Results (Table) ---")
    print_table(results)

    save_results(results)
    print("\nResults saved as: results.txt, results.csv, results.md")