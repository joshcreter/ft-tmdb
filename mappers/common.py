from formatters import CommonFormatters
from mappers.util import MapperUtil
from mappers.country import CountryMapper


class CommonMappers:
    @staticmethod
    def map_genres(genres):
        mapping = {
            "Sci-Fi & Fantasy": ["Sci-Fi", "Fantasy"],
            "Action & Adventure": ["Action", "Adventure"],
            "Science Fiction": "Sci-Fi"
        }

        genre_list = []
        for genre in genres:
            genre_list.append(genre['name'])

        return MapperUtil.map_list(genre_list, mapping)

    @staticmethod
    def map_production_status(status):
        mapping = {
            "Returning Series": "Production",
            "Planned": "Development",
            "In Production": "Production",
            "Ended": "Completed",
            "Canceled": "Completed",
            "Pilot": "Pre-Sale"
        }

        return MapperUtil.map_list([status], mapping)[0]

    @staticmethod
    def map_release_dates(release_dates):
        type_mapping = {
            1: "Premiere",
            2: "Release Date",
            3: "Release Date",
            4: "Release Date",
            5: "Release Date",
            6: "Release Date",
        }

        media_mapping = {
            1: "Theatrical",
            2: "Theatrical",
            3: "Theatrical",
            4: "Internet",
            5: "DVD",
            6: "Free TV",
        }

        timeline = []
        # print(release_dates)
        for territory in release_dates['results']:
            for release_date in territory['release_dates']:
                data = {
                    "type": type_mapping.get(release_date['type']),
                    # This is a convoluted way to map a single country
                    "territory": CountryMapper.map_countries([territory['iso_3166_1']])[0],
                    "media": media_mapping.get(release_date['type']),
                    "start_date": CommonFormatters.format_date(release_date['release_date']),
                    "note": release_date.get('note', '')
                }
                timeline.append(data)

        return timeline

    @staticmethod
    def map_tv_content_ratings(certifications):
        ratings = []

        authority_mapping = {
            'US': "TV Parental Guidelines",
            'KR': "Korea Media Rating Board",
            'DE': "Freiwillige Selbstkontrolle der Filmwirtschaft",
            'AU': "Australian Classification Board",
            'HU': "Hungarian Classification Board"
        }

        for certification in certifications:
            authority = authority_mapping.get(certification['iso_3166_1'], None)
            rating = certification['rating']
            if authority:
                ratings.append({'authority': authority,
                                'rating': rating})
            else:
                print("Missing rating authority: " + certification['iso_3166_1'])

        return ratings


        # content_ratings = series.content_ratings()
        # rating_us = list(filter(lambda d: d['iso_3166_1'] == 'US', content_ratings['results']))[0]['rating'].\
        #     replace('TV-PG', 'PG')
        # us_rating = list(filter(lambda d: d['iso_3166_1'] == 'US', ratings))[0]['rating']
