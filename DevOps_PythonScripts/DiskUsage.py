import os
use_space=os.system('du -h')  # Disk space usage
free_space=os.system('df -h')  # Disk space free

print('Disk Usage:',use_space)
print('Disk Free:',free_space)

