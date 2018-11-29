from datetime import datetime


class SortManager:

    compare_num = 0
    swap_num = 0

    @staticmethod
    def compare_count(n):
        SortManager.compare_num += n
        pass

    @staticmethod
    def swap_count(n):
        SortManager.swap_num += n
        pass

    @staticmethod
    def count_reset():
        SortManager.compare_num = 0
        SortManager.swap_num = 0

    # Реалізувати Bubble алгоритм для сортування пазлів  по спаданню за кількістю елементів
    @staticmethod
    def bubble_sort(arr):
        # sorting
        for index in range(len(arr)-1,0,-1):
         for i in range(index):
            SortManager.compare_count(1)
            if arr[i].number_of_parts<arr[i+1].number_of_parts:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                SortManager.swap_count(2)
        return arr

    #sorts elemnets with Quicksort by power consumption in increasing order

    # This function takes last element as pivot, places
    # the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot)
    # to left of pivot and all greater elements to right
    # of pivot
    def partition(arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high].height  # pivot

        for j in range(low, high):
            # If current element is smaller than or
            # equal to pivot
            SortManager.compare_count(1)
            if arr[j].height <= pivot:

                # increment index of smaller element
                i = i + 1
                SortManager.swap_count(2)
                arr[i], arr[j] = arr[j], arr[i]

        SortManager.swap_count(2)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index

    # Function to do Quick sort

    def quickSort(arr, low, high):

        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = SortManager.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            SortManager.quickSort(arr, low, pi - 1)
            SortManager.quickSort(arr, pi + 1, high)

        return arr
