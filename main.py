import logging
from sentinelhub import *
import os
from eval_scripts import *

from secret import get_secret

config = SHConfig()

logging.basicConfig(level=logging.DEBUG)
logging.captureWarnings(True)



config.sh_client_id, config.sh_client_secret = get_secret()
config.sh_base_url = 'https://sh.dataspace.copernicus.eu'
config.sh_token_url = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'
config.save("my profile")



betsiboka_coords_wgs84 = (15.857563,45.736860,16.138916,45.829397)
resolution = 10
betsiboka_bbox = BBox(bbox=betsiboka_coords_wgs84, crs=CRS.WGS84)
betsiboka_size = bbox_to_dimensions(betsiboka_bbox, resolution=resolution)

print(f"Image shape at {resolution} m resolution: {betsiboka_size} pixels")




request_all_bands = SentinelHubRequest(
    data_folder="test_dir",
    evalscript=evalscript_all_bands,
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L1C.define_from("s2l1c", service_url=config.sh_base_url),
            time_interval=("2024-08-01", "2024-09-01"),
            mosaicking_order=MosaickingOrder.LEAST_CC,
        )
    ],
    responses=[SentinelHubRequest.output_response("default", MimeType.TIFF)],
    bbox=betsiboka_bbox,
    size=betsiboka_size,
    config=config,
)


all_bands_img = request_all_bands.get_data(save_data=True)

all_bands_img_from_disk = request_all_bands.get_data()

all_bands_img_redownload = request_all_bands.get_data(redownload=True)