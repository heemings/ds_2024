from listQueue import *

sw=0
def isSame(a)->bool:
    s=Listqueue()
    for i in range(len(a)):
        if sw==0:
            s.enqueue(a[i])
        elif a[i]=='$':
            sw==1
        else:
            if s.front()==a[i]:
                s.dequeue()
    s.printQueue()

    if s.isEmpty():
        return True
    else:
        return False
    



def main():
    str='abc$abc'
    t=isSame(str)
    print(t)

if __name__=="__main__":
    main()
    