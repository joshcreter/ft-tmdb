#!/usr/bin/env python
import argparse
from accessors.movie import MovieAccessor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("movies", help="List of movies to scrape")

    args = parser.parse_args()

    movies = args.movies

    movie_accessor = MovieAccessor()

    movie_accessor.search_and_process_movielist(movies)


if __name__ == "__main__":
    main()
