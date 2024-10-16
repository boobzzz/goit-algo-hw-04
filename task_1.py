import timeit
import random


def insertion_sort(arr: list[int]):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr: list[int]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def tim_sort(array: list[int]):
    array.sort()


def run_sorting_algorithm(algorithm, array):
    if algorithm == "insertion_sort":
        insertion_sort(array)
    elif algorithm == "merge_sort":
        merge_sort(array)
    elif algorithm == "tim_sort":
        tim_sort(array)


def main():
    algorithms = ["insertion_sort", "merge_sort", "tim_sort"]
    sizes = [100, 1000, 10000]
    results = {}

    for algorithm in algorithms:
        results[algorithm] = []
        for size in sizes:
            array = [random.randint(0, 10000) for _ in range(size)]
            exec_time = timeit.timeit(lambda: run_sorting_algorithm(algorithm, array.copy()), number=10)
            results[algorithm].append(exec_time)

    for algorithm in results:
        print(f"{algorithm}:")
        for size, time_taken in zip(sizes, results[algorithm]):
            print(f"  Size {size}: {time_taken:.6f} seconds")


if __name__ == "__main__":
    main()
