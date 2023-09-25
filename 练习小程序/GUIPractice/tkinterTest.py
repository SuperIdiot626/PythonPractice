import sys
import time
import multiprocessing as mp
import multiprocessing.queues as mpq
from threading import Thread
from tkinter import *


class StdoutQueue(mpq.Queue):

    def __init__(self, *args, **kwargs):
        ctx = mp.get_context()
        super(StdoutQueue, self).__init__(*args, **kwargs, ctx=ctx)

    def write(self,msg):
        self.put(msg)

    def flush(self):
        sys.__stdout__.flush()
        
        
def text_catcher(text_widget,queue):
    while True:
        text_widget.insert(END, queue.get())


def test_child(q):
    sys.stdout = q
    print('child running')



##############################

def run_in_thread(fun):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fun, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper


#@run_in_thread
def test_parent(q):
    sys.stdout = q
    print('parent running')
    time.sleep(5.)
    mp.Process(target=test_child, args=(q,)).start()

#############################

if __name__ == '__main__':
    gui_root = Tk()
    gui_txt = Text(gui_root)
    gui_txt.pack()
    q = StdoutQueue()
    gui_btn = Button(gui_root, text='Test', command=lambda: test_parent(q),)
    gui_btn.pack()

    monitor = Thread(target=text_catcher, args=(gui_txt, q))
    monitor.daemon = True
    monitor.start()

    gui_root.mainloop()