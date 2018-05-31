from generators import WorkbookTV
from formatters import TvFormatters
from populators import CommonPopulator, ContactsPopulator, TvEpisodePopulator

import tmdbsimple as tmdb


def process_episode(self, episode_number: int, formatted_series_name: str, season_title_code: str,
                    genres, origin_countries, rating_us: str, season_number: int,
                    series_id: str, series_imdb_id: str, workbook: WorkbookTV):

    episode = self.tmdb.TV_Episodes(series_id=series_id, season_number=season_number, episode_number=episode_number)

    print("{0:02d}x{1:02d}: {2}".format(season_number, episode_number, episode.info()['name']))

    title_code = TvFormatters.format_tv_episode_title_code(series_imdb_id, season_number, episode_number)

    TvEpisodePopulator.populate_episode_sheet(workbook, title_code, season_title_code, season_number,
                                              episode_number, episode, formatted_series_name)
    # ContactsPopulator.populate_project_contacts_sheet(workbook, title_code, episode.credits())
    CommonPopulator.populate_ratings_sheet(workbook, title_code, rating_us)
    CommonPopulator.populate_genres_sheet(workbook, title_code, genres)
    CommonPopulator.populate_countries_of_origin_sheet(workbook, title_code, origin_countries)
    CommonPopulator.populate_applications_sheet(workbook, title_code)
    contacts = ContactsPopulator.populate_project_contacts_sheet(worksheet=workbook.get_tv_episode_contacts_sheet(),
                                                                 title_code=title_code,
                                                                 credits=episode.credits())

    return contacts

