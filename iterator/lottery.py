import random

class LotteryIterable:
    def __init__(self, all_numbers, numbers_to_draw):
        self.all_numbers = all_numbers
        self.numbers_to_draw = numbers_to_draw

    def __iter__(self):
        return LotteryIterator(self.all_numbers, self.numbers_to_draw)

class LotteryIterator:
    def __init__(self, all_numbers, numbers_to_draw):
        self.numbers = self.draw_numbers(all_numbers, numbers_to_draw)
        self.index = 0

    def draw_numbers(self, all_numbers, numbers_to_draw):
        list_of_numbers = []
        for n in range(numbers_to_draw):
            list_of_numbers.append(random.randint(1, all_numbers))
        return list_of_numbers

    def __next__(self):
        if self.index == len(self.numbers):
            raise StopIteration()
        numbers = self.numbers[self.index]
        self.index += 1
        return numbers

    def __iter__(self):
        return self

