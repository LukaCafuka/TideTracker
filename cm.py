import copernicusmarine

copernicusmarine.subset(
   dataset_id = "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m",
   variables = ["thetao"],
   start_datetime = "2023-08-07T00:00:00",
   end_datetime = "2023-08-21T23:59:59",
   minimum_longitude = -26,
   maximum_longitude = -22,
   minimum_latitude = 14,
   maximum_latitude = 18,
   minimum_depth = 0,
   maximum_depth = 5
)