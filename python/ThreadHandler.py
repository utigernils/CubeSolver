import threading
import time

filename = "ThreadHandler.py"

class threadManager:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.threads = []
        self.is_running = False
        self.thread_functions = []

    def threadWorker(self, thread_id, user_function, *args, **kwargs):
        while self.is_running:
            user_function(thread_id, *args, **kwargs)
            time.sleep(1)

    def linkThreadFunction(self, user_function):
        if not self.is_running:
            self.thread_functions.append(user_function)
            print(filename + f": Function linked for threading: {user_function.__name__}")

    def startThreads(self, user_function=None):
        if user_function:
            self.linkThreadFunction(user_function)

        if not self.is_running and self.thread_functions:
            self.is_running = True
            for i, user_function in enumerate(self.thread_functions):
                thread = threading.Thread(target=self.threadWorker, args=(i, user_function))
                thread.start()
                self.threads.append(thread)
            print(filename + f": {len(self.thread_functions)} threads started.")

    def stopThreads(self):
        if self.is_running:
            print(filename + f": Stopping threads...")
            self.is_running = False
            for thread in self.threads:
                thread.join()
            print(filename + f": All threads stopped.")
            self.threads = []



