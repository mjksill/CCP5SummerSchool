
import glob
import pandas as pd
import matplotlib.pylab as plt

import ANALYSIS

traj_list = glob.glob('junk?.pkl')
traj_list.sort()

for trajfile in traj_list:
    ANALYSIS.peek_file(trajfile)
    ANALYSIS.get_timesteps(trajfile)
