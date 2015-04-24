#!/usr/bin/env python

"""
Create Canopy Height model from a DSM and DTM
"""

import os
import argparse
import datetime as dt
from l2d import create_chm


def main():
    dhf = argparse.ArgumentDefaultsHelpFormatter

    desc = 'Calculate and create CHM from a DSM and DTM'
    parser = argparse.ArgumentParser(description=desc, formatter_class=dhf)
    parser.add_argument('dsm', help='DSM input', default='DSM.tif')
    parser.add_argument('dtm', help='DTM input', default='DTM.tif')
    parser.add_argument('--fout', help='Output filename', default='CHM.tif')
    parser.add_argument('--hillshade', help='Generate hillshade', default=False, action='store_true')
    args = parser.parse_args()

    start = dt.datetime.now()
    print 'Gap-filling and creating final DEMs from %s files' % len(args.filenames)

    fout = create_chm(args.dtm, args.dsm, args.fout)

    if args.hillshade:
        cmd = 'gdaldem hillshade %s %s' % (fout, os.path.splitext(fout)[0] + '_hillshade.tif')
        os.system(cmd)

    print 'Created CHM in %s' % (dt.datetime.now() - start)


if __name__ == "__main__":
    main()
