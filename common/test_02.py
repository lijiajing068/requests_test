#encoding=utf-8
import pytest
class TestCase():

    def test_01(self):
        a="hello"
        assert "h" in a
    def test_02(self):
        b="hello"
        assert "hello" == b
    def test_03(self):
        b=5
        assert 5 == b
if __name__ == '__main__':
    pytest.main(["-s", "test_02.py"])
