import re
import requests
import json

from ..base.abstracts import Extractor
from ..base.video import Video


class Youtube(Extractor):
    results = []
    _next_page = ''
    
    def __init__(self, token):
        super(self.__class__, self).__init__(token)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.results = None
        
    def _abstract_search(self, term, request, max_results):
        req = request(term, max_results)
        results = []
        for element in req['items']:
            video = Video()
            video.id_source = element['id']['videoId']
            video.source = 'youtube'
            video.user = self._channel_name(element['snippet']['channelId'])
            video.title = element['snippet']['title']
            video.description = element['snippet']['description']
            video.created_at = element['snippet']['publishedAt']
            video.thumbnail = {
                'url': element['snippet']['thumbnails']['high']['url'],
                'width': element['snippet']['thumbnails']['high']['width'],
                'height': element['snippet']['thumbnails']['high']['height']
            }
            video.tags = self._tags(element['snippet']['title'])
            results.append(video)
        return results
        
    def _request_video_by_term(self, term, max_results):
        url = 'https://www.googleapis.com/youtube/v3/search?part=snippet%20&q='\
              + term +'&type=video%20&videoCaption=closedCaption&key=' \
              + self.token +'&maxResults=' + str(max_results)
        resp = requests.get(url)
        return json.loads(resp.text)
        
    def _request_video_by_id(self, id_video, max_results):
        url = 'https://www.googleapis.com/youtube/v3/search?part=snippet' \
            + '&relatedToVideoId=' + id_video + '&type=video&key=' + self.token\
            + '&maxResults=' + str(max_results)
        resp = requests.get(url)
        return json.loads(resp.text)
    
    def search_term(self, term, max_results=50):
        return self._abstract_search(term, self._request_video_by_term,
                                     max_results)
        
    def search_related(self, id_video, max_results=50):
        return self._abstract_search(id_video, self._request_video_by_id,
                                     max_results)

    def _channel_name(self, channel_id):
        url = 'https://www.googleapis.com/youtube/v3/channels?key=' + \
              self.token + '&id=' + channel_id + '&part=snippet'
        resp = requests.get(url)
        text = json.loads(resp.text)
        return text['items'][0]['snippet']['title']
    
    def _tags(self, words_str):
        words = re.sub(r'[^a-zA-Z0-9 ]+', '', words_str).split(' ')
        return [tag for tag in words if len(tag) >= 3] or words
        
if __name__ == '__main__':
    youtube = Youtube()
    results = youtube.search_term('delete from', 1)
    print results
