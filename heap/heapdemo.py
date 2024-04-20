class Heap:
    def __init__(self,list):
        if list == None:
            self.__A =[]
        else:
            self.__A = list

    def insert(self,x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A)-1)

    def __percolateUp(self,i:int):
        parent = (i-1) // 2
        if i > 0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)

    def deleteMax(self):
        if (not self.isEmpty()):
            max = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)
            return max
        else:
            return None
    
    def __percolateDown(self, i:int):
        child = 2 * i + 1
        right = 2 * i + 2
        if (child <= len(self.__A)-1):
            if (right <= len(self.__A)-1 and self.__A[child]<self.__A[right]):
                child = right

            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)
        

    def max(self):
        return self.__A[0]

    def buildHeap(self):
        for i in range((len(self.__A)-2) // 2, -1,-1 ):
            self.__percolateDown(i)

    def size(self) -> int:
        return len(self.__A)


    def isEmpty(self) -> bool:
        return len(self.__A) == 0

    def clear(self):
        self.__A = []

    def heapPrint(self):
        enter = 2
        for n in range(len(self.__A)):
            if not self.__A[n] == None :
                x = int(self.__A[n])
                print(x, end=" ")
                if n == enter-2:
                    print("\n")
                    enter=enter*2
        print("")
        print("================")



h1 = Heap([1,11,9,2,3])
h1.buildHeap()
h1.heapPrint()
h1.insert(7)
h1.insert(5)
h1.insert(9)
h1.insert(4)
h1.insert(11)
h1.insert(19)
h1.insert(20)
h1.insert(21)
h1.insert(11)
h1.heapPrint()
h1.deleteMax()
h1.heapPrint