import time
from tqdm import tqdm

def loading():
    for i in tqdm(range(100), desc="Loading....", ascii = False, ncols = 75):
        time.sleep(0.09)
    print("Loading Done!")

if __name__ == "__main__":
   loading()


  '''
  Loading and unloading simulator per terminal, 
  excellent to implement in applications that work through the terminal
  '''
