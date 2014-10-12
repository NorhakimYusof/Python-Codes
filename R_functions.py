
import rpy2.robjects as robjects


# Exp 1 (R operator)

pi = robjects.r['pi']
pi[0]
print 'Exp 1'
print pi

# Exp 2 (R vectors)

#IntV = robjects.IntVector([1, 2, 3])
FloV = robjects.FloatVector([1.1,2.2,3.3])

rsort = robjects.r['sort']
sortV = rsort(robjects.IntVector([7,8,9]), decreasing=True)

print 'Exp 2'
print(IntV.r_repr())
print(FloV.r_repr())
print(sortV.r_repr())

# Exp 3 (R string)

letters = robjects.r['letters']
rcode = 'paste(%s, collapse="-")' %(letters.r_repr())
res = robjects.r(rcode)
print
print 'Exp 3'
print(res)

# Exp 4 (R Matrix)

values = robjects.FloatVector([1.1, 2.2, 3.3, 4.4, 5.5, 6.6])
matrix = robjects.r['matrix'](values, nrow = 2, ncol = 3)
print 'Exp 4'
print(matrix)



