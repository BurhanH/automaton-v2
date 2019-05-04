import unittest


class Test(unittest.TestCase):

    def test_upper(self) -> None:
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self) -> None:
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self) -> None:
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
