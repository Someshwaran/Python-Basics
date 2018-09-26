import queue

def _input():
    print('in the _input')
    q  = queue.Queue()
    for value in range(1,7):
        q.put(value)
    return q
def _output(q):
    print('in the _output')
    # print(' queue ',q.empty())
    while not q.empty():
        print(q.get())
        # q.task_done()
        

def main():
    q_value = _input()
    _output(q_value)

if __name__ == '__main__':
    main()
