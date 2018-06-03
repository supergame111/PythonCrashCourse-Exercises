# 编写一个名为Employee的类，其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。
# 编写一个名为give_raise()的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。
# 为Employee编写一个测试用例，其中包含两个测试方法：test_give_default_raise()和test_give_custom_raise()。
# 使用方法setUp()，以免在每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。

import unittest
from import_lib.employee_11_3 import Employee


class MyTest(unittest.TestCase):

    def setUp(self):
        self.emp = Employee('Z', 'M', 5000)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(10000, self.emp.salary)

    def test_give_custom_raise(self):
        self.emp.give_raise(1000)
        self.assertEqual(6000, self.emp.salary)

    if __name__ == "__main__":
        unittest.main()
