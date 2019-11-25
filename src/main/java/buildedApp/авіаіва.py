def fminnlcon(self,fun,x0,g,c,beta,threshold=1e-6,vectorized=False,**kwargs):
'''
Minimum (Non Linearly) Constrained Optimization
The weighted function is minimized using the defined algorithm for unconstrained optimization
in .unconstrained
..fun as callable object; must be a function of x0 and return a single number
..x0 as a numeric array; point from which to start
..g as an array of callable inequality constraints functions
..c as numeric, initial constraint weight
..beta as numeric (>1) as the factor by which c growths after each iteration
..threshold as a numeric value; threshold at which to stop the iterations
..**kwargs = initial_hessian : as matrix (default = identity)
.. see unconstrained.params for further details on the methods that are being used
'''
P = lambda x : _np.sum([_np.max([0.,_(x)]) for _ in g])
f = lambda x : fun(x)+c*P(x)
chck = lambda x : c*P(x)
x = x0
if vectorized:
x_vec = [x0]
c_vec = [c]
err_vec =[chck(x)]
else:
    pass
iters = 0
inner_iters = 0
lsiters = 0
print chck(x)
#print P(x)
while chck(x) > threshold:
    print 'f(x) = ', f(x)#,'P(x) = ', P(x)
    sol = self.__unconstrained.fminunc(f,x,threshold)
    print sol
    x = sol['x']
    print 'x',x
    print 'f(x)',f(x)
    #print 'P(x)',P(x)
    print 'chck',chck(x)
    c *= beta
    if vectorized:
        x_vec += [x]
        c_vec += [c]
        err_vec += [chck(x)]
    else:
        pass
    iters += 1
    inner_iters += sol['iterations']
    lsiters += sol['ls_iterations']
if vectorized:
print x_vec
    return {'x':x_vec, 'f':[fun(x) for x in x_vec], 'c': c_vec, 'err' : err_vec,
'iterations':iters,'inner_iterations':inner_iters,'ls_iterations':lsiters}#, 'parameters' : params.copy()}
else:
    return {'x':x, 'f':fun(x),'c':c,'iterations':iters,'inner_iterations':inner_iters,'ls_iterations':lsiters}#,
'parameters' : params.copy()}