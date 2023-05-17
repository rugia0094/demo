from unittest import TestCase, main
from main import *


class ProgramTest(TestCase):

    def test_success_replace_1(self):
        self.assertEqual(replace('Один'), 1)

    def test_success_replace_2(self):
        self.assertEqual(replace('Два'), 2)

    def test_success_replace_3(self):
        self.assertEqual(replace('Три'), 3)

    def test_success_replace_4(self):
        self.assertEqual(replace('Четыре'), 4)

    def test_success_replace_5(self):
        self.assertEqual(replace('Пять'), 5)


if __name__ == "__main__":
    main()