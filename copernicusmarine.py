from copernicusmarine import subset


subset(
  dataset_id="cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m",
  variables=["uo", "vo"],
  minimum_longitude=50,
  maximum_longitude=90,
  minimum_latitude=0,
  force_download=True,
  maximum_latitude=25,
  start_datetime="2022-01-01T00:00:00",
  end_datetime="2022-01-31T23:59:59",
  minimum_depth=0,
  maximum_depth=30,
  output_filename = "CMEMS_Indian_currents_Jan2022.nc",
  output_directory = "copernicus-data"
)
