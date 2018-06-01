from generators import WorkbookTV
from populators import CommonPopulator, ContactsPopulator, TvSeriesPopulator
from formatters import TvFormatters, CommonFormatters
from mappers import CommonMappers, CountryMapper
from functools import reduce
import operator
from more_itertools import unique_everseen
import tmdbsimple as tmdb
import accessors.tv.season
# from accessors.awards import AwardsAccessor


def process_series(self, series: tmdb.TV, workbook: WorkbookTV):

    series_imdb_id = series.external_ids()['imdb_id']
    series_title_code = TvFormatters.format_tv_series_title_code(series_imdb_id)
    raw_series_name = series.info()['name']
    formatted_series_name = CommonFormatters.format_project_title(raw_series_name)
    genres = CommonMappers.map_genres(series.info()['genres'])
    origin_countries = CountryMapper.map_countries(series.info()['origin_country'])
    production_status = CommonMappers.map_production_status(series.info()['status'])
    episode_run_time = series.info()['episode_run_time'][0]
    original_language = CommonFormatters.format_language(series.info()['original_language'])
    languages = CommonFormatters.format_languages(series.info()['languages'])
    certifications = CommonMappers.map_tv_content_ratings(series.content_ratings()['results'])
    homepage = series.info()['homepage']
    series_overview = series.info()['overview']
    series_title_aka1, series_title_aka2 = TvFormatters.get_series_title_aka_1_and_2(series)

    # Below here is faked data
    episode_run_time_adjusted = 30 if episode_run_time <= 30 else 60
    year_completed = CommonFormatters.format_date_year_only(series.info()['last_air_date'])
    languages_subtitles = languages
    average_episodes_per_season = round(series.info()['number_of_episodes']/series.info()['number_of_seasons'])
    budget = episode_run_time * 70000 * average_episodes_per_season
    budget_currency = "USD"
    original_format = 'HD' if int(year_completed) > 2010 else 'SD'
    copyright_holder = series.info()['production_companies'][0]['name']
    copyright_year = year_completed if int(year_completed) > 1990 else 2018


    # awards = AwardsAccessor.get_awards(series_imdb_id)

    TvSeriesPopulator.populate_series_sheet(workbook=workbook,
                                            title_code=series_title_code,
                                            series_title_formatted=formatted_series_name,
                                            raw_title=raw_series_name,
                                            imdb_id=series_imdb_id,
                                            production_status=production_status,
                                            episode_run_time=episode_run_time,
                                            episode_run_time_adjusted=episode_run_time_adjusted,
                                            year_completed=year_completed,
                                            original_language=original_language,
                                            budget=budget,
                                            budget_currency=budget_currency,
                                            homepage=homepage,
                                            original_format=original_format,
                                            copyright_holder=copyright_holder,
                                            copyright_year=copyright_year,
                                            series_overview=series_overview,
                                            series_title_aka1=series_title_aka1,
                                            series_title_aka2=series_title_aka2

                                            )

    CommonPopulator.populate_localizations_sheet(workbook=workbook,
                                                 localizations=series.translations(),
                                                 title_code=series_title_code,
                                                 formatted_title=formatted_series_name)

    CommonPopulator.populate_genres_sheet(workbook, series_title_code, genres)
    CommonPopulator.populate_countries_of_origin_sheet(workbook, series_title_code, origin_countries)

    CommonPopulator.populate_languages_sheet(worksheet=workbook.get_languages_sheet(),
                                             title_code=series_title_code,
                                             languages=languages)

    CommonPopulator.populate_subtitles_sheet(worksheet=workbook.get_subtitles_sheet(),
                                             title_code=series_title_code,
                                             languages=languages_subtitles)

    CommonPopulator.populate_ratings_sheet(worksheet=workbook.get_ratings_sheet(),
                                           title_code=series_title_code,
                                           certifications=certifications)

    CommonPopulator.populate_project_groups_sheet(workbook, series_title_code)
    CommonPopulator.populate_applications_sheet(workbook, series_title_code)

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
                                                                 season=tv_season,
                                                                 series_id=series.id,
                                                                 series_imdb_id=series_imdb_id,
                                                                 workbook=workbook,
                                                                 episode_count=episode_count)

            series_contacts_merged.append(season_contacts)

    series_contacts = ContactsPopulator.populate_project_contacts_sheet(
        worksheet=workbook.get_tv_series_contacts_sheet(),
        title_code=series_title_code,
        credits=series.credits())

    series_contacts_merged.append(series_contacts)
    series_contacts_merged = reduce(operator.add, series_contacts_merged)
    series_contacts_merged = list(unique_everseen(series_contacts_merged))

    return series_contacts_merged
