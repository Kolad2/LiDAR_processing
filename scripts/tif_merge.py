import os
from pathlib import Path
from rocknetmanager.tools import mosaic_merge
from rocknetmanager.tools import geotif2geotif_standart


#path_to_images = Path("D:/1.ToSaver/profileimages/Matteo_database/Site_A/images")
path_to_image = Path("D:/1.ToSaver/profileimages/Matteo_database/Site_I/Site_I.tif")

geotif2geotif_standart(path_to_image, path_to_image.parent / (path_to_image.stem + "_2.tif"))
#mosaic_merge(path_to_images)

# geotif2geotif_standart()

