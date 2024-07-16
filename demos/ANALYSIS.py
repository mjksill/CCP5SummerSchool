
import pandas as pd

def peek_file(trajfile):
    print(trajfile)
    df = pd.read_pickle(trajfile)
    print(df['pos'][0])

def get_timesteps(trajfile):
    df = pd.read_pickle(trajfile)
    print(df.shape[0])
