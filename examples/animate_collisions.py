import cms_made_simple as cms
import matplotlib.pylab as plt

import sys

import time

infile = '../test_data/cms_test.dat'

start = time.time()
collisions = cms.get_collisions(infile)
ncollisions = len(collisions)
print "Time to read in %d collisions: %f seconds" % (ncollisions,time.time()-start)


fig = plt.figure()
ax = fig.gca(projection='3d')
for i in xrange(ncollisions):
    print collisions[i]
    lines,fig,ax = cms.display_collision3D(collisions[i],fig=fig,ax=ax)
    plt.pause(0.0001)


