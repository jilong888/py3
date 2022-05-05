import os
class TestCase_1():
    a=0
    def test_3(self):
        # print(111,os.system('cd /Users/jilong/py3/report/allure/'))
        os.system('rm -rf /Users/jilong/py3/report/allure/*')
        assert 1 == 1,'ok1'
    def test_4(self):
        assert 'h' in "hello",'ok2'