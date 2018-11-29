from SortManager import SortManager
from datetime import datetime


class Pazzles(object):
    def __init__(self,
                 description="Cat",
                 number_of_parts = 30,
                 width = 20,
                 height = 30):
        self.description = description
        self.number_of_parts = number_of_parts
        self.width = width
        self.height = height

    def __str__(self):
        return ("Description: " + self.description + ", Number of parts: " +
                str(self.number_of_parts) + ", Width: " + str(self.width) +
                ", Height: " + str(self.height))


class Main:
    ARRAY_SIZE = 10
    pazzles = [Pazzles()] * ARRAY_SIZE

    @staticmethod
    def init():
        with open("Puzzle.txt") as file:
            i = 0
            for line in file:
                array = line.split(",")
                Main.pazzles[i] = Pazzles(array[0], int(array[1]),
                                                  int(array[2]), int(array[3]))
                i += 1

    @staticmethod
    def print_array(arr_name, arr):
        print("\n" + arr_name + ":")
        for arr_i in range(len(arr)):
            print(arr[arr_i])
        print("\n====================\n")


Main.init()
Main.print_array("Initial array", Main.pazzles)

quicksort_arr = Main.pazzles
insertion_sort_arr = Main.pazzles

# Quicksort
start = datetime.now().microsecond
quicksort_arr = SortManager.quickSort(Main.pazzles, 0, len(Main.pazzles) - 1)
finish = datetime.now().microsecond - start
print("Quicksort by memory RESULTS:")
print("Time spent: %s mills" %
      (finish))
print("Number of comparisons: " + str(SortManager.compare_num))
print("Number of item swaps: " + str(SortManager.swap_num))
print("Final arr:")
for j in range(len(quicksort_arr)):
    print(quicksort_arr[j])
print("\n====================\n")

SortManager.count_reset()
start = 0
finish = 0

#  sorting
start = datetime.now().microsecond
insertion_sort_arr = SortManager.bubble_sort(Main.pazzles)
finish = datetime.now().microsecond - start
print("Bubble sort by memory RESULTS:")
print("Time spent: %s mills" %
      (finish))
print("Number of comparisons: " + str(SortManager.compare_num))
print("Number of item swaps: " + str(SortManager.swap_num))
for j in range(len(insertion_sort_arr)):
    print(insertion_sort_arr[j])
print("\n====================\n")
