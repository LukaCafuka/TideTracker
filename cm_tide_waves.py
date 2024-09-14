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

DS = cm.open_dataset(dataset_id="cmems_mod_glo_wav_anfc_0.083deg_PT3H-i", start_datetime="2020-01-01T00:00:00", end_datetime="2024-07-01T00:00:00")

target_date = "2023-02"


port_lon = slice(-11.77, -7.22)
port_lat = slice(36.74, 42.22)

subset = DS[['VHM0']].sel(time = slice("2023-01-01", "2023-12-31"))

#wave = subset.isel(wave=0).sel(time=0).plot()

port_T = DS.VHM0.sel(longitude = port_lon, latitude = port_lat)
port_T.sel(time=target_date).plot()

## Display the locations of the glider on a mini map
ax_mini_map = port_T.add_axes([0.5, 1, 0.3, 0.2], projection=ccrs.PlateCarree())                               # create the minimap and define its projection
gl = ax_mini_map.gridlines(draw_labels=True)                                                              # add the lon/lat gridlines
gl.right_labels = False                                                                                   # remove latitude labels on the right
gl.top_labels = False                                                                                     # remove longitude labels on the top
# Customize mini map
ax_mini_map.add_feature(cfeature.LAND, zorder=0, edgecolor='k')                                           # add land mask
ax_mini_map.set_extent([-10, -9, 38.4, 39], crs = ccrs.PlateCarree())                            # define the extent of the mini map [lon_min,lon_max,lat_min,lat_max]
ax_mini_map.scatter(port_lon, port_lat, 25,'tab:green',transform=ccrs.PlateCarree())

plt.show()
