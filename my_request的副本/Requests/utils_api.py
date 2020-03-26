import requests
data  = {
  "diseaseCode": "string",
  "diseaseName": "接口测试2334",
  "diseaseTypeCode": "string"
}
class Request_Method:

    def api(self,url,data=None,json=None,headers=None,cookies=None,method=None):
        if method == "get":
            re = requests.get(url,data=None,json=None,headers=None,cookies=None)
        elif method == "post":
            re = requests.post(url,data=None,json=None,headers=None,cookies=None)
        else:
            print("接口请求错误")

        code = re.status_code
        try:
            body = re.json()
            print("dasdasdasdasdasdasda")
        except Exception as e:
            body = re.text
            print("dasdas")
        res = {}
        res["code"] = code
        res["body"] = body
        return res
    
    def api_get(self,url,**kwargs):
        return self.api(url,method="get",**kwargs)

    def api_post(self,url,**kwargs):
        return self.api(url,method="post",**kwargs)

aa = Request_Method()
print(aa.api_get("https://api.xiaobangtouzi.com/community/article/get?articleId=711701804"))