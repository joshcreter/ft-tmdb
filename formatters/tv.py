class TvFormatters:
    @staticmethod
    def format_tv_season_title(project_title):
        title = ''
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
    def format_tv_episode_title_code(series_imdb_id, season_number, episode_number):
        return "{0}-{1:02d}x{2:02d}".format(series_imdb_id, season_number, episode_number)

