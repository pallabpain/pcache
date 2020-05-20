import unittest
import pcache
import os
import time


class TestPesistentCache(unittest.TestCase):

    def setUp(self):
        self.filename = "testcache"
        self.cache = pcache.PersistentCache(filename=self.filename)

    def test_add_key(self):
        name = "John Doe"
        self.cache["name"] = name
        self.assertEqual(self.cache["name"], name)

    def test_remove_key(self):
        country = "Japan"
        self.cache["country"] = country
        self.assertEqual(self.cache["country"], country)
        del self.cache["country"]
        self.assertIsNone(self.cache["country"])

    def test_key_expiry(self):
        count = 10
        ttl = 2
        self.cache["count"] = count
        self.assertEqual(self.cache["count"], count)
        self.cache.expire("count", ttl)
        time.sleep(3)
        self.assertIsNone(self.cache["count"])

    def tearDown(self):
        try:
            os.remove(self.filename + ".db")
        except FileNotFoundError:
            try:
                os.remove(self.filename)
            except FileNotFoundError:
                pass
