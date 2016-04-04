from collections import deque


class Crawler:
    """
    BFS based video crawler
    """
    
    def __init__(self, site, site_token=None, max_breadth=2, max_depth=1000):
        self.extractor = self._get_extractor_class(site)
        self.max_breadth = max_breadth
        self.max_depth = max_depth
        self.site_token = site_token

        self.ids = deque()
        self.ids_hash = set()
 
    def run(self, terms):
        # first lookup will be by terms
        for video in self._run_terms(terms):
            yield video
        
        # consequent lookups will be by ids
        for video in self._run_related():
            yield video
    
    def _new_extractor_instance(self):
        return self.extractor(token=self.site_token)
    
    def _get_extractor_class(self, site):
        site = site.lower()
        
        import importlib
        module = importlib.import_module('lotube_crawler.extractor.' + site)
        class_ = getattr(module, site.title())
        return class_
        
    def _run_terms(self, terms):
        for term in terms:
            with self._new_extractor_instance() as ext:
                res = ext.search_term(term, self.max_breadth)
                for video in res:
                    self.ids.append((video.id_source, 0))
                    self.ids_hash.add(video.id_source)
                    yield video
    
    def _run_related(self):
        expanded = set()
        while self.ids:
            video = self.ids.popleft()
            id_video = video[0]
            depth = video[1]
            if depth >= self.max_depth:
                break
            with self._new_extractor_instance() as ext:
                res = ext.search_related(id_video, self.max_breadth)
                selected_videos = filter(lambda x: x.id_source not in expanded and
                                         x.id_source not in self.ids_hash, res)
                for video in selected_videos:
                    self.ids.append((video.id_source, depth + 1))
                    self.ids_hash.add(video.id_source)
                    yield video
            expanded.add(id_video)
