#!/usr/bin/env python
import argparse
from accessors.tv import SeriesAccessor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("series", help="Series to scrape")

    args = parser.parse_args()

    series = args.series

    series_accessor = SeriesAccessor()

    series_accessor.search_and_process_series(series)


if __name__ == "__main__":
    main()