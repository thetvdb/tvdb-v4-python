from json import load, dumps
from urllib import urlencode
from urllib.request import urlopen, Request


class Auth:
    def __init__(self, url, apikey, pin = ''):
        loginInfo = {"apikey": apikey}
        if pin != '':
            loginInfo["pin"] = pin

        loginInfoBytes = dumps(loginInfo, indent = 2).encode("utf-8")
        request = Request(url, data = loginInfoBytes)
        request.add_header("Content-Type", "application/json")
        with urlopen(request, data = loginInfoBytes) as response:
            self.token = load(response)["data"]["token"]

    def get_token(self):
        return self.token


class Request:
    def __init__(self, auth_token):
        self.auth_token = auth_token

    def make_request(self, url):
        request = Request(url)
        request.add_header("Authorization", f"Bearer {self.auth_token}")
        with urlopen(request) as response:
            return load(response)["data"]


class Url:
    def __init__(self):
        self.base_url = "https://api4.thetvdb.com/v4"

    def login_url(self):
        return f"{self.base_url}/login"

    def artwork_status_url(self):
        return f"{self.base_url}/artwork/statuses"

    def artwork_types_url(self):
        return f"{self.base_url}/artwork/types"

    def artwork_url(self, id, extended = False):
        return f"{url}/extended" if extended else f"{self.base_url}/artwork/{id}"

    def awards_url(self, page):
        return f"{self.base_url}/awards?page={0 if page < 0 else page}"

    def award_url(self, id, extended = False):
        return f"{url}/extended" if extended else f"{self.base_url}/awards/{id}"

    def awards_categories_url(self):
        return f"{self.base_url}/awards/categories"

    def award_category_url(self, id, extended = False):
        return f"{url}/extended" if extended else f"{self.base_url}/awards/categories/{id}"

    def content_ratings_url(self):
        return f"{self.base_url}/content/ratings"

    def countries_url(self):
        return f"{self.base_url}/countries"

    def companies_url(self, page = 0):
        return f"{self.base_url}/companies?page={page}"

    def company_url(self, id):
        return f"{self.base_url}/companies/{id}"

    def all_series_url(self, page = 0):
        return f"{self.base_url}/series"

    def series_url(self, id, extended = False):
        return f"{url}/extended" if extended else f"{self.base_url}/series/{id}"

    def movies_url(self, page = 0):
        return f"{self.base_url}/movies"

    def movie_url(self, id, extended = False):
        return f"{url}/extended" if extended else f"{self.base_url}/movies/{id}"

    def season_url(self, id, extended = False):
        return f"{url}/extended" if extended else f"{self.base_url}/seasons/{id}"

    def episode_url(self, id, extended = False):
        return f"{url}/extended" if extended else f"{self.base_url}/episodes/{id}"

    def person_url(self, id, extended = False):
        return f"{url}/extended" if extended else f"{self.base_url}/people/{id}"

    def character_url(self, id):
        return f"{self.base_url}/characters/{id}"

    def people_types_url(self, id):
        return f"{self.base_url}/people/types"

    def source_types_url(self):
        return f"{self.base_url}/sources/types"

    def updates_url(self, since = 0):
        return f"{self.base_url}/updates?since={since}"

    def tag_options_url(self):
        return f"{self.base_url}/tags/options"

    def tag_option_url(self, id):
        return f"{self.base_url}/tags/options/{id}"

    def search_url(self, query, filters):
        filters["query"] = query
        return f"{self.base_url}/search?{urlencode(filters)}"


class TVDB:
    def __init__(self, apikey: str, pin = ''):
        self.url = Url()
        login_url = self.url.login_url()
        self.auth = Auth(login_url, apikey, pin)
        auth_token = self.auth.get_token()
        self.request = Request(auth_token)

    def get_artwork_statuses(self) -> list:
        """ Returns a list of artwork statuses """
        return self.request.make_request(self.url.artwork_status_url())

    def get_artwork_types(self) -> list:
        """ Returns a list of artwork types """
        return self.request.make_request(self.url.artwork_types_url())

    def get_artwork(self, id: int) -> dict:
        """ Returns an artwork dictionary """
        return self.request.make_request(self.url.artwork_url(id))

    def get_artwork_extended(self, id: int) -> dict:
        """ Returns an artwork extended dictionary """
        return self.request.make_request(self.url.artwork_url(id, True))

    def get_all_awards(self, page = 0) -> list:
        """ Returns a list of awards """
        return self.request.make_request(self.url.awards_url(page))

    def get_award(self, id: int) -> dict:
        """ Returns an award dictionary """
        return self.request.make_request(self.url.award_url(id, False))

    def get_award_extended(self, id: int) -> dict:
        """ Returns an award extended dictionary """
        return self.request.make_request(self.url.award_url(id, True))

    def get_all_award_categories(self) -> list:
        """ Returns a list of award categories """
        return self.request.make_request(self.url.awards_categories_url())

    def get_award_category(self, id: int) -> dict:
        """ Returns an artwork category dictionary """
        return self.request.make_request(self.url.award_category_url(id, False))

    def get_award_category_extended(self, id: int) -> dict:
        """ Returns an award category extended dictionary """
        return self.request.make_request(self.url.award_category_url(id, True))

    def get_content_ratings(self) -> list:
        """ Returns a list of content ratings """
        return self.request.make_request(self.url.content_ratings_url())

    def get_countries(self) -> list:
        """ Returns a list of countries """
        return self.request.make_request(self.url.countries_url())

    def get_all_companies(self, page = 0) -> list:
        """ Returns a list of companies """
        return self.request.make_request(self.url.companies_url(page))

    def get_company(self, id: int) -> dict:
        """ Returns a company dictionary """
        return self.request.make_request(self.url.company_url(id))

    def get_all_series(self, page = 0) -> list:
        """ Returns a list of series """
        return self.request.make_request(self.url.all_series_url(page))

    def get_series(self, id: int) -> dict:
        """ Returns a series dictionary """
        return self.request.make_request(self.url.series_url(id, False))

    def get_series_extended(self, id: int) -> dict:
        """ Returns an series extended dictionary """
        url = self.url.series_url(id, True)
        print(url)
        return self.request.make_request(url)

    def get_series_translation(self, lang: str) -> dict:
        """ Returns a series translation dictionary """
        return self.request.make_request(self.url.series_translation_url(id, lang))

    def get_all_movies(self, page = 0) -> list:
        """ Returns a list of movies """
        return self.request.make_request(self.url.movies_url(page))

    def get_movie(self, id: int) -> dict:
        """ Returns a movie dictionary """
        return self.request.make_request(self.url.movie_url(id, False))

    def get_movie_extended(self, id: int) -> dict:
        """ Returns a movie extended dictionary """
        return self.request.make_request(self.url.movie_url(id, True))

    def get_movie_translation(self, lang: str) -> dict:
        """ Returns a movie translation dictionary """
        return self.request.make_request(self.url.movie_translation_url(id, lang))

    def get_season(self, id: int) -> dict:
        """ Returns a season dictionary """
        return self.request.make_request(self.url.season_url(id, False))

    def get_season_extended(self, id: int) -> dict:
        """ Returns a season extended dictionary """
        return self.request.make_request(self.url.season_url(id, True))

    def get_episode(self, id: int) -> dict:
        """ Returns an episode dictionary """
        return self.request.make_request(self.url.episode_url(id, False))

    def get_episodes_translation(self, lang: str) -> dict:
        """ Returns an episode translation dictionary """
        return self.request.make_request(self.url.episode_translation_url(id, lang))

    def get_episode_extended(self, id: int) -> dict:
        """ Returns an episode extended dictionary """
        return self.request.make_request(self.url.episode_url(id, True))

    def get_person(self, id: int) -> dict:
        """ Returns a person dictionary """
        return self.request.make_request(self.url.person_url(id, False))

    def get_person_extended(self, id: int) -> dict:
        """ Returns a person extended dictionary """
        return self.request.make_request(self.url.person_url(id, True))

    def get_character(self, id: int) -> dict:
        """ Returns a character dictionary """
        return self.request.make_request(self.url.character_url(id))

    def get_all_people_types(self) -> list:
        """ Returns a list of people types """
        return self.request.make_request(self.url.people_types_url())

    def get_all_sourcetypes(self) -> list:
        """ Returns a list of sourcetypes """
        return self.request.make_request(self.url.source_types_url())

    def get_updates(self, since: int) -> list:
        """ Returns a list of updates """
        return self.request.make_request(self.url.updates_url(since))

    def get_all_tag_options(self, page = 0) -> list:
        """ Returns a list of tag options """
        return self.request.make_request(self.url.tag_options_url(page))

    def get_tag_option(self, id: int) -> dict:
        """ Returns a tag option dictionary """
        return self.request.make_request(self.url.tag_option_url())

    def search(self, query, **kwargs) -> list:
        """ Returns a list of search results """
        return self.request.make_request(self.url.search_url(query, kwargs))
