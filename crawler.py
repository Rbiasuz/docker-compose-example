import os
import time
from functions import *

already_seen = set()

while True:
    
    time.sleep(3)
    files = os.listdir('code/Images') #lembrar de onde ela vai estar no container

    if len(files) < 1:
        print('No files to process...', flush=True)
    else:
        processed = 0
        for file in files:
            if file not in already_seen:
                texto = get_text('code/Images'+"/"+file) 
                print('\n', texto, '\n')
                already_seen.add(file)
                processed+=1
        if processed != 0:
            print('\n run finished, total files processed: ', processed,  flush=True)
        else:
            print('No new files to process...',  flush=True)

