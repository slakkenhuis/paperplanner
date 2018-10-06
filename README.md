paperplanner
===============================================================================

This repository contains the template for the week planner I use in my 
notebook.

The notebook is more or less A6 size, has a ring binder, and tabs. This works 
very well for me: it makes for a single object that carries all my schedule 
and notes; my fountain pen fits neatly into the rings; scrap paper can be 
given a second life by cutting it into the right size; and the pages can be 
freely rearranged or increased. I also find that it's easier to act 
intentionally when my organizational habits are offline.

My handwriting is very small, so for now, the script crams a whole week into a 
single page, which has the dimensions 16.3cm × 10cm. The dividing lines 
between the days have a 24-hour 'measuring tape' which allows me to mark 
certain events or keep track of my sleeping times. A little sun icon at the 
top shows the approximate sunrise time for that week.



Usage
-------------------------------------------------------------------------------

To generate the week planners, there is a Python script that uses 
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to manipulate 
the SVG, and [pyephem](https://rhodesmill.org/pyephem/) to calculate sunrise 
times. The single-page SVGs are converted to PDF with 
[Inkscape](https://inkscape.org), finally merging them into a single file with 
[pdfunite](https://poppler.freedesktop.org/).

Example:

    # Generate 10 pages for the 52N 2E location; see -h for details
    ./generate.py -n 10 -N 52 -E 2

    # Generate full planner
    make planner.pdf


Alternatives
-------------------------------------------------------------------------------

I could find a similar script for the publishing application 
[Scribus](https://www.scribus.net/), [here](http://diyplanner.com/node/8914).

