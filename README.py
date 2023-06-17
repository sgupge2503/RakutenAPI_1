# ほげ
import requests
import json
from pprint import pprint

res = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?applicationId=1009993429057254143')

json_data = json.loads(res.text)
pprint(json_data)