import cms_made_simple as cms
import matplotlib.pylab as plt

import sys

import time

infile = '../test_data/cms_test.dat'

start = time.time()
collisions = cms.get_collisions(infile)
print "Time to read in %d collisions: %f seconds" % (len(collisions),time.time()-start)

print len(collisions)

lines,fig,ax = cms.display_collision3D(collisions[1])

plt.show()

