# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2015.
#  https://github.com/GeographicaGS
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import rasterio

input_file = "/home/cayetano/Dropbox/documentos/python/GIS/workshop_RasterGIS_data/data/raster_out/example_data"
out_tif_file = "/tmp/out.tif"

with rasterio.drivers():
    with rasterio.open(input_file) as src:
        print(src.width, src.height)
        print(src.crs)
        print(src.affine)
        print(src.count)
        print(src.indexes)

with rasterio.drivers():
    rasterio.copy(input_file, out_tif_file, driver='GTiff')
