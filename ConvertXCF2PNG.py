#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# "C:\Users\[USER]\AppData\Roaming\GIMP\2.xx\plug-ins\" Put This File
# Check Gimp Tool Bar, Open Batch -> XCF2xx
#

import os,glob
from gimpfu import *

def xcf2png(file, compression):
    image = pdb.gimp_xcf_load(0, file, file)
    savedlayer = pdb.gimp_layer_new_from_visible(image, image, "Saved Image")
    outfile = os.path.splitext(file)[0]+'.png'
    pdb.file_png_save(image, savedlayer, outfile, outfile, True, compression, True, True, True, True, True)
    pdb.gimp_image_delete(image)

def xcf2png_batch(directory, compression):
    for file in glob.glob(os.path.join(directory, '*.xcf')):
        xcf2png(file, compression)

register(
        "python_fu_xcf2png_batch",
        "Convert XCF to PNG",
        "Convert XCF to PNG",
        "@pcjpnet",
        "@pcjpnet",
        "2021/1/14",
        "<Toolbox>/Batch/XCF2PNG",
        "",
        [
           (PF_DIRNAME, "directory", "XCF Image Directory", "/tmp"),
           (PF_ADJUSTMENT, "compression", "Compression", 9, (0, 9, 1))
        ],
        [],
        xcf2png_batch)

main()

