class Post(object):

    def __init__(self, id: int = 0, title: str = '', body: str = '', userId: int = 0):
        self.id = id
        self.title = title
        self.body = body
        self.user_id = userId

    def __str__(self):
        text = "id: %s, title: %s, body: %s, userId: %s" % (self.id, self.title, self.body, self.user_id)
        return text
