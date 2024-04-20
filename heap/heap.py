class LFUNode:
    def __init__(self, lpn, frequency):
        self.lpn = lpn
        self.frequency = frequency

class Heap:
    def __init__(self, lst=None):
        if lst is None:
            self.__A = []
        else:
            self.__A = lst

    def insert(self,x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A)-1)

    def find(self, x):
        idx = self.__A.index(x)
        self.__percolateDown(idx)


    def __percolateUp(self,i:int):
        parent = (i-1) // 2
        if i > 0 and self.__A[i].frequency < self.__A[parent].frequency:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)

    def deleteMin(self):
        if not self.isEmpty():
            min_value = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)
            return min_value
        else:
            return None

    def __percolateDown(self, i:int):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < len(self.__A) and self.__A[left_child].frequency < self.__A[smallest].frequency:
            smallest = left_child
        if right_child < len(self.__A) and self.__A[right_child].frequency < self.__A[smallest].frequency:
            smallest = right_child

        if smallest != i:
            self.__A[i], self.__A[smallest] = self.__A[smallest], self.__A[i]
            self.__percolateDown(smallest)

    def min(self):
        return self.__A[0]

    def size(self) -> int :
        return len(self.__A)

    def isEmpty(self) -> bool:
        return len(self.__A) == 0

    def clear(self):
        self.__A = []

    def heapPrint(self):
        enter = 2
        for n in range(len(self.__A)):
            if not self.__A[n] == None :
                x = self.__A[n].frequency
                print(x, end=" ")
                if n == enter-2:
                    print("\n")
                    enter=enter*2
        print("")
        print("================")


    def __len__(self):
        return len(self.__A)
