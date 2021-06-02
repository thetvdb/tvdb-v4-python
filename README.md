# tvdb-v4-python
This is the official tvdb api v4 python package

### Instalation
    pip install tvdb_v4

### Getting Started
some projects require a user supplied pin as well as an apikey
    import tvdb_v4

    tvdb = tvdb_v4.Api("APIKEY") // tvdb = tvdb_v4.Api("APIKEY", pin="YOUR PIN HERE")
    // fetching a page of series
    tvdb.get_all_series(0)

    // fetching a series 
    tvdb.get_series(121361)

    // fetching a seasons episodes
    seasons = tvdb.get_series_extended(121361).seasons
    season_one = None
    for season in seasons:
        if season.number == 1:
            season_one
    episodes = tvdb.get_season_extended(season_one.id).episodes

    // fetching a movie
    tvdb.get_movie(31) // avengers

    // fetching movie's characters
    characters = tvdb.get_movie_extended(31).characters

    // fetching a person record
    person = tvdb.get_person_extended(characters[0].peopleId)

    
