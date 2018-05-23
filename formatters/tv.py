class TvFormatters:
    @staticmethod
    def format_tv_season_title(formatted_series_name, season_number):
        title = "{0} - Season {1:02d}".format(formatted_series_name, season_number)
        return title

    @staticmethod
    def format_tv_episode_title(project_title):
        title = ''
        return title

    @staticmethod
    def format_tv_series_title(project_title):
        title = ''
        return title

    @staticmethod
    def format_tv_season_title_code(series_imdb_id, season_number):
        return "{0}-{1:02d}".format(series_imdb_id, season_number)

    @staticmethod
    def format_tv_episode_title_code(series_imdb_id, season_number, episode_number):
        return "{0}-{1:02d}x{2:02d}".format(series_imdb_id, season_number, episode_number)

