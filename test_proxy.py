''' Unit testing rotatingproxy '''
import unittest

from rotatingproxy import RotatingProxy


class ProxyTestCase(unittest.TestCase):
    ''' Tests if proxy is set '''

    def setUp(self):
        ''' set up RotatingProxy object '''
        self.rp = RotatingProxy()

    def test_is_random_proxy(self):
        ''' Is Random Proxy? '''
        try:
            self.rp.set_proxy(self, "r")
            passed = True
        except Exception as e:
            passed = False
        self.assertTrue(passed)

    def test_is_index_proxy(self):
        ''' Is Proxy in list of indexes? '''
        try:
            for p in range(3):
                self.rp.set_proxy(self, proxy_num=p)
            passed = True
        except Exception as e:
            passed = False
        self.assertTrue(passed)


if __name__ == '__main__':
    unittest.main()
