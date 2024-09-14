## Import Modules

from IPython.display import IFrame
# %matplotlib inline
import matplotlib.pyplot as plt
import getpass
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import copernicusmarine as cm

import numpy as np

# To avoid warning messages
import warnings
warnings.filterwarnings('ignore')

DS = cm.open_dataset(dataset_id="cmems_mod_ibi_phy_anfc_0.027deg-3D_P1M-m", start_datetime="2023-01-01T00:00:00", end_datetime="2024-07-01T00:00:00")

print(DS.depth)

target_date = "2023-02"
target_depth = 10

subset = DS[['thetao','so','time']].sel(time = slice("2023-01-01", "2023-12-31"))


port_lon = slice(-11.77, -7.22)
port_lat = slice(36.74, 42.22)

port_T = DS.thetao.sel(longitude = port_lon, latitude = port_lat)
port_T.sel(time=target_date).isel(depth=target_depth).plot(cmap='bwr')

target_t_period=slice("2023-01-01","2023-12-31")

gridpoint_lon = -9.541
gridpoint_lat = 38.718



port_S = DS.so.sel(longitude = port_lon, latitude = port_lat, time = target_t_period).isel(depth = target_depth)
port_S = port_S.sel(longitude = gridpoint_lon, latitude = gridpoint_lat, method='nearest')

subset_T = subset.thetao.isel(depth=target_depth).sel(time = target_date, method = 'nearest') # method='nearest' -> Method to use for inexact matches (use the nearest valid index value)

t_thetao = subset.thetao.isel(depth=target_depth).sel(time = target_date, method = 'nearest')

plt.figure(figsize=(15,10))

plt.subplot(1, 2, 1)
t_thetao.plot(color = 'blue')


plt.subplot(1, 2, 2)
port_S.plot(color = 'orange')


t_evolution = subset.thetao.sel(time=target_t_period).isel(depth=target_depth)
#plot
t_evolution.plot(col="time", col_wrap=6, size=4)

subset_T.plot(size = 8)


plt.show()

##plt.figure(figsize=(10, 6))
##ax = plt.axes(projection=ccrs.PlateCarree())

##DS['thetao'].isel(time=0, depth=0).plot(ax=ax, transform=ccrs.PlateCarree())

##ax.coastlines()
##plt.show()
