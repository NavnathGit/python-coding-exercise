
from collections import deque

# Aproach 1- Using set and queue


class Logger:

    def __init__(self):
        self._msg_set = set()
        self._msg_queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break

        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

class Logger1:
    def __init__(self):
        self._msg_dict = {}

    def shouldPrintMessage2(self, timeStamp, message):
        # case 1). add the message to print
        if message not in self._msg_dict:
            self._msg_dict[message] = timeStamp
            return True

        if timeStamp - self._msg_dict[message] >= 10:
            self._msg_dict[message] = timeStamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
obj = Logger1()
timestamp = 1
message = "foo"
param_1 = obj.shouldPrintMessage2(timestamp, message)
print(param_1)

timestamp = 2
message = "foo"
param_1 = obj.shouldPrintMessage2(timestamp, message)
print(param_1)
