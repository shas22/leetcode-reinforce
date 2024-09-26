class MyCalendar:

    def __init__(self):
        self.slots = []

    def book(self, start: int, end: int) -> bool:
        for st, en in self.slots:
            if not(start >= en or end <= st):
                return False
        
        self.slots.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)