import numpy as np


def deterministic(X,L=0.8, kappa=0.025, alpha=0.01):
    """
    INPUT: 
        X : vector of sister positions
        
    OUTPUT:
        Y : spring + PEF component"""
    X1 = X[0]
    X2 = X[1]
    
    Y = np.zeros(2)
    Y[0] = -(kappa*(X1-X2-L*np.cos(0))) - (alpha*(X1))
    Y[1] = -(kappa*(X2-X1+L*np.cos(0))) - (alpha*(X2))
    
    return Y

def check_coherent(u):
    """
    INPUT:
        u : 1D vector of sister states
        
    OUTPUT:
        boolean to check if the sister states are coherent(opposite signs)"""
    if u == [1,-1] or u == [-1,1]:
        check = True
    else:
        check = False
    return check

def check_incoherent(u):
    """
    INPUT:
        u : 1D vector of sister states
        
    OUTPUT:
        boolean to check if the sister states are incoherent(same signs)"""
    if u == [1,1] or u == [-1,-1]:
        check = True
    else:
        check = False
    return check


def sister_states(p,sigma,T=600,dt=2):
    """
    INPUT:
        p : 1D vector of probabilities
        T : max time
        dt : time step
        sigma : (de)polymerizing state
        
    OUTPUT:
        Y : 2D vector of the two sisters"""
    
    steps = np.arange(0,T,dt)
    Y = np.zeros((len(steps),2))
    Y[0] = sigma
    sign = -1
    
    
    for i in range(1,len(Y)):
        
        current_state = Y[i-1].tolist()
        sigma1 = current_state[0] #sister1
        sigma2 = current_state[1] #sister2
        
        #draw uniform random sample
        u = np.random.uniform(0,1,2)
        
        #check state
        if check_coherent(current_state):
            
            #compute new state using p_c
            if u[0] <= p[0] and u[1] <= p[0]: #remain coherent
                Y[i] = Y[i-1]
            elif u[0] <= p[0] and u[1] > p[0]: #sister 2 switches sign
                Y[i] = [sigma1, sigma2*sign]
            elif u[0] > p[0] and u[1] > p[0]: #both sisters switches sign
                Y[i] = [sigma1*sign, sigma2*sign]
            elif u[0] > p[0] and u[1] <= p[0]: #sister1 switches sign
                Y[i] = [sigma1*sign, sigma2]
        
        elif check_incoherent(current_state):
            
            #compute new state using p_ic
            if u[0] <= p[1] and u[1] <= p[1]: #remain coherent
                Y[i] = Y[i-1]
            elif u[0] <= p[1] and u[1] > p[1]: #sister 2 switches sign
                Y[i] = [sigma1, sigma2*sign]
            elif u[0] > p[1] and u[1] > p[1]: #both sisters switches sign
                Y[i] = [sigma1*sign, sigma2*sign]
            elif u[0] > p[1] and u[1] <= p[1]: #sister1 switches sign
                Y[i] = [sigma1*sign, sigma2]
    return Y

def oscillations(Y,v,dt,s):
    
    Z = np.zeros((len(Y),5)) #[siter1 pos, sister2 pos, inter-sis distance, annotated state, mean sis pos]
    Z[0] = [0.5, -0.5, 0., 1. ,0.]#initial positions

    for i in range(1,len(Y)):
    
        X = deterministic(Z[i-1])

        if Y[i,0] == -1 and Y[i,1] == 1:
            Z[i,0] = Z[i-1,0] + (-v[0] + X[0] + np.random.normal(0,(s)))*dt
            Z[i,1] = Z[i-1,1] + (v[1] + X[1] + np.random.normal(0,(s)))*dt
            Z[i,2] = Z[i,0] - Z[i,1] # intersister distance
            Z[i,3] = 0 #annotation to record the state in time
            Z[i,4] = np.mean(Z[i,:2]) # sister mean distance

        elif Y[i,0] == -1 and Y[i,1] == -1:
            Z[i,0] = Z[i-1,0] + (-v[0] + X[0] + np.random.normal(0,(s)))*dt
            Z[i,1] = Z[i-1,1] + (v[0] + X[1] + np.random.normal(0,(s)))*dt
            Z[i,2] = Z[i,0] - Z[i,1] # intersister distance
            Z[i,3] = 1 #annotation to record the state in time
            Z[i,4] = np.mean(Z[i,:2]) # sister mean distance

        elif Y[i,0] == 1 and Y[i,1] == -1:
            Z[i,0] = Z[i-1,0] + (-v[1] + X[0] + np.random.normal(0,(s)))*dt
            Z[i,1] = Z[i-1,1] + (v[0] + X[1] + np.random.normal(0,(s)))*dt
            Z[i,2] = Z[i,0] - Z[i,1] # intersister distance
            Z[i,3] = 2 #annotation to record the state in time
            Z[i,4] = np.mean(Z[i,:2]) # sister mean distance

        elif Y[i,0] == 1 and Y[i,1] == 1:
            Z[i,0] = Z[i-1,0] + (-v[1] + X[0] + np.random.normal(0,(s)))*dt
            Z[i,1] = Z[i-1,1] + (v[1] + X[1] + np.random.normal(0,(s)))*dt
            Z[i,2] = Z[i,0] - Z[i,1] # intersister distance
            Z[i,3] = 3 #annotation to record the state in time
            Z[i,4] = np.mean(Z[i,:2]) # sister mean distance
    return Z