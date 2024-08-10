from queue import Queue


class H2O:
    def __init__(self):
        self.h = Queue(2)
        self.o = Queue(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.put(releaseHydrogen)
        self.res()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.put(releaseOxygen)
        self.res()

    def res(self):
        if self.h.full() and self.o.full():
            self.h.get()()
            self.h.get()()
            self.o.get()()
