import tmdbsimple as tmdb


class TvFormatters:
    @staticmethod
    def format_tv_season_title(formatted_series_name: str, season_number: int):
        title = "{0} - Season {1:02d}".format(formatted_series_name, season_number)
        # title = "{0} - Season {1}".format(formatted_series_name, season_number)

        return title

    @staticmethod
    def format_tv_episode_title(series_title_formatted: str, season_number: int, episode_number: int):
        abnormal1 = [

        ]

        abnormal2 = [

        ]

        abnormal3 = [

        ]

        if series_title_formatted in abnormal1:
            formatted_title = "{0} - Season {1:02d} - Ep.{2:02d}".format(series_title_formatted,
                                                                         season_number,
                                                                         episode_number)

        elif series_title_formatted in abnormal2:
            formatted_title = "{0} - Season {1} - Ep. {2}".format(series_title_formatted,
                                                                  season_number,
                                                                  episode_number)

        elif series_title_formatted in abnormal3:
            formatted_title = "{0} - Season {1:02d} - Ep.{2}".format(series_title_formatted,
                                                                     season_number,
                                                                     episode_number)

        else:
            formatted_title = "{0} - Season {1:02d} - Ep. {2:02d}".format(series_title_formatted,
                                                                          season_number,
                                                                          episode_number)

        return formatted_title

    @staticmethod
    def format_tv_series_title(project_title):
        title = ''
        return title

    @staticmethod
    def format_tv_series_title_code(series_imdb_id):
        return format(series_imdb_id).replace("tt", "")

    @staticmethod
    def format_tv_season_title_code(series_imdb_id, season_number):
        return "{0}-{1:02d}".format(TvFormatters.format_tv_series_title_code(series_imdb_id), season_number)

    @staticmethod
    def format_tv_episode_title_code(series_imdb_id, season_number, episode_number):
        return "{0}-{1:02d}x{2:02d}".format(TvFormatters.format_tv_series_title_code(series_imdb_id), season_number, episode_number)

    @staticmethod
    def get_series_title_aka_1_and_2(series: tmdb.TV) -> [str, str]:
        alternative_titles = series.alternative_titles()['results']

        if len(alternative_titles) >= 2:
            us_titles = list(filter(lambda d: d['iso_3166_1'] == 'US', alternative_titles))

            if len(us_titles) >= 2:
                return[us_titles[0]['title'], us_titles[1]['title']]

            elif len(us_titles) == 1:
                first_not_us_title = list(filter(lambda d: d['iso_3166_1'] != 'US', alternative_titles))[0]['title']
                return[us_titles[0]['title'], first_not_us_title]

            else:
                return [(alternative_titles[0]['title']), alternative_titles[1]['title']]

        elif len(alternative_titles) == 1:
            return [(alternative_titles[0]['title']), '']

        else:
            return ['', '']

    @staticmethod
    def get_series_copyright_holder(series: tmdb.TV) -> str:
        try:
            return series.info()['production_companies'][0]['name']
        except IndexError:
            return ''

    @staticmethod
    def get_episode_run_time(series: tmdb.TV) -> int:
        try:
            return series.info()['episode_run_time'][0]
        except IndexError:
            # This is a total guess
            return 25

