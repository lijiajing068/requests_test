import unittest
from yewu.jiekou.wangyi_login import LoginTest
from yewu.jiekou.select_myselfsongs import SelectSongs
from yewu.jiekou.select_allsongs import select_allsongs
from yewu.jiekou.select_detail import select_detail

class flow01_select(unittest.TestCase):

    def test_select_myself_gedan(self):
        id=LoginTest().test_login_success()
        result=SelectSongs().test_select_songs(id)
        self.assertEqual(result['playlist'][0]['creator']['nickname'], '樱桃你个车厘子1808')
    def test_select_songs(self):
        songid=select_allsongs().test_allsongs()
        result=select_detail().test_select_detail(songid)
        self.assertEqual(result['code'], 200)




if __name__=='__main__':
    unittest.main()
    #unittest.main()  #执行全部案例
    #构造测试集
    #suite=unittest.TestSuite()
    #suite.addTest(flow01_select("test_select_myself_gedan"))
    #suite.addTest(flow01_select("test_select_songs"))

    #执行测试
    #runner=unittest.TextTestRunner()
    #runner.run(suite)


