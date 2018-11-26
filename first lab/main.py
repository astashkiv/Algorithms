from algoritms.puzle import Puzle
from algoritms.sorting import bubble_sort,quicksort
import time

if __name__ == "__main__":
    puzle = []
    lines = [line.rstrip('\n') for line in open('puzle_list.txt')]
    for line in lines:
        fields = line.split(',')
        student = Student(fields[0], fields[1], fields[2], fields[3])
        puzle.append(student)

    print("Bubble sort")
    start_time = time.perf_counter()
    bubble_sort(puzle)
    print("Time: " + str(time.perf_counter() - start_time))
    for item in puzle:
        print(item)

    print("Quick Sort")
    start_time = time.perf_counter()
    quicksort(puzle, 0, len(puzle)-1, 0)
    print("Time: " + str(time.perf_counter() - start_time))
    for item in puzle:
        print(item)


