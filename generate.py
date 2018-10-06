#!/usr/bin/env python3

from copy import copy
from bs4 import BeautifulSoup #at least 4.4, for copy()
from datetime import date, datetime, timedelta

svg = open("template.svg","r")
primordial_soup = BeautifulSoup(svg, "xml")

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


def cook(year, week, prefix="planner-"):
    soup = copy(primordial_soup)

    mon = monday(year, week)
    tue = mon + timedelta(days=1)
    wed = mon + timedelta(days=2)
    thu = mon + timedelta(days=3)
    fri = mon + timedelta(days=4)
    sat = mon + timedelta(days=5)
    sun = mon + timedelta(days=6)

    soup.find(id="title").string=mon.strftime("%B %Y, week %W")
    soup.find(id="mon").string="mon {}".format(mon.day)
    soup.find(id="tue").string="tue {}".format(tue.day)
    soup.find(id="wed").string="wed {}".format(wed.day)
    soup.find(id="thu").string="thu {}".format(thu.day)
    soup.find(id="fri").string="fri {}".format(fri.day)
    soup.find(id="sat").string="sat {}".format(sat.day)
    soup.find(id="sun").string="sun {}".format(sun.day)

    with open("{}{}-{}.svg".format(prefix, year, week), "w") as f:
        f.write(str(soup))

cook(2018, 41)
