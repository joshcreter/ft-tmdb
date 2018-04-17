#!/usr/bin/env python
import argparse
from accessors.tv import AccessImdbTVSeries

# if __name__ == '__main__':
#     # AccessImdbTVSeries.get_series('Star Trek: Voyager')
#


def main():
    outputfile = ''

    parser = argparse.ArgumentParser()
    parser.add_argument("series", help="Series to scrape")

    args = parser.parse_args()

    series = args.series

    AccessImdbTVSeries.get_series(series)



if __name__ == "__main__":
    main()
