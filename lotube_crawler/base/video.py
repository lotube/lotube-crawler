from .. import utils

class Video(object):
    
    def __init__(self):
        self.id_source = 0
        self.source = ''
        self.user = ''
        self.title = ''
        self.description = ''
        self.created_at = None
        self.modified_at = None
        self.thumbnail = {
            'url': '',
            'width': 0,
            'height': 0
        }
        self.tags = []
        self.related = []
    
    def __str__(self):
        s = 'Video {\n' + \
            'id_source: ' + str(self.id_source) + ',\n' + \
            'source: ' + str(self.source) + ',\n' + \
            'user: ' + str(self.user) + ',\n' + \
            'title: ' + utils.to_utf8(self.title) + ',\n' + \
            'description: ' + utils.to_utf8(self.description) + ',\n' + \
            'created_at: ' + str(self.created_at) + ',\n' + \
            'modified_at: ' + str(self.modified_at) + ',\n' + \
            'thumbnail: ' + str(self.thumbnail) + ',\n' + \
            'tags: ' + str(self.tags) + ',\n' + \
            'related: ' + str(self.related) + ',\n' + \
            '}'
        return s
