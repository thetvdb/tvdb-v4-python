from .auth import Auth
from .url import url_provider


class Tvdb:
    def __init__(self, apikey, pin=""):
        self.auth = Auth(apikey, pin)

    def getArtworkStatuses():

    def getArtworkTypes():

    def getArtwork(id):

    def getArtworkExtended(id):

    def getAllAwards(page=0):

    def getAward(id):

    def getAwardExtended(id):

    def getAwardCategories(id):

    def getAwardCategoriesExtended(id):

    def getContentRatings():

    def getCountries():

    def getAllCompanies(page=0):

    def getCompany(id):

    def getAllSeries(page=0):

    def getSeries(id):

    def getSeriesExtended(id, translations=False):

    def getAllMovies(page=0):

    def getMovie(id):

    def getMovieExtended(id):

    def getSeason(id):

    def getSeasonExtended(id):

    def getEpisode(id):

    def getEpisodeExtended(id):

    def getPerson(id):

    def getPersonExtended(id):

    def getCharacter(id):

    def getAllPeopleTypes():

    def getAllSourceTypes():

    def getUpdates(since=0):

    def getAllTagOptions(page=0):

    def getTagOption(id):
