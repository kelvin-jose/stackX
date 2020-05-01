from exceptions import StackOverflow
from exceptions import StackUnderflow


class stack:
    def __init__(self, max_size=8, reset_on_full=False):
        self.max_size = max_size
        self.stack = [None] * self.max_size
        self.reset_on_full = reset_on_full
        self.top = -1

    @staticmethod
    def ping():
        return 'pong!'

    def push(self, value):
        if self.top + 1 == self.max_size:
            if self.reset_on_full:
                self.reset()
                self.push(value)
            else:
                raise StackOverflow
        if value is not None:
            self.top += 1
            self.stack[self.top] = value
        else:
            raise ValueError

    def pop(self):
        if self.top == -1:
            raise StackUnderflow
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return value

    def full(self):
        if self.top + 1 == self.max_size:
            return True
        else:
            return False

    def show_all(self):
        return self.stack

    def reset(self):
        self.__init__(self.max_size, self.reset_on_full)
