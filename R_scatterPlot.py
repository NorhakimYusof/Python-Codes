

from rpy2 import robjects
from rpy2.robjects import Formula, Environment
from rpy2.robjects.vectors import IntVector, FloatVector
from rpy2.robjects.lib import grid
from rpy2.robjects.packages import importr

# The R 'print' function
rprint = robjects.globalenv.get("print")
lattice = importr('lattice')
##datasets = importr('datasets')

### Plot
##xyplot = lattice.xyplot

# Dataset
mtcars = datasets.__rdata__.fetch('mtcars')['mtcars']

##formula = Formula('mpg ~ wt')
##formula.getenvironment()['mpg'] = mtcars.rx2('mpg')
##formula.getenvironment()['wt'] = mtcars.rx2('wt')
##
##p = lattice.xyplot(formula)
##
##rprint(p)

# Plot
gp = ggplot2.ggplot(mtcars)

pp = gp + \
     ggplot2.aes_string(x='wt', y='mpg', col='factor(cyl)') + \
     ggplot2.geom_point()

pp.plot()