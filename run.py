from crawler import Crawler

try:
    crawler = Crawler()
    crawler.run();
except Exception as e:
    print(e)