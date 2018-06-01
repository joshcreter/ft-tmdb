from generators import *


class CommonPopulator:
    @staticmethod
    def populate_applications_sheet(workbook, title_code: str):
        worksheet = workbook.get_application_sheet().get_worksheet()

        applications = ['Avails', 'BizAffairs', 'InvenTrack']
        for application in applications:
            dataset = {
                'title_code': title_code,
                'application': application
            }
            worksheet.write_data_row(dataset)

    @staticmethod
    def populate_project_groups_sheet(workbook, title_code: str):
        worksheet = workbook.get_project_groups_sheet().get_worksheet()

        project_groups = ['Demo Titles']
        for project_group in project_groups:
            dataset = {
                'title_code': title_code,
                'project_group': project_group
            }
            worksheet.write_data_row(dataset)

    @staticmethod
    def populate_ratings_sheet(worksheet: RatingsSheet, title_code: str, certifications: {}):
        for certification in certifications:
            dataset = {
                'title_code': title_code,
                'authority': certification['authority'],
                'rating': certification['rating']
            }
            worksheet.write_data_row(dataset)

    @staticmethod
    def populate_ratings_sheet_US_only(workbook, title_code: str, rating_US: str):
        worksheet_ratings = workbook.get_ratings_sheet().get_worksheet()
        ratings_dataset = {
            'title_code': title_code,
            'authority': 'MPAA',
            'rating': rating_US
        }
        worksheet_ratings.write_data_row(ratings_dataset)

    @staticmethod
    def populate_genres_sheet(workbook, title_code: str, genres: [str]):
        worksheet_genre = workbook.get_genre_sheet().get_worksheet()
        for genre in genres:
            genre_dataset = {
                'title_code': title_code,
                'genre': genre
            }
            worksheet_genre.write_data_row(genre_dataset)

    @staticmethod
    def populate_countries_of_origin_sheet(workbook, title_code: str, countries: [str]):
        worksheet = workbook.get_countries_of_origin_sheet().get_worksheet()
        for country in countries:
            dataset = {
                'title_code': title_code,
                'country': country
            }
            worksheet.write_data_row(dataset)

    @staticmethod
    def populate_localizations_sheet(workbook, title_code, localizations, formatted_title: str):
        worksheet = workbook.get_localizations_sheet().get_worksheet()

        allowed_localization_codes = ['af', 'ar', 'az', 'be', 'bg', 'ca', 'cs', 'da', 'de', 'div', 'el', 'es', 'et',
                                      'eu', 'fa', 'fi', 'fil', 'fo', 'fr', 'gl', 'gu', 'he', 'hi', 'hr', 'hu', 'hy',
                                      'id', 'is', 'it', 'ja', 'ka', 'kk', 'kn', 'ko', 'kok', 'ky', 'lt', 'lv', 'mk',
                                      'mn', 'mr', 'ms', 'nl', 'no', 'pa', 'pl', 'pt', 'ro', 'ru', 'sa', 'sk', 'sl',
                                      'sq', 'sv', 'sw', 'syr', 'ta', 'te', 'th', 'tr', 'tt', 'uk', 'ur', 'uz', 'vi']

        for localization in localizations['translations']:
            if localization['iso_639_1'] in allowed_localization_codes:
                if len(localization['data']['overview']) > 0:

                    title = formatted_title
                    if len(localization['data'].get('title', '')) > 0:
                        title = localization['data']['title']
                    elif len(localization['data'].get('name', '')) > 0:
                        title = localization['data']['name']

                    dataset = {
                        'title_code': title_code,
                        'culture': localization['iso_639_1'],
                        'title': title,
                        'synopsis': localization['data']['overview']
                    }
                    worksheet.write_data_row(dataset)


    @staticmethod
    def populate_timeline_sheet(workbook, title_code: str, release_dates: {}):
        worksheet = workbook.get_timeline_sheet().get_worksheet()

        for release_date in release_dates:
            dataset = {
                'title_code': title_code,
                'territory': release_date['territory'],
                'start_date': release_date['start_date'],
                'type': release_date['type'],
                'note': release_date['note'],
                'media': release_date['media'],
            }
            worksheet.write_data_row(dataset)

    @staticmethod
    def populate_awards_sheet(workbook, title_code: str, awards: {}):
        worksheet = workbook.get_awards_sheet().get_worksheet()

        for award in awards:
            dataset = {
                'title_code': title_code,
                'result': award['result'],
                'year': award['year'],
                'organization': award['organization'],
                'trophy': award['trophy'],
                'category': award['category'],
            }
            worksheet.write_data_row(dataset)

    @staticmethod
    def populate_languages_sheet(worksheet: LanguagesSheet, title_code: str, languages: [str]):
        for language in languages:
            dataset = {
                'title_code': title_code,
                'language': language,
            }
            worksheet.write_data_row(dataset)

    @staticmethod
    def populate_subtitles_sheet(worksheet: SubtitlesSheet, title_code: str, languages: [str]):
        for language in languages:
            dataset = {
                'title_code': title_code,
                'language': language,
            }
            worksheet.write_data_row(dataset)
