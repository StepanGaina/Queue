import unittest
from QUEUE import Queue


class TestQUEUE(unittest.TestCase):
    """ Тесты для QUEUE """
    def setUp(self):
        self.q = Queue()

    def test_init(self):
        self.assertEqual(self.q.size(), 0)

    def test_front(self):
        self.assertTrue(self.q.front() is None)

    def test_back(self):
        self.assertTrue(self.q.back() is None)

    def test_enqueue(self):
        self.q.enqueue(1)
        self.q.enqueue('Stepan')
        self.assertTrue(self.q.size() == self.q.size())
        print(self.q.size())

    def test_enqueue2(self):
        self.q.enqueue is None
        self.assertTrue(self.q.size() == 0)

    def test_dequeue(self):
        self.q.enqueue(1)
        self.q.enqueue(1)
        self.q.dequeue()
        self.assertTrue(self.q.size() == self.q.size())
        print(self.q.size())

    def test_dequeue2(self):
        self.q.enqueue(1)
        self.q.dequeue()
        self.assertTrue(self.q.size() == 0)
        print(self.q.size())

    def test_size(self):
        self.q.enqueue(1)
        self.q.enqueue(1)
        self.assertTrue(self.q.size() > 0)
        print(self.q.size())

    def test_size2(self):
        self.q.enqueue(1)
        self.q.enqueue(1)
        self.q.dequeue()
        self.q.dequeue()
        self.assertTrue(self.q.size() == 0)
        print(self.q.size())

    def test_clear(self):
        self.q.enqueue(1)
        self.q.enqueue(1)
        self.q.clear()
        self.assertTrue(self.q.size() == 0)


if __name__ == '__main__':
    unittest.main()

