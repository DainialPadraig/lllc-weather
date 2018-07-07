# lllcweather
#   Retrives data from the MesoWest repository for the Living Lab and Learning
#   Center weather station and displays it on a Raspberry Pi touchscreen.
#   Hardware: Raspberry Pi 3
#             Raspberry Pi official 7" touchscreen display.
#   Software: Raspbian Jessie
#             Python 2.7
#             MesoPy 2.0.3
#             Kivy
#   Program by Dan Stormont
#   License: MIT


from datetime import datetime, date, time
from MesoPy import Meso
from pprint import pprint

#TODO-Get rid of these global constants and variables
MESOWEST_TOKEN = '0ee93b568404435a9f98ead284f5fc9c'    
_m = Meso(token=MESOWEST_TOKEN)


def display_latest(station_id):
    """Display the latest weather readings from station_id."""
    
    print 'Most recent weather readings:'
    print '-----------------------------'
    latest_reading = _m.latest(stid=station_id,
                               units='precip|in,speed|mph,temp|F')
    print ('Temperature: '
           + str(latest_reading['STATION'][0]['OBSERVATIONS']
                 ['air_temp_value_1']['value'])
           + ' deg F')
    print ('Rainfall today: '        
           + str(latest_reading['STATION'][0]['OBSERVATIONS']
                 ['precip_accum_since_local_midnight_value_1']['value'])
           + ' inches')
    print ('Wind speed: '
           + str(latest_reading['STATION'][0]['OBSERVATIONS']
                 ['wind_speed_value_1']['value'])
           + ' mph')
    print ('Wind cardinal direction: '
           + str(latest_reading['STATION'][0]['OBSERVATIONS']
                 ['wind_cardinal_direction_value_1d']['value']))           
    print ('Wind direction: '
           + str(latest_reading['STATION'][0]['OBSERVATIONS']
                 ['wind_direction_value_1']['value'])
           + ' degrees')           
    print


def display_temp_month(station_id):
    """Display daily high, low, and average temperature for the month at
       station_id, daily high, low, and average temperature for the same month
       last year at station_id, and average high, low, and average temperature
       for the month from the National Weather Service."""
    print 'Temperatures for this month:'
    print '----------------------------'
    dt = datetime.now()
    stats_mtd = _m.time_stats(stid=station_id,
                              start=(dt.strftime('%Y%m') + '010000'),
                              end=dt.strftime('%Y%m%d%H%M'),
                              obtimezone='local',
                              units='temp|F',
                              type='all',
                              vars='air_temp')
    print ('Average: '
           + str(stats_mtd['STATION'][0]['STATISTICS']
                 ['air_temp_set_1']['average'])
           + ' deg F')
    print ('Maximum: '
           + str(stats_mtd['STATION'][0]['STATISTICS']
                 ['air_temp_set_1']['maximum'])
           + ' deg F')
    print ('Median: '
           + str(stats_mtd['STATION'][0]['STATISTICS']
                 ['air_temp_set_1']['median'])
           + ' deg F')
    print ('Minimum: '
           + str(stats_mtd['STATION'][0]['STATISTICS']
                 ['air_temp_set_1']['minimum'])
           + ' deg F')
    print

def display_temp_ytd(station_id):
    """Display monthly high, low, and average temperature for the year to date
       at station_id, monthly high, low, and average temperature for last year
       at station_id, and average monthly high, low, and average temperature
       for the year from the National Weather Service."""
    print 'Temperatures since the start of the year:'
    print '-------------------------------------------------'
    dt = datetime.now()
    stats_ytd = _m.time_stats(stid=station_id,
                              start=(dt.strftime('%Y') + '01010000'),
                              end=dt.strftime('%Y%m%d%H%M'),
                              obtimezone='local',
                              units='temp|F',
                              type='all',
                              vars='air_temp')
    print ('Average: '
           + str(stats_ytd['STATION'][0]['STATISTICS']
                 ['air_temp_set_1']['average'])
           + ' deg F')
    print ('Maximum: '
           + str(stats_ytd['STATION'][0]['STATISTICS']
                 ['air_temp_set_1']['maximum'])
           + ' deg F')
    print ('Median: '
           + str(stats_ytd['STATION'][0]['STATISTICS']
                 ['air_temp_set_1']['median'])
           + ' deg F')
    print ('Minimum: '
           + str(stats_ytd['STATION'][0]['STATISTICS']
                 ['air_temp_set_1']['minimum'])
           + ' deg F')
    print
    

def display_precip_month(station_id, nws_stid):
    """Display daily rainfall for the month at station_id, daily rainfall for
       the same month last year at station_id, and average rainfall for the
       month from the National Weather Service."""
    print 'Total monthly rainfall:'
    print '-----------------------'
    dt = datetime.now()
    # Note that it should be possible to have multiple stids in the call to the
    # MesoPy API; however, I found the order of the returned lists was not
    # consistent, so I am limiting the call to one id at a time.
    precip_mtd = _m.precip(stid=station_id,
                           start=(dt.strftime('%Y%m') + '010000'),
                           end=dt.strftime('%Y%m%d%H%M'),
                           obtimezone='local',
                           units='precip|in')
    print('Rainfall for ' + dt.strftime('%B %Y') + ' at '
          + str(precip_mtd['STATION'][0]['NAME']) + ': '
          + str(precip_mtd['STATION'][0]['OBSERVATIONS']
                ['total_precip_value_1'])
          + ' inches')
    last_year = dt.year - 1
    precip_mtd = _m.precip(stid=station_id,
                           start=(str(last_year) + dt.strftime('%m') + '010000'),
                           end=(str(last_year) + dt.strftime('%m%d%H%M')),
                           obtimezone='local',
                           units='precip|in')
    print('Rainfall for ' + dt.strftime('%B ') + str(last_year) + ' at '
          + str(precip_mtd['STATION'][0]['NAME']) + ': '
          + str(precip_mtd['STATION'][0]['OBSERVATIONS']
                ['total_precip_value_1'])
          + ' inches')
    precip_mtd = _m.precip(stid=nws_stid,
                           start=(dt.strftime('%Y%m') + '010000'),
                           end=dt.strftime('%Y%m%d%H%M'),
                           obtimezone='local',
                           units='precip|in')
    print('Rainfall for ' + dt.strftime('%B %Y') + ' at '
          + str(precip_mtd['STATION'][0]['NAME']) + ': '
          + str(precip_mtd['STATION'][0]['OBSERVATIONS']
                ['total_precip_value_1'])
          + ' inches')
    print
    

def display_precip_ytd(station_id):
    """Display total rainfall since Jan 1 at station_id.""" 
    print 'Total rainfall since the start of the year:'
    print '-------------------------------------------'
    precip = _m.precip(stid=station_id,
                       start=(datetime.now().strftime('%Y') + '01010000'),
                       end=datetime.now().strftime('%Y%m%d%H%M'),
                       obtimezone='local',
                       units='precip|in')
    print ('Living Lab and Learning Center: '
           + str(precip['STATION'][0]['OBSERVATIONS']['total_precip_value_1'])
           + ' inches')
    print
    

    
def main():
    """Main function for WeatherData."""

    LLLC_STID = 'e8967'
    NWS_STID = 'ktus'

    display_latest(LLLC_STID)
    display_temp_month(LLLC_STID)
    display_temp_ytd(LLLC_STID)
    display_precip_month(LLLC_STID, NWS_STID)
    display_precip_ytd(LLLC_STID)

if __name__ == '__main__':
    main()
    
