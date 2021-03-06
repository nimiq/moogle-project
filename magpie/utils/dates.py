from time import strptime, mktime
from datetime import datetime


def twitter_date_to_solr_date(date_string):
    """
    Convert a Twitter date in the format:   Sun Feb 23 10:49:52 +0000 2014
    to a Solr date in the format:           2014-02-23T22:37:57Z
    """
    # First convert to datetime.
    dt = strptime(date_string, '%a %b %d %H:%M:%S +0000 %Y')
    dt = datetime.fromtimestamp(mktime(dt))

    # Then convert datetime to Solr format.
    return '{}Z'.format(dt.isoformat())


def facebook_date_to_solr_date(date_string):
    """
    Convert a Facebook date in the format:  2014-05-01T16:14:37+0000
    to a Solr date in the format:           2014-05-01T16:14:37Z
    """
    # Then convert datetime to Solr format.
    return date_string.replace('+0000', 'Z')


def dropbox_date_to_solr_date(date_string):
    """
    Convert a Dropbox date in the format:   Wed, 07 May 2014 10:00:54 +0000
    to a Solr date in the format:           2014-05-07T10:00:54Z
    """
    # First convert to datetime.
    dt = strptime(date_string, '%a, %d %b %Y %H:%M:%S +0000')
    dt = datetime.fromtimestamp(mktime(dt))

    # Then convert datetime to Solr format.
    return '{}Z'.format(dt.isoformat())