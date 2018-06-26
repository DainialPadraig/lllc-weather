'''
WeatherData
   Retrives data from the MesoWest repository for the Living Lab and Learning
   Center weather station and displays it on a Raspberry Pi touchscreen.
   Hardware: Raspberry Pi 3
             Raspberry Pi official 7" touchscreen display.
   Software: Raspbian Jessie
             Python 2.7
             MesoPy 2.0.2
             Kivy
   Program by Dan Stormont
   License:
'''

from MesoPy import Meso

def main():
    m = Meso(token='0ee93b568404435a9f98ead284f5fc9c')

    current = m.latest(stid='e8967')
    precip = m.precip(stid='e8967',
                      start='201801010000', end='201806232359',
                      units='precip|in')
    print('Current station observations:')
    print(current)
    print('Precipitation observations since the start of the year:')
    print(precip)

if __name__ == '__main__':
    main()
    
