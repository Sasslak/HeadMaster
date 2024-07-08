import sys
import time

# Loading start program

def loading(sleep=0.1, run_time=0.8):
    animation = "|/-\\"
    start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(sleep)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > run_time:
            break
    sys.stdout.write("\rDone!")