class Post:
    def __init__(self,
        head, link,
        author, author_link,
        submitter, submittor_link,
        pub_date):

        self.head = head
        self.link = link
        self.author = author
        self.author_link = author_link
        self.submitter = submitter
        self.submitter_link = submitter_link
        self.pub_date = pub_date


    def __str__(self):
        pass
