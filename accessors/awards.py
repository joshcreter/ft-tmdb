# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

from SPARQLWrapper import SPARQLWrapper, JSON
from formatters.common import CommonFormatters
from mappers.mappers import Mappers

class AwardsAccessor:
    @staticmethod
    def get_awards(imdb_id):

        # See https://stackoverflow.com/questions/3877623/in-python-can-you-have-variables-within-triple-quotes-if-so-how for formatting

        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        # query = """SELECT ?film ?award_received ?award_receivedLabel ?IMDb_ID WHERE {
        #   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        #   ?film wdt:P166 ?award_received.
        #   ?film wdt:P31 wd:Q11424.
        #   OPTIONAL { ?film wdt:P345 ?IMDb_ID. }
        #   FILTER(?IMDb_ID = "%s")
        # }
        # LIMIT 100"""

        query ="""SELECT DISTINCT ?time ?award_receivedLabel
                {
                    ?film wdt:P345 ?IMDb_ID;
                          p:P166 ?awardStat;
                          wdt:P166 ?award_received . 
                    FILTER(?IMDb_ID = "%s")
                  
                    ?awardStat pq:P805 ?award .            # Get the award (which is "subject of" XXth Academy Awards)
                    ?award wdt:P585 ?time .                # the "point of time" of the Academy Award
                  
                    SERVICE wikibase:label {               # ... include the labels
                        bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en"
                    }
                }
                ORDER BY DESC(?time)"""

        query = query % (imdb_id)
        # print (query)

        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()

        # print(results)
        # quit()

        output = []

        for result in results["results"]["bindings"]:
            year = CommonFormatters.format_date_year_only(result['time']['value'])
            award_title_data = Mappers.map_award(result['award_receivedLabel']['value'])

            # print(year + " | " + result['award_receivedLabel']['value'])

            if award_title_data:
                award_data = {
                    "result": "Winner",
                    "year": year,
                    "organization": award_title_data['organization'],
                    "trophy": award_title_data['trophy'],
                    "category": award_title_data['category'],
                }

                output.append(award_data)
                # print(award_data)

        return output
