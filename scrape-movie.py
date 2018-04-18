#!/usr/bin/env python
import argparse
from accessors.movie import MovieAccessor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("movie", help="Movie to scrape")

    args = parser.parse_args()

    movie = args.movie

    movie_accessor = MovieAccessor()

    movie_accessor.search_and_process_movie(movie)


if __name__ == "__main__":
    main()
