from generators import WorkbookTV
from populators import CommonPopulator, ContactsPopulator, TvSeriesPopulator
from formatters import TvFormatters, CommonFormatters
from mappers import CommonMappers
from functools import reduce
import operator
from more_itertools import unique_everseen
import tmdbsimple as tmdb
import accessors.tv.season
from accessors.awards import AwardsAccessor

def process_series(self, series: tmdb.TV, workbook: WorkbookTV):
    series_imdb_id = series.external_ids()['imdb_id']

    formatted_series_name = CommonFormatters.format_project_title(series.info()['name'])

    genres = CommonMappers.map_genres(series.info()['genres'])
    origin_countries = CommonMappers.map_countries(series.info()['origin_country'])

    content_ratings = series.content_ratings()
    # rating_us = list(filter(lambda d: d['iso_3166_1'] == 'US', content_ratings['results']))[0]['rating'].\
    #     replace('TV-PG', 'PG')

    rating_us = None
    series_title_code = TvFormatters.format_tv_series_title_code(series_imdb_id)

    # awards = AwardsAccessor.get_awards(series_imdb_id)

    TvSeriesPopulator.populate_series_sheet(workbook, series, series_title_code, formatted_series_name,
                                            series_imdb_id)

    CommonPopulator.populate_localizations_sheet(workbook=workbook,
                                                 localizations=series.translations(),
                                                 title_code=series_title_code,
                                                 formatted_title=formatted_series_name)

    series_contacts_merged = []
    for season in series.info()['seasons']:
        # if season['season_number'] > 0 and season['season_number'] < 2:
        if season['season_number'] > 0:
            tv_season = self.tmdb.TV_Seasons(series_id=series.id, season_number=season['season_number'])

            episode_count = season['episode_count']
            season_contacts = accessors.tv.season.process_season(self=self,
                                                                       formatted_series_name=formatted_series_name,
                                                                       series_title_code=series_title_code,
                                                                       genres=genres,
                                                                       origin_countries=origin_countries,
                                                                       rating_us=rating_us,
                                                                       season=tv_season,
                                                                       series_id=series.id,
                                                                       series_imdb_id=series_imdb_id,
                                                                       workbook=workbook,
                                                                       episode_count=episode_count)

            series_contacts_merged.append(season_contacts)

    series_contacts = ContactsPopulator.populate_project_contacts_sheet(worksheet=workbook.get_tv_series_contacts_sheet(),
                                                                        title_code=series_title_code,
                                                                        credits=series.credits())

    series_contacts_merged.append(series_contacts)
    series_contacts_merged = reduce(operator.add, series_contacts_merged)
    series_contacts_merged = list(unique_everseen(series_contacts_merged))

    return series_contacts_merged
