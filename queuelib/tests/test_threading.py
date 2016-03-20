import threading
import unittest

from queuelib.pqueue import PriorityQueue
from queuelib.queue import (
    FifoMemoryQueue, LifoMemoryQueue, FifoDiskQueue, LifoDiskQueue,
    FifoSQLiteQueue, LifoSQLiteQueue,
)
from queuelib.tests import QueuelibTestCase


class FifoMemoryThreadingTest(unittest.TestCase):
    
    def push_and_pop(self):
        for i in xrange(self.itemcnt):
            self.q.push(i)

        while True:
            i = self.q.pop()
            if i is None:
                break
            self.sum += i

    def test_threading(self):
        self.q = FifoMemoryQueue()

        thread_cnt = 1000
        self.itemcnt = 1000
        self.sum = 0
        
        threads = []        
        for i in xrange(thread_cnt):
            t = threading.Thread(target=self.push_and_pop)
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        self.assertEqual(thread_cnt * self.itemcnt * (self.itemcnt-1) / 2, self.sum)
