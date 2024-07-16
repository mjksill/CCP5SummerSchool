import argparse
import numpy as np
import pandas as pd


################################################################################
################################################################################
################################################################################
parser = argparse.ArgumentParser()

parser.add_argument('--N', type=int, default=20, help='number of particles')
parser.add_argument('--steps', type=int, default=10, help='number of time steps')
parser.add_argument('--outfile', type=str, default='traj.pkl', help='output trajectory file')

args = parser.parse_args()

N = args.N
nsteps = args.steps
outfile = args.outfile

################################################################################
################################################################################
################################################################################
# All the parameters of the simulation
box_length = 10 # How wide an area should the particles be scattered over
#N = 2          # How many particles to simulate
dt = 0.1        # The timestep
k_particle = 5  # How stiff should the particle-particle interaction be
diameter = 2.0  # \sigma or the diameter of the particles
k_body = 0.1    # The stiffness of the spring holding the particles in the center of the sys



#Now we generate a Nx2 array/matrix holding the positions of all particles.
#They are randomly scattered from +- box_length
pos = (np.random.rand(N, 2) - 0.5) * box_length
#we also generate a Nx2 array of velocities initially at zero
vel = np.zeros((N,2))

#Calculate the force between two particles
def force(i, j):
    rij = pos[i] - pos[j]
    distance = np.linalg.norm(rij)
    if distance > diameter or i == j:
        # outside the interaction distance so return zero force
        return np.array([0,0])
    rij_norm = rij / distance
    return k_particle * (diameter - distance) * rij_norm

def body_force(i):
    return - k_body * pos[i]

def timestep(step):
    for i in range(N):
        pos[i] += 0.5 * dt * vel[i]
    #pos += 0.5 * dt * vel
    
    forces = np.zeros((N,2))
    for i in range(N):
        forces[i] += body_force(i)
        for j in range(N):
            forces[i] += force(i,j)

    for i in range(N):
        vel[i] += dt * forces[i]
    #vel += dt * forces
    
    for i in range(N):
        pos[i] += 0.5 * dt * vel[i]

        

pos_list = [pos]
vel_list = [vel]
for step in range(nsteps):
    timestep(step)
    pos_list.append(pos)
    vel_list.append(vel)

df = pd.DataFrame()
df['pos'] = pos_list
df['vel'] = vel_list
df.to_pickle(outfile)



################################################################################
################################################################################
################################################################################


        
