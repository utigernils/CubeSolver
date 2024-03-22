import threading

import time

class ThreadManager:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.threads = []
        self.is_running = False
        self.thread_functions = []

    def thread_worker(self, thread_id, user_function, *args, **kwargs):
        while self.is_running:
            user_function(thread_id, *args, **kwargs)
            time.sleep(1)

    def link_thread_function(self, user_function):
        if not self.is_running:
            self.thread_functions.append(user_function)
            print(f"Function linked for threading: {user_function.__name__}")

    def start_threads(self, user_function=None):
        if user_function:
            self.link_thread_function(user_function)

        if not self.is_running and self.thread_functions:
            self.is_running = True
            for i, user_function in enumerate(self.thread_functions):
                thread = threading.Thread(target=self.thread_worker, args=(i, user_function))
                thread.start()
                self.threads.append(thread)
            print(f"{len(self.thread_functions)} threads started.")

    def stop_threads(self):
        if self.is_running:
            print("Stopping threads...")
            self.is_running = False
            for thread in self.threads:
                thread.join()
            print("All threads stopped.")
            self.threads = []



