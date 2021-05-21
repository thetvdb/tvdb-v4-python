
base_url = "http://localhost:8081/v4"


class Url_provider:
    def __init__(self):
        self.base_url = base_url

    def get_login_url(self):
        url = "{}/login".format(self.base_url)
        return url

    def get_artwork_status_url(self):
        url = "{}/artworks/statuses".format(self.base_url)
