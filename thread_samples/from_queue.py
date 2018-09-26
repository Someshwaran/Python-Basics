from queue import Queue
from threading import Thread, current_thread

def do_stuff(q):
  print(' type ',type(q))
  print('current thread ',current_thread().getName())
  while True:
    print(q.get())
    q.task_done()

q = Queue(maxsize=0)
num_threads = 10

for i in range(num_threads):
  worker = Thread(target=do_stuff,name=str(i)+' thread', args=(q,))
  worker.setDaemon(True)
  worker.start()

for x in range(100):
  q.put(x)

q.join()