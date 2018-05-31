from generators import WorkbookTV
from populators import ContactsPopulator, TvSeasonPopulator
from formatters import TvFormatters
from functools import reduce
import operator
from more_itertools import unique_everseen
import tmdbsimple as tmdb
import accessors.processors.episode


def process_season(self, formatted_series_name: str, series_title_code: str, genres,
                   origin_countries, rating_us: str, season: tmdb.TV_Seasons,
                   episode_count: int,
                   series_id: str, series_imdb_id: str, workbook: WorkbookTV):
    season_number = season.season_number
    formatted_season_name = TvFormatters.format_tv_season_title(formatted_series_name, season_number)
    season_title_code = TvFormatters.format_tv_season_title_code(series_imdb_id, season_number)

    TvSeasonPopulator.populate_season_sheet(workbook=workbook,
                                            title_code=season_title_code,
                                            series_title_code=series_title_code,
                                            season_title_formatted=formatted_season_name)

    season_contacts_merged = []

    # for episode_number in range(1, 2):
    for episode_number in range(1, episode_count + 1):
        episode_contacts = accessors.processors.episode.process_episode(self=self,
                                                                        episode_number=episode_number,
                                                                        formatted_series_name=formatted_series_name,
                                                                        season_title_code=season_title_code,
                                                                        genres=genres,
                                                                        origin_countries=origin_countries,
                                                                        rating_us=rating_us,
                                                                        season_number=season_number,
                                                                        series_id=series_id,
                                                                        series_imdb_id=series_imdb_id,
                                                                        workbook=workbook)
        season_contacts_merged.append(episode_contacts)

    season_contacts = ContactsPopulator.populate_project_contacts_sheet(worksheet=workbook.get_tv_season_contacts_sheet(),
                                                                        title_code=season_title_code,
                                                                        credits=season.credits())

    season_contacts_merged.append(season_contacts)
    season_contacts_merged = reduce(operator.add, season_contacts_merged)
    season_contacts_merged = list(unique_everseen(season_contacts_merged))

    return season_contacts_merged

