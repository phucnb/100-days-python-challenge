import requests

class Post:
    def __init__(self, id=None, title=None, subtitle=None, body=None):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body

    def get_posts(self):
        response = requests.get("https://api.npoint.io/6c038a85e111edd94aec")
        posts = response.json()
        posts_list = []
        for post in posts:
            posts_list.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))
        return posts_list
    
    def get_post(self, index):
        posts = self.get_posts()
        return posts[index-1]