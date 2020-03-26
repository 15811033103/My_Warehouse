import pytest


class Testcase:
    data_list = [("xiaohei","654321"),("xiaohong","111111")]
    @pytest.mark.parametrize(("name","password"),data_list)
    def test01(self,name,password):
        print(name,password)



a = Testcase()
print(a.test01)