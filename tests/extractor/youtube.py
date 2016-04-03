from lotube_crawler.extractor.youtube import Youtube
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises


class TestYoutube(object):
    
    def test_youtube_terms(self):
        y = Youtube()
        v = y.search_term('games', 1)
        print v
        
    def test_youtube_related(self):
        y = Youtube()
        v = y.search_related('EHBLFVn3sE0', 1)
        print v[0]

    #def test_init(self):
    #    a = A()
    #    assert_equal(a.value, "Some Value")
    #    assert_not_equal(a.value, "Incorrect Value")

    #def test_return_true(self):
    #    a = A()
    #    assert_equal(a.return_true(), True)
    #    assert_not_equal(a.return_true(), False)

    #def test_raise_exc(self):
    #    a = A()
    #    assert_raises(KeyError, a.raise_exc, "A value")

    #@raises(KeyError)
    #def test_raise_exc_with_decorator(self):
    #    a = A()
    #    a.raise_exc("A message")