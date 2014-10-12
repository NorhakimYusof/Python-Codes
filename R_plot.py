
# import rpy2 robjects to call R code
import rpy2.robjects as robjects

# setting R functions
rplot = robjects.r('plot')
rhist = robjects.r('hist')

r = robjects.r

#Create Data
data = [random.randint(0,10) for x in range(0,1000)]

# calling rplot
robjects.r('dev.new()') # optional: create a new figure
rplot(robjects.FloatVector(data[:]), ylab="")


# plotting the histogram
robjects.r('dev.new()') # optional: create a new figure
rhist(robjects.FloatVector(data[:]), xlab="", main="Histrogram")