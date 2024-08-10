# @Time :2024/8/20 9:37
from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooJobDone = Lock()
        self.barJobDone = Lock()
        self.barJobDone.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.fooJobDone.acquire()
            printFoo()
            self.barJobDone.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.barJobDone.acquire()
            printBar()
            self.fooJobDone.release()