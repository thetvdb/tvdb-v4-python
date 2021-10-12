# tvdb-v4-python
This is the official tvdb api v4 python package

### Instalation
```bash
python3 -m pip install tvdb_v4_official
```
### Getting Started
some projects require a user supplied pin as well as an apikey

```python3
from tvdb_v4_official import TVDB

tvdb = TVDB("APIKEY")
# OR:
# tvdb = TVDB("APIKEY", pin="YOUR PIN HERE")

# fetching 5 pages of series info
series_list = [tvdb.get_all_series(i) for i in range(5)]

# fetching a series so tvdb object has changed to that context
tvdb.get_series(121361)

# fetching a season's episode list
series = tvdb.get_series_extended(121361)
sorted(series["seasons"], key=lambda x: (x["type"]["name"], x["number"]))
for season_name, season_number in sorted_series:
	if season["type"]["name"] == "Aired Order" and season["number"] == 1:
		print(tvdb.get_season_extended(season["id"])["episodes"])
		break

# fetch a page of episodes from a series by season_type (type is "default" if unspecified)
info = tvdb.get_series_episodes(121361, page=0)
print(info["series"])
print(", ".join(e for e in info["episodes"]))

# fetching a movie so tvdb object has changed to that context
tvdb.get_movie(31) # avengers

# access a movie's characters
print(", ".join(c for c in tvdb.get_movie_extended(31)["characters"]))

# fetching a person record
person = tvdb.get_person_extended(characters[0]["peopleId"])
```
