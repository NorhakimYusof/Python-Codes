

from rpy2 import robjects
from rpy2.robjects import Formula, Environment
from rpy2.robjects.vectors import IntVector, FloatVector
from rpy2.robjects.lib import grid
from rpy2.robjects.packages import importr

# The R 'print' function
rprint = robjects.globalenv.get("print")
lattice = importr('lattice')

# Dataset
mtcars = datasets.__rdata__.fetch('mtcars')['mtcars']


# Plot
gp = ggplot2.ggplot(mtcars)

pp = gp + \
     ggplot2.aes_string(x='wt', y='mpg', col='factor(cyl)') + \
     ggplot2.geom_point()

pp.plot()