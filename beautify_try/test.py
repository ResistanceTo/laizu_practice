import requests
from utils import catch, BaseClass


class So(BaseClass):
    def __init__(self):
        super().__init__()
        self.url = "https://google.com/"

    @catch
    def _get(self):
        
        resp = requests.get(self.url, timeout=3)
        print(resp.status_code)
        return resp.status_code


if __name__ == "__main__":
    so = So()
    so._get()
    requests.get("https://google.com/", timeout=2)