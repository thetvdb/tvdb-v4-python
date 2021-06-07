import urllib


class Url:
    def __init__(self):
        self.base_url = "https://api4.thetvdb.com/v4"

    def login_url(self):
        return "{}/login".format(self.base_url)

    def artwork_status_url(self):
        return "{}/artwork/statuses".format(self.base_url)

    def artwork_types_url(self):
        return "{}/artwork/types".format(self.base_url)

    def artwork_url(self, id, extended=False):
        url = "{}/artwork/{}".format(self.base_url, id)
        if extended:
            url = "{}/extended".format(url)
        return url

    def awards_url(self, page):
        if page < 0:
            page = 0
        url = "{}/awards?page={}".format(self.base_url, page)
        return url

    def award_url(self, id, extended=False):
        url = "{}/awards/{}".format(self.base_url, id)
        if extended:
            url = "{}/extended".format(url)
        return url

    def awards_categories_url(self):
        url = "{}/awards/categories".format(self.base_url)
        return url

    def award_category_url(self, id, extended=False):
        url = "{}/awards/categories/{}".format(self.base_url, id)
        if extended:
            url = "{}/extended".format(url)
        return url

    def content_ratings_url(self):
        url = "{}/content/ratings".format(self.base_url)
        return url

    def countries_url(self):
        url = "{}/countries".format(self.base_url)
        return url

    def companies_url(self, page=0):
        url = "{}/companies?page={}".format(self.base_url, page)
        return url

    def company_url(self, id):
        url = "{}/companies/{}".format(self.base_url, id)
        return url

    def all_series_url(self, page=0):
        url = "{}/series".format(self.base_url)
        return url

    def series_url(self, id, extended=False):
        url = "{}/series/{}".format(self.base_url, id)
        if extended:
            url = "{}/extended".format(url)
        return url

    def movies_url(self, page=0):
        url = "{}/movies".format(self.base_url, id)
        return url

    def movie_url(self, id, extended=False):
        url = "{}/movies/{}".format(self.base_url, id)
        if extended:
            url = "{}/extended".format(url)
        return url

    def season_url(self, id, extended=False):
        url = "{}/seasons/{}".format(self.base_url, id)
        if extended:
            url = "{}/extended".format(url)
        return url

    def episode_url(self, id, extended=False):
        url = "{}/episodes/{}".format(self.base_url, id)
        if extended:
            url = "{}/extended".format(url)
        return url

    def person_url(self, id, extended=False):
        url = "{}/people/{}".format(self.base_url, id)
        if extended:
            url = "{}/extended".format(url)
        return url

    def character_url(self, id):
        url = "{}/characters/{}".format(self.base_url, id)
        return url

    def people_types_url(self, id):
        url = "{}/people/types".format(self.base_url)
        return url

    def source_types_url(self):
        url = "{}/sources/types".format(self.base_url)
        return url

    def updates_url(self, since=0):
        url = "{}/updates?since={}".format(self.base_url, since)
        return url

    def tag_options_url(self):
        url = "{}/tags/options".format(self.base_url)
        return url

    def tag_option_url(self, id):
        url = "{}/tags/options/{}".format(self.base_url, id)
        return url

    def search_url(self, query, filters):
        filters["query"] = query
        qs = urllib.urlencode(filters)
        url = "{}/search?{}".format(self.base_url, qs)
        return url
