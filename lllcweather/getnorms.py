# getnorms
#   Gets data about climatic normals from the United States National
#   Oceanographic and Atmospheric Administration National Climate Data Center.
#   Source data: https://www1.ncdc.noaa.gov/pub/data/normals/1981-2010
#   TODO: This data is updated every decade, so the link will change in 2020.
#         The code should adjust for that.
#
#   Program by Dan Stormont for Watershed Management Group
#   License: MIT


import requests

BASE_URL = 'https://www1.ncdc.noaa.gov/pub/data/normals/'

def get_precip_norms(stid):
    """Returns a list containing the monthly normal precipitation for the
       weather station indicated by the stid. The stid is the id for the GHCND
       network as defined by NOAA."""
    
    # TODO: This function returns the normal precipitation for all stations
    #       right now. Code needs to be added to parse the text and just return
    #       a list of precip values for the station indicated in stid.
    
    url = BASE_URL + '1981-2010' + '/products/precipitation/mly-prcp-normal.txt'
    r = requests.get(url)
    if (r.status_code == 200):
        for line in r.text.splitlines():
            parse_line = line.split()
            if parse_line[0] == stid:
                for norm in range(1, 13):
                    parse_line[norm] = float(parse_line[norm][:-1]) / 100
                return parse_line
    else:
        print 'ERROR: No data returned from server.'


def main():
    """Main function for getnorms."""

    LLLC_STID = 'USW00023160'
    
    print get_precip_norms(LLLC_STID)


if __name__ == '__main__':
    main()
    
