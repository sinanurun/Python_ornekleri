import sys,time
for i in range(10,0,-1):
    time.sleep(1)
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    print(i,end="")