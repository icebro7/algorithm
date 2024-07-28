import random

class RandomizedSet:

    def __init__(self):
        self.conset = set()

    def insert(self, val: int) -> bool:
        if val not in self.conset:
            self.conset.add(val)
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        if val in self.conset:
            self.conset.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_ele = random.choice(list(self.conset))
        return random_ele


if __name__ == '__main__':

    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_2 = obj.remove(2)
    param_3 = obj.insert(2)
    param_4 = obj.getRandom()
    print(param_4)