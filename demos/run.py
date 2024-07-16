

from subprocess import check_call

for N in range(1, 5):
    cmd = ['python', 'md.py', '--N', f'{N}',  '--outfile', f'junk{N}.pkl']
    output = check_call(cmd)

