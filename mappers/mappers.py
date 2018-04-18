from functools import reduce
import operator
from more_itertools import unique_everseen


class Mappers:
    @staticmethod
    def map_list(source_list, mapping_dict):
        output = []

        for item in source_list:
            mapped_item = mapping_dict.get(item, item)

            # If the item is not mapped, wrap it in a list
            # Doing this prevents the unmapped item string from exploding into single characters in the next step
            if isinstance(mapped_item, list):
                output.append(mapped_item)
            else:
                output.append([mapped_item])

        # Now flatten the list of lists into a simple list
        output = reduce(operator.add, output)

        # Next deduplicate the flattened list
        output = list(unique_everseen(output))

        # Filter out blank items
        output = list(filter(None, output))

        return output

    @staticmethod
    def map_genres(genres):
        mapping = {
            "Sci-Fi & Fantasy": ["Sci-Fi", "Fantasy"],
            "Action & Adventure": ["Action", "Adventure"]
        }

        genre_list = []
        for genre in genres:
            genre_list.append(genre['name'])

        return Mappers.map_list(genre_list, mapping)

    @staticmethod
    def map_countries(countries):
        mapping = {
            "AU": "Australia",
            "GB": "United Kingdom",
            "MT": "Malta",
            "US": "United States of America"
        }

        return Mappers.map_list(countries, mapping)



