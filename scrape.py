#!/usr/bin/env python
import argparse
from accessors.tv import AccessImdbTVSeries


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("series", help="Series to scrape")

    args = parser.parse_args()

    series = args.series

    AccessImdbTVSeries.search_and_process_series(series)


if __name__ == "__main__":
    main()
