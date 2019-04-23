import urllib.request as request
import json
from datetime import datetime

class WaqiQueryUrlBuilder:
    """
    Build desired url
    """
    root_url = "https://api.waqi.info/feed/"
    token = "3c7c262efbfad0c1d3921f5a3884987c614a1557"

    def __init__(self):
        pass

    def get_url(self, idx):
        return self.root_url + '@' + str(idx) + '/?token=' + self.token

class DirectoryPathManager:
    """
    Manage the paths for files
    """
    path_root_sor = "D:/AQI_Track/Data/SOR/"

    def __init__(self):
        pass

    def get_sor_path(self):
        return self.path_root_sor + "transactions_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".txt"

# script execution
def job_fetch_waqi_data():
    url = WaqiQueryUrlBuilder().get_url(idx=455)
    res = request.urlopen(url)
    data = json.loads(res.read())
    path = DirectoryPathManager().get_sor_path()
    print(path)
    with open(path, 'w') as outfile:
        json.dump([data], outfile)
