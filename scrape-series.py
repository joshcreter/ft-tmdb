#!/usr/bin/env python
import argparse
from accessors import tv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("series", help="Series to scrape")

    args = parser.parse_args()

    series = args.series

    series_accessor = tv.TvAccessor()

    series_accessor.search_and_process_series(series)


if __name__ == "__main__":
    main()
