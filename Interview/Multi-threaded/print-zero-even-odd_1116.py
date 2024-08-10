# @Time :2024/8/20 9:58
from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zeroJobDone = Lock()
        self.evenJobDone = Lock()
        self.oddJobDone = Lock()

        self.evenJobDone.acquire()
        self.oddJobDone.acquire()
        self.zeroJobDone.acquire()
        self.zeroJobDone.release()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zeroJobDone.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.oddJobDone.release()
            else:
                self.evenJobDone.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2,self.n + 1,2):
            self.evenJobDone.acquire()
            printNumber(i)
            self.zeroJobDone.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n + 1,2):
            self.oddJobDone.acquire()
            printNumber(i)
            self.zeroJobDone.release()


