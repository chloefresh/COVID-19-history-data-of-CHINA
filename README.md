# COVID-2019-situation-reports
This project consists of the COVID-2019 confirmed,suspected and dead cases of 31-situations in China mainland.  

The dataset is crawled from the website of Chinese CDC http://2019ncov.chinacdc.cn/2019-nCoV/ and is updated from 2020-01-16 to now.


本项目可以crawl中国31个省和直辖市的每日新冠肺炎**新增确诊**、**疑似**和**死亡**病例，和**累计**病例。爬取网站为中国疾控中心建立的新冠肺炎实时平台。


项目的**初衷**是丁香园来源的数据不含疑似病例，该项目填补了这一空白，且数据具有一定的权威性。由于本人代码水平有限，一些功能的实现并不尽人意，所以，欢迎大家修改补充，非常乐意和大家交流！

## Including Some Data Files(.csv)

| cum_confirmed.csv | 累计确诊病例  |
|------|----------------|
| cum_suspected.csv  | 累计疑似病例  |
| cum_dead.csv   | 累计死亡病例  |
| new_confirmed.csv | 新增确诊病例  |
| new_suspected.csv   | 新增疑似病例  |
| new_dead.csv  | 新增死亡病例  |

## A Spider Wrote With Python3
`main.py` is the spider, you can set your own time range just by updating the following codes:

```

if __name__ == "__main__":  

    spider = Scraper()

    spider.download('20200116', '20200304') # set the crawling date range
    
 ```
 And the data is stored in `Data2.csv`
## Data Processing 

The data processing is wrote in `data_processing.ipynb`, you can get the above data csv files by running this ipynb.
