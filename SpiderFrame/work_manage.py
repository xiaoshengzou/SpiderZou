# -*-coding:utf-8-*-

import Queue
import threading
import time

class WorkManager(object):
    def __init__(self, thread_num):
        self.work_queue = Queue.Queue()
        self.threads = []
        self.__init_thread_pool(thread_num)
        # self.__init_work_queue()
    """
        init threading
    """
    def __init_thread_pool(self,thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))

    # """
    #     init work queue
    # """
    # def __init_work_queue(self, jobs_num=0):
    #     for i in range(jobs_num):
    #         self.add_job(do_job, i)

    """
        add a job in queue
    """
    def add_job(self, func, *args):
        #任务入队，Queue内部实现了同步机制
        self.work_queue.put((func, list(args)))
   
    """
        check the rest of queue
    """
    def check_queue(self):
        return self.work_queue.qsize()

    """
        wait all threading done
    """   
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()

class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        #死循环，从而让创建的线程在一定条件下关闭退出
        while True:
            try:
                do, args = self.work_queue.get(block=True)#任务异步出队，Queue内部实现了同步机制
                do(args)
                self.work_queue.task_done()#通知系统任务完成
            except Exception,e:
                print str(e)
                break