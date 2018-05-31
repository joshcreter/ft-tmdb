from formatters import CommonFormatters
import textwrap


class MovieTitlePopulator:
    @staticmethod
    def populate_movie_title_sheet(workbook, title_code, movie, imdb_id, unique_id=None):
        worksheet = workbook.get_movie_title_sheet().get_worksheet()

        title = movie.info()['title']
        formatted_title = CommonFormatters.format_project_title(title)

        dataset = {
            'unique_id': unique_id,
            'title_code': title_code,
            'title': title,
            'formatted_title': formatted_title,
            'tagline':  movie.info()['tagline'],
            'type': 'Film',
            'imdb_id': imdb_id,
            'year_completed': CommonFormatters.format_date_year_only(movie.info()['release_date']),
            'budget': movie.info()['budget'],
            'budget_currency': 'USD',
            'revenue': movie.info()['revenue'],
            'revenue_currency': 'USD',
            'runtime': movie.info()['runtime'],
            'homepage': movie.info()['homepage'],
            'original_language': CommonFormatters.format_language(movie.info()['original_language']),
            'status': CommonFormatters.format_project_status(movie.info()['status']),
            'synopsis': textwrap.shorten(movie.info()['overview'], width=999, placeholder="..."),
            'original_format': '35mm'
        }
        worksheet.write_data_row(dataset)


