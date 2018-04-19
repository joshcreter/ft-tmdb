from generators.worksheets.worksheet import Worksheet


class TvEpisodeSheet(Worksheet):
    name = 'Episode'
    columns = {
        'unique_id': {'label': 'Unique ID', 'width': 15.0},
        'parent_id': {'label': 'Parent ID', 'width': 15.0},
        'title_code': {'label': 'Title Code', 'width': 15.0},
        'season_title_code': {'label': 'Season Title Code', 'width': 15.0},
        'title': {'label': 'Title', 'width': 30.0},
        'formatted_title': {'label': 'Formatted Title', 'width': 50.0},
        'type':  {'label': 'Type', 'width': 10.0},
        'season_number': {'label': 'Season No', 'width': 10.0},
        'episode_number': {'label': 'Episode Number', 'width': 15.0},
        'tmdb_id': {'label': 'TMDB ID', 'width': 15.0},
        'imdb_id': {'label': 'IMDB ID', 'width': 15.0},
        'air_date': {'label': 'Air Date', 'width': 15.0},
        'production_code': {'label': 'Production Code', 'width': 15.0},
        'synopsis': {'label': 'Synopsis', 'width': 100.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)