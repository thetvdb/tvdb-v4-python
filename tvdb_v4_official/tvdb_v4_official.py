from auth.auth import Auth
from request.request import Request
from url.url import Url


class TVDB:
    def __init__(self, apikey: str, pin=""):
        self.url = Url()
        login_url = self.url.login_url()
        self.auth = Auth(login_url, apikey, pin)
        auth_token = self.auth.get_token()
        self.request = Request(auth_token)

    def get_artwork_statuses(self) -> list:
        """Returns a list of artwork statuses"""
        url = self.url.artwork_status_url()
        return self.request.make_request(url)

    def get_artwork_types(self) -> list:
        """Returns a list of artwork types"""
        url = self.url.artwork_types_url()
        return self.request.make_request(url)

    def get_artwork(self, id: int) -> dict:
        """Returns an artwork dictionary"""
        url = self.url.artwork_url(id)
        return self.request.make_request(url)

    def get_artwork_extended(self, id: int) -> dict:
        """Returns an artwork extended dictionary"""
        url = self.url.artwork_url(id, True)
        return self.request.make_request(url)

    def get_all_awards(self, page=0) -> list:
        """Returns a list of awards"""
        url = self.url.awards_url(page)
        return self.request.make_request(url)

    def get_award(self, id: int) -> dict:
        """Returns an award dictionary"""
        url = self.url.award_url(id, False)
        return self.request.make_request(url)

    def get_award_extended(self, id: int) -> dict:
        """Returns an award extended dictionary"""
        url = self.url.award_url(id, True)
        return self.request.make_request(url)

    def get_all_award_categories(self) -> list:
        """Returns a list of award categories"""
        url = self.url.awards_categories_url()
        return self.request.make_request(url)

    def get_award_category(self, id: int) -> dict:
        """Returns an artwork category dictionary"""
        url = self.url.award_category_url(id, False)
        return self.request.make_request(url)

    def get_award_category_extended(self, id: int) -> dict:
        """Returns an award category extended dictionary"""
        url = self.url.award_category_url(id, True)
        return self.request.make_request(url)

    def get_content_ratings(self) -> list:
        """Returns a list of content ratings"""
        url = self.url.content_ratings_url()
        return self.request.make_request(url)

    def get_countries(self) -> list:
        """Returns a list of countries"""
        url = self.url.countries_url()
        return self.request.make_request(url)

    def get_all_companies(self, page=0) -> list:
        """Returns a list of companies"""
        url = self.url.companies_url(page)
        return self.request.make_request(url)

    def get_company(self, id: int) -> dict:
        """Returns a company dictionary"""
        url = self.url.company_url(id)
        return self.request.make_request(url)

    def get_all_series(self, page=0) -> list:
        """Returns a list of series"""
        url = self.url.all_series_url(page)
        return self.request.make_request(url)

    def get_series(self, id: int) -> dict:
        """Returns a series dictionary"""
        url = self.url.series_url(id, False)
        return self.request.make_request(url)

    def get_series_extended(self, id: int) -> dict:
        """Returns an series extended dictionary"""
        url = self.url.series_url(id, True)
        print(url)
        return self.request.make_request(url)

    def get_series_translation(self, lang: str) -> dict:
        """Returns a series translation dictionary"""
        url = self.url.series_translation_url(id, lang)
        return self.request.make_request(url)

    def get_all_movies(self, page=0) -> list:
        """Returns a list of movies"""
        url = self.url.movies_url(page)
        return self.request.make_request(url)

    def get_movie(self, id: int) -> dict:
        """Returns a movie dictionary"""
        url = self.url.movie_url(id, False)
        return self.request.make_request(url)

    def get_movie_extended(self, id: int) -> dict:
        """Returns a movie extended dictionary"""
        url = self.url.movie_url(id, True)
        return self.request.make_request(url)

    def get_movie_translation(self, lang: str) -> dict:
        """Returns a movie translation dictionary"""
        url = self.url.movie_translation_url(id, lang)
        return self.request.make_request(url)

    def get_season(self, id: int) -> dict:
        """Returns a season dictionary"""
        url = self.url.season_url(id, False)
        return self.request.make_request(url)

    def get_season_extended(self, id: int) -> dict:
        """Returns a season extended dictionary"""
        url = self.url.season_url(id, True)
        return self.request.make_request(url)

    def get_episode(self, id: int) -> dict:
        """Returns an episode dictionary"""
        url = self.url.episode_url(id, False)
        return self.request.make_request(url)

    def get_episodes_translation(self, lang: str) -> dict:
        """Returns an episode translation dictionary"""
        url = self.url.episode_translation_url(id, lang)
        return self.request.make_request(url)

    def get_episode_extended(self, id: int) -> dict:
        """Returns an episode extended dictionary"""
        url = self.url.episode_url(id, True)
        return self.request.make_request(url)

    def get_person(self, id: int) -> dict:
        """Returns a person dictionary"""
        url = self.url.person_url(id, False)
        return self.request.make_request(url)

    def get_person_extended(self, id: int) -> dict:
        """Returns a person extended dictionary"""
        url = self.url.person_url(id, True)
        return self.request.make_request(url)

    def get_character(self, id: int) -> dict:
        """Returns a character dictionary"""
        url = self.url.character_url(id)
        return self.request.make_request(url)

    def get_all_people_types(self) -> list:
        """Returns a list of people types"""
        url = self.url.people_types_url()
        return self.request.make_request(url)

    def get_all_sourcetypes(self) -> list:
        """Returns a list of sourcetypes"""
        url = self.url.source_types_url()
        return self.request.make_request(url)

    def get_updates(self, since: int) -> list:
        """Returns a list of updates"""
        url = self.url.updates_url(since)
        return self.request.make_request(url)

    def get_all_tag_options(self, page=0) -> list:
        """Returns a list of tag options"""
        url = self.url.tag_options_url(page)
        return self.request.make_request(url)

    def get_tag_option(self, id: int) -> dict:
        """Returns a tag option dictionary"""
        url = self.url.tag_option_url()
        return self.request.make_request(url)

    def search(self, query, **kwargs) -> list:
        """Returns a list of search results"""
        url = self.url.search_url(query, kwargs)
        return self.request.make_request(url)
