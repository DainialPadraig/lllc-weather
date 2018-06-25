from MesoPy import Meso


m = Meso(token='0ee93b568404435a9f98ead284f5fc9c')
precip = m.precip(stid='e8967', start='201801010000', end='201806232359', units='precip|in')
