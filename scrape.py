#!/usr/bin/env python
import argparse
from accessors.movie import MovieAccessor
from accessors.tv import SeriesAccessor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("type", help="Type: movie or series")
    parser.add_argument("property", help="Name of movie or series")
    parser.add_argument("--unique_id_start", help="Start of unique ID range", default=None, type=int)

    args = parser.parse_args()

    scrape_type = args.type.lower()
    property_name = args.property
    unique_id_start = args.unique_id_start

    if scrape_type == 'movie':
        movie_accessor = MovieAccessor()
        movie_accessor.search_and_process_movie(property_name)

    if scrape_type == 'tv':
        series_accessor = SeriesAccessor()
        series_accessor.search_and_process_series(property_name, unique_id_start)


if __name__ == "__main__":
    main()
