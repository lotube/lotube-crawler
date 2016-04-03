class Extractor(object):
    
    def __init__(self, token):
        self.token = token
    
    def search_term(self, term, maxResults=50):
        """
        Abstract method.
        """
        raise NotImplementedError('Not implemented')
        
    def search_related(self, id_video, maxResults=50):
        """
        Abstract method.
        """
        raise NotImplementedError('Not implemented')
    