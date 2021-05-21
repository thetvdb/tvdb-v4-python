from auth.auth_provider import Auth
from request.request import Request
from url.url_provider import Url


class Api:
    def __init__(self, apikey, pin=""):
        self.url = Url()
        login_url = self.url.login_url()
        self.auth = Auth(login_url, apikey, pin)
        auth_token = self.auth.get_token()
        self.request = Request(auth_token)

    def get_artwork_statuses(self) -> list:
        url = self.url.artwork_status_url()
        return self.request.make_request(url)

    def get_artwork_types(self) -> list:
        url = self.url.artwork_types_url()
        return self.request.make_request(url)

    def get_artwork(self, id):
        url = self.url.artwork_url(id)
        return self.request.make_request(url)

    def get_artwork_extended(self, id):
        url = self.url.artwork_url(id, True)
        return self.request.make_request(url)

    def get_all_awards(self, page=0):
        url = self.url.awards_url(page)
        return self.request.make_request(url)

    def get_award(self, id):
        url = self.url.award_url(id, False)
        return self.request.make_request(url)

    def get_award_extended(self, id):
        url = self.url.award_url(id, True)
        return self.request.make_request(url)

    def get_all_award_categories(self):
        url = self.url.awards_categories_url()
        return self.request.make_request(url)

    def get_award_category(self, id):
        url = self.url.award_category_url(id, False)
        return self.request.make_request(url)

    def get_award_category_extended(self, id):
        url = self.url.award_category_url(id, True)
        return self.request.make_request(url)

    def get_content_ratings(self):
        url = self.url.content_ratings_url()
        return self.request.make_request(url)

    def get_countries(self):
        url = self.url.countries_url()
        return self.request.make_request(url)

    def get_all_companies(self, page=0):
        url = self.url.companies_url(page)
        return self.request.make_request(url)

    def get_company(self, id=0):
        url = self.url.company_url(id)
        return self.request.make_request(url)

    def get_all_series(self, page=0):
        url = self.url.all_series_url(page)
        return self.request.make_request(url)

    def get_series(self, id=0):
        url = self.url.series_url(id, False)
        return self.request.make_request(url)

    def get_series_extended(self, id=0):
        url = self.url.series_url(id, True)
        return self.request.make_request(url)

    def get_all_movies(self, page=0):
        url = self.url.movies_url(page)
        return self.request.make_request(url)

    def get_movie(self, id=0):
        url = self.url.movie_url(id, False)
        return self.request.make_request(url)

    def get_movie_extended(self, id=0):
        url = self.url.movie_url(id, True)
        return self.request.make_request(url)

    def get_season(self, id=0):
        url = self.url.season_url(id, False)
        return self.request.make_request(url)

    def get_season_extended(self, id=0):
        url = self.season_url(id, True)
        return self.request.make_request(url)

    def get_episode(self, id=0):
        url = self.url.episode_url(id, False)
        return self.request.make_request(url)

    def get_episode_extended(self, id=0):
        url = self.url.episode_url(id, True)
        return self.request.make_request(url)

    def get_person(self, id=0):
        url = self.url.person_url(id, False)
        return self.request.make_request(url)

    def get_person_extended(self, id=0):
        url = self.url.person_url(id, True)
        return self.request.make_request(url)

    def get_character(self, id=0):
        url = self.url.character_url(id)
        return self.request.make_request(url)

    def get_all_people_types(self):
        url = self.url.people_types_url()
        return self.request.make_request(url)

    def get_all_sourcetypes(self):
        url = self.url.source_types_url()
        return self.request.make_request(url)

    def get_updates(self, since=0):
        url = self.url.updates_url(since)
        return self.request.make_request(url)

    def get_all_tag_options(self, page=0):
        url = self.url.tag_options_url(page)
        return self.request.make_request(url)

    def get_tag_option(self, id=0):
        url = self.url.tag_option_url()
        return self.request.make_request(url)
