
from rpy2.robjects import r
from rpy2.robjects.packages import importr

#First
stats = importr('utils', data=True)
help_doc = stats.help("help")
#print str(help_doc)

#Second
r.library("stats")
r.library("lattice")
r.library("splines")
r.library("ggplot2")
r.library("gstat")

#r.library("gstat")