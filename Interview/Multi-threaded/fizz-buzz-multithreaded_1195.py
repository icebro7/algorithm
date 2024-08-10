# @Time :2024/8/23 16:29
from threading import Lock


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizzJobDone = Lock()
        self.buzzJobDone = Lock()
        self.fizzbuzzJobDone = Lock()
        self.numberJobDone = Lock()

        self.fizzJobDone.acquire()
        self.buzzJobDone.acquire()
        self.fizzbuzzJobDone.acquire()
        self.numberJobDone.acquire()

        self.numberJobDone.release()




    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self.fizzJobDone.acquire()
        printFizz()
        self.numberJobDone.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self.buzzJobDone.acquire()
        printBuzz()
        self.numberJobDone.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self.fizzbuzzJobDone.acquire()
        printFizzBuzz()
        self.numberJobDone.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            if i % 3 == 0 and i % 5 == 0:
                self.fizzbuzzJobDone.release()
            elif i % 3 == 0:
                self.fizzJobDone.release()
            elif i % 5 == 0:
                self.buzzJobDone.release()
            else:
                printNumber(i)



