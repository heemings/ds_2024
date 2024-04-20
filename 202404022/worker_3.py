from listQueue import ListQueue
import threading
import time

class Producer:
    def __init__(self, items):
        self.board=[0,0,0]
        for i in range(3):
            self.board[i]=ListQueue()
        self.__alive = True
        self.items=items
        self.pos=0
        self.worker = threading.Thread(target=self.run)

    def get_item(self):
        if self.pos<len(self.items):
            item=self.items[self.pos]
            n=int(item[0])
            self.board[n-1].enqueue(item[1])
            self.pos+=1
            return item[1]
        else:
            return None

    def run(self):
        while True:
            time.sleep(0.2)
            if self.__alive:
                item=self.get_item()
                if not item==None:
                    print("Arrived: ",item)
            else:
                break
        print("Producer is dying...")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive=False
        self.worker.join()

class Consumer:
    def __init__(self):
        self.__alive=True
        self.worker=threading.Thread(target=self.run)

    def run(self):
        while True:
            time.sleep(1)
            if self.__alive:

                for i in range(2,-1,-1):
                    if producer.board[i].front()!=None:
                        t=producer.board[i].front()
                        print("Boarding: ",t)
                        producer.board[i].dequeue()
                        break

                
            else:
                break
        print("Consumer is dying.")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive=False
        self.worker.join()

if __name__ == "__main__":
    
    customers = []
    with open("customer.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            customer = line.split()
            customers.append(customer)

    # FIFO
    names = []
    for c in customers:
        names.append(c[1])

    #producer = Producer()

    producer = Producer(customers)

    consumer = Consumer()    
    producer.start()
    consumer.start()
    time.sleep(10)
    producer.finish()
    consumer.finish()