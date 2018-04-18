from generators.worksheets.worksheet import Worksheet


class TvEpisodeSheet(Worksheet):
    name = 'Episode'
    columns = {
        # Start from the first cell. Rows and columns are zero indexed.
        'title_code': {'position': 0, 'label': 'Title Code', 'width': 15.0},
        'season_title_code': {'position': 1, 'label': 'Season Title Code', 'width': 15.0},
        'title': {'position': 2, 'label': 'Title', 'width': 30.0},
        'formatted_title': {'position': 3, 'label': 'Formatted Title', 'width': 50.0},
        'type':  {'position': 4, 'label': 'Type', 'width': 10.0},
        'season_number': {'position': 5, 'label': 'Season No', 'width': 10.0},
        'episode_number': {'position': 6, 'label': 'Episode Number', 'width': 15.0},
        'tmdb_id': {'position': 7, 'label': 'TMDB ID', 'width': 15.0},
        'imdb_id': {'position': 8, 'label': 'IMDB ID', 'width': 15.0},
        'air_date': {'position': 9, 'label': 'Air Date', 'width': 15.0},
        'production_code': {'position': 10, 'label': 'Production Code', 'width': 15.0},
        'synopsis': {'position': 11, 'label': 'Synopsis', 'width': 100.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)