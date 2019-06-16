class Myqueue():
    def __init__(self, len):
        self.que = [0 for _ in range(len)]
        self.head = 0
        self.tail = 0
        self.len = len

    def push(self):
        if self.tail == self.head:
            print("empty que")
            return
        else:
            out = self.que[self.tail]
            if self.tail == 0:
                self.tail = self.len - 1
            else:
                self.tail -= 1
            return out

    def append(self, num):
        thead = self.head
        if thead == self.len - 1:
            thead = 0
        else:
            thead += 1
        if thead == self.tail:
            print("full queue")
            return
        self.head = thead
        self.que[thead] = num


if __name__ == '__main__':
    a = Myqueue(5)
    a.pop()


