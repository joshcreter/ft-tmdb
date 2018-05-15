from generators.worksheets.worksheet import Worksheet


class TvEpisodeSheet(Worksheet):
    name = 'Episode'
    columns = {
        'unique_id': {'label': 'Unique ID', 'width': 15.0},
        'parent_id': {'label': 'Parent ID', 'width': 30.0},
        'title_code': {'label': 'TitleCode', 'width': 15.0},
        'season_title_code': {'label': 'Season Title Code', 'width': 15.0},
        'title': {'label': 'Title', 'width': 30.0},
        'logline': {'label': 'Logline', 'width': 30.0},
        'type':  {'label': 'ProjectType', 'width': 10.0},
        'season_number': {'label': 'SeasonNo', 'width': 10.0},
        'episode_number': {'label': 'EpisodeNumber', 'width': 15.0},
        'tmdb_id': {'label': 'TMDB ID', 'width': 15.0},
        'imdb_id': {'label': 'ImdbId', 'width': 15.0},
        'air_date': {'label': 'OriginalAirDate', 'width': 15.0},
        'production_code': {'label': 'ProductionCode', 'width': 15.0},
        'synopsis': {'label': 'ShortSynopsis', 'width': 100.0}
    }

    def __init__(self, workbook):
        super().__init__(workbook)