#!/usr/bin/env python3

from copy import copy
from bs4 import BeautifulSoup #at least 4.4, for copy()
from datetime import date, datetime, timedelta
import argparse

def monday(year, week):
    """
    Return the Monday of a given week.
    Thanks to https://stackoverflow.com/a/1287862
    """

    first_day = date(year, 1, 1)
    offset = first_day.isoweekday() - 1
    if year == first_day.isocalendar()[0]:
        week -= 1
    return first_day + timedelta(days=-offset, weeks=week)


def cook(soup, first):
    """
    Manipulate the BeautifulSoup XML object by changing the strings to
    correspond to the correct dates.
    """

    soup.find(id="title").string=first.strftime("%B %Y, week %W")

    for i, item in enumerate(["mon", "tue", "wed", "thu", "fri", "sat", "sun"]):
        d = first + timedelta(days=i)
        soup.find(id=item).string=d.strftime("%a %-d")

    return soup



if __name__ == "__main__":

    year, week, _ = datetime.now().isocalendar()

    parser = argparse.ArgumentParser(
            description="Generate week planner in SVG format.",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-y", "--year", 
        default=year, 
        metavar="N", 
        type=int,
        help="First week planner's year.")
    parser.add_argument("-w", "--week",
        default=week, 
        metavar="N", 
        type=int,
        help="Week number of first page.")
    parser.add_argument("-n", "--number", 
        default=1, 
        metavar="N",
        type=int,
        help="Number of week planners to generate.")
    parser.add_argument("-p", "--prefix", 
        default="planner-", 
        metavar="S", 
        help="Filename prefix of generated files.")
    args = parser.parse_args()

    # Obtain template
    svg = open("template.svg","r")
    primordial_soup = BeautifulSoup(svg, "xml")

    # Create week planners
    for i in range(0, args.number):

        fn = "{}{}.svg".format(args.prefix, i+1)
        soup = cook(first=monday(args.year, args.week+i), soup=copy(primordial_soup))
        
        with open(fn, "w") as f:
            f.write(str(soup))
