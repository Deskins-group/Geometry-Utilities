#! /usr/bin/env python
import string
import sys
import math 

#---------------------------------------------------
# xyz-compare.py Takes two xyz files and compares the coordinates
# of the two structures. It gives difference in x coords (del X), 
# difference in y coords (del Y), difference in z coords (del Z),
# total distance between the atoms (del Tot), and the surface 
# fluxionality. 
# Surface fluxionality defined in Yang et al. (2015). Phys. Chem. Chem. Phys.,
# 17(38), 25379-25392. https://doi.org/10.1039/C5CP03674G
#---------------------------------------------------
# Usage: ./xyz-compare.py file1.xyz file2.xyz 
#
#---------------------------------------------------
# Author: N. Aaron Deskins e-mail: nadeskins [at] wpi.edu
# Date:   6-5-2017
#---------------------------------------------------

zf = open(sys.argv[1],'r')
gf = open(sys.argv[2],'r')
print '%5s %5s %8s %11s %11s %12s' % ('No.','Type','del X', 'del Y', 'del Z', 'del Tot')
totdist = 0.0
it = 0

while 1:
    line = zf.readline()
    line = line.strip()
    ls = line.split()

    lineg = gf.readline()
    lineg = lineg.strip()
    lsg = lineg.split()

    if not line:
        break
    it = it + 1
    if it > 2:
        #print line
        tx = float(ls[1])
        ty = float(ls[2])
        tz = float(ls[3])
        gx = float(lsg[1])
        gy = float(lsg[2])
        gz = float(lsg[3])

        dx = tx-gx
        dy = ty-gy
        dz = tz-gz
        dist = (dx*dx+dy*dy+dz*dz)**0.5
        totdist = totdist + dist
        #print ls[0], tx, ty, tz, dist 
        print '%4s %4s %11.5f %11.5f %11.5f %11.5f' % (it-2,ls[0], dx, dy, dz, dist)

zf.close()
gf.close()
totdist = totdist/(float(it-2))
print "Structual Fluxionality: ",totdist




