from threading import Thread
import queue
import traceback


def print_exc():
    traceback.print_exc()
    traceback.print_stack()


class ZThread(Thread):
    """
    ZMD custom thread
    """

    def __init__(self, queue_in, name):
        Thread.__init__(self)
        self.name = name
        self.queue_func = queue_in
        print("Init thread:", self.name)

    def run(self):
        while 1:
            try:
                func, args, kwargs = self.queue_func.get()
                func(*args, **kwargs)
            except:
                print_exc()
            finally:
                pass


class ZThreadPool(object):
    """
    ZMD custom threadpool
    """

    def __init__(self, num_workers, size_max, name):
        self.queue_func = queue.Queue(maxsize=size_max)

        list_thread = []
        for idx_worker in range(num_workers):
            thread_new = ZThread(
                queue_in=self.queue_func,
                name="{}.{}".format(name, idx_worker),
            )
            thread_new.start()
            list_thread.append(thread_new)

    def submit(self, func, *args, **kwargs):
        self.queue_func.put((func, args, kwargs))
