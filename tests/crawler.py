from lotube_crawler.crawler import Crawler
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

from collections import deque


class TestCrawler(object):
    
    #def test_crawler_terms(self):
    #    c = Crawler(site='youtube', max_breadth=2, max_depth=1)
    #    c.run(['games', 'university'])
        
    def test_crawler_run(self):
        c = Crawler(site='youtube', max_breadth=2, max_depth=3)
        for video in c.run(['games']):
            print video.id_source