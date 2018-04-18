import tmdbsimple as tmdb
from populators.common import CommonPopulator
from populators.contacts import ContactsPopulator


class CommonAccessor:
    tmdb = tmdb

    def __init__(self):
        self.tmdb.API_KEY = '9115e244e6f77d274bb345abc96fa420'

# from functools import reduce
# import operator
# import re
# from more_itertools import unique_everseen
#
# class CommonAccessors:
#     @staticmethod
#     def map_list(source_list, mapping_dict):
#         output = []
#
#         for item in source_list:
#             mapped_item = mapping_dict.get(item, item)
#
#             # If the item is not mapped, wrap it in a list
#             # Doing this prevents the unmapped item string from exploding into single characters in the next step
#             if isinstance(mapped_item, list):
#                 output.append(mapped_item)
#             else:
#                 output.append([mapped_item])
#
#         # Now flatten the list of lists into a simple list
#         output = reduce(operator.add, output)
#
#         # Next deduplicate the flattened list
#         output = list(unique_everseen(output))
#
#         # Filter out blank items
#         output = list(filter(None, output))
#
#         return output
#
#     @staticmethod
#     def formatGenres(genres):
#         mapping = {
#             "Sci-Fi & Fantasy": ["Sci-Fi", "Fantasy"],
#             "Action & Adventure": ["Action", "Adventure"]
#         }
#
#         genre_list = []
#         for genre in genres:
#             genre_list.append(genre['name'])
#
#         return CommonAccessors.map_list(genre_list, mapping)
#
#     @staticmethod
#     def formatCountries(countries):
#         mapping = {
#             "US": "United States of America"
#         }
#
#         return CommonAccessors.map_list(countries, mapping)
#
#     @staticmethod
#     def formatPropertyTitle(property):
#         property = re.sub(r'^The (.*)', r'\1, The', property)
#         property = re.sub(r'^A (.*)', r'\1, A', property)
#         property = re.sub(r'^An (.*)', r'\1, An', property)
#
#         return property
#
