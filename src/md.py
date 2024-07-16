import numpy as np
import numpy, math
import pandas as pd


################################################################################
################################################################################
################################################################################
# All the parameters of the simulation
box_length = 10 # How wide an area should the particles be scattered over
N = 20          # How many particles to simulate
dt = 0.1        # The timestep
k_particle = 5  # How stiff should the particle-particle interaction be
diameter = 2.0  # \sigma or the diameter of the particles
k_body = 0.1    # The stiffness of the spring holding the particles in the center of the sys

#Now we generate a Nx2 array/matrix holding the positions of all particles.
#They are randomly scattered from +- box_length
pos = (numpy.random.rand(N, 2) - 0.5) * box_length
#we also generate a Nx2 array of velocities initially at zero
vel = numpy.zeros((N,2))

#Calculate the force between two particles
def force(i, j):
    rij = pos[i] - pos[j]
    distance = numpy.linalg.norm(rij)
    if distance > diameter or i == j:
        # outside the interaction distance so return zero force
        return numpy.array([0,0])
    rij_norm = rij / distance
    return k_particle * (diameter - distance) * rij_norm

def body_force(i):
    return - k_body * pos[i]

def timestep(step):
    for i in range(N):
        pos[i] += 0.5 * dt * vel[i]
    #pos += 0.5 * dt * vel
    
    forces = numpy.zeros((N,2))
    for i in range(N):
        forces[i] += body_force(i)
        for j in range(N):
            forces[i] += force(i,j)

    for i in range(N):
        vel[i] += dt * forces[i]
    #vel += dt * forces
    
    for i in range(N):
        pos[i] += 0.5 * dt * vel[i]

        
nsteps = 100

pos_list = [pos]
vel_list = [vel]
for step in range(nsteps):
    timestep(step)
    pos_list.append(pos)
    vel_list.append(vel)
    
df = pd.DataFrame()
df['pos'] = pos_list
df.to_pickle('traj.pkl')

################################################################################
################################################################################
################################################################################


        
