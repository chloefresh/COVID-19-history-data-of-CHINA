#!/usr/bin/env python
# coding: utf-8

# In[26]:


import json
import requests
import pandas as pd
from datetime import datetime, timedelta

class Scraper():
    """爬取中国疾控中心历史曲线数据"""
    def __init__(self):
        self.apiUrl = "https://2019ncov.chinacdc.cn/JKZX/yq_{}.json"
        self.header = {'Upgrade-Insecure-Requests': '1',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                       'Accept-Encoding': 'gzip, deflate, sdch',
                       'Accept-Language': 'zh-CN,zh;q=0.8',
                       'Connection': 'close'
                       }
        # 准备好的代理ip
#         self.proxy = None
        self.proxies = { "http": None, "https": None}


    def download(self,startDate, endDate):
        '''
        下载指定日期的数据
        startDate: yyyy-mm-dd
        ennDate: yyyy-mm-dd
        '''
        date = datetime.strptime(startDate, "%Y%m%d")
        end = datetime.strptime(endDate, "%Y%m%d")
        j = 0
        Data = []
        while date <= end:
            currentDate = date.strftime('%Y%m%d')
            print(currentDate)
            date = date + timedelta(days=1)
            url = self.apiUrl.format(currentDate)
#             requests.DEFAULT_RETRIES = 5
#             s = requests.session()
#             #2、关闭多余的连接
#             s.keep_alive = False

            response = requests.get(url,headers = self.header)#verify=False 2022/02/25新加，不加的时候出现SSLVerifyError
#             print(response)
#             response = requests.get(url, headers = self.header,proxies=self.proxies,timeout=(3,7),verify=False)
            city_list = json.loads(response.text)
            data = []
            for i in range(31):
                df = city_list['features'][i]['properties']
                data.append(df)
            df[j] = pd.DataFrame(data)
            df[j].drop(['OBJECTID','编码','省份','type1','type2','Shape_Length','Shape_Area'], axis=1, inplace=True)  # 删除第1第3列
            #data.to_csv('{}.csv'.format(currentDate), encoding='utf-8-sig')
            Data = pd.DataFrame(Data)
            Data = pd.concat([Data, df[j]], axis=1)
            j += 1
        Data.to_csv('Data.csv',encoding='utf-8-sig')

if __name__ == "__main__":
    spider = Scraper()
    spider.download('20220331', '20220408')


# In[ ]:




