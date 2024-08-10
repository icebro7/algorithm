# @Time :2024/9/2 8:58
from threading import Lock,Semaphore

class DiningPhilosophers:
    def __init__(self):
        self.Limit = Semaphore(4)
        # 叉子锁
        self.Forklock = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        right_fork = philosopher
        left_fork = (philosopher + 1) % 5
        with self.Limit:
            with self.Forklock[right_fork],self.Forklock[left_fork]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()


