# WeatherData
#   Retrives data from the MesoWest repository for the Living Lab and Learning
#   Center weather station and displays it on a Raspberry Pi touchscreen.
#   Hardware: Raspberry Pi 3
#             Raspberry Pi official 7" touchscreen display.
#   Software: Raspbian Jessie
#             Python 2.7
#             MesoPy 2.0.3
#             Kivy
#   Program by Dan Stormont
#   License:


from MesoPy import Meso

#TODO-Get rid of these global constants and variables
MESOWEST_TOKEN = '0ee93b568404435a9f98ead284f5fc9c'    
m = Meso(token=MESOWEST_TOKEN)


def display_latest(station_id):
    """Display the latest weather readings from station_id."""
    
    print 'Most recent weather readings:'
    print '-----------------------------'
    print m.latest(stid=station_id,
                   units='precip|in,speed|mph,temp|F')
    print


def display_precip_ytd(station_id):
    """Display total rainfall since Jan 1 at station_id.""" 
    print 'Total rainfall since the start of the year:'
    print '-------------------------------------------'
    print m.precip(stid=station_id,
                   start='201801010000', end='201806232359',
                   units='precip|in')
    print
    

    
def main():
    """Main function for WeatherData."""

    LLLC_STID = 'e8967'

    display_latest(LLLC_STID)
    display_precip_ytd(LLLC_STID)

if __name__ == '__main__':
    main()
    
