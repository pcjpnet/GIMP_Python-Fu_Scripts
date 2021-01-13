#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# "C:\Users\[USER]\AppData\Roaming\GIMP\2.xx\plug-ins\" Put This File
# Check Gimp Tool Bar, Open Batch -> XCF2xx
#

import os,glob
from gimpfu import *

def xcf2jpg(file, quality):
    image = pdb.gimp_xcf_load(0, file, file)
    savedlayer = pdb.gimp_layer_new_from_visible(image, image, "Saved Image")
    outfile = os.path.splitext(file)[0]+'.jpg'
    pdb.file_jpeg_save(image, savedlayer, outfile, outfile, quality, 0.0, 0, 0, "", 0, 1, 0, 2)
    pdb.gimp_image_delete(image)

def xcf2jpg_batch(directory, quality):
    for file in glob.glob(os.path.join(directory, '*.xcf')):
        xcf2jpg(file, quality)

register(
        "python_fu_xcf2jpg_batch",
        "Convert XCF to JPG",
        "Convert XCF to JPG",
        "@pcjpnet",
        "@pcjpnet",
        "2021/1/14",
        "<Toolbox>/Batch/XCF2JPEG",
        "",
        [
           (PF_DIRNAME, "directory", "XCF Image Directory", "/tmp"),
           (PF_ADJUSTMENT, "quality", "Quality", 0.9, (0.00, 1.00, 0.01))
        ],
        [],
        xcf2jpg_batch)

main()

