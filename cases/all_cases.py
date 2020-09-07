import pytest
import pytest_html
import unittest
def run_all():
    pytest.main(['../cases','--html=report-all.html'])
if __name__ == '__main__':
    run_all()
#pytest.main( ['-s',discover,'--html=../report/report-all.html'])
#runner.run(discover)
#fp.close()
#now = time.strftime("%Y-%m-%d %H_%M_%S")
#filename = './result/' + now + '_result.html'

