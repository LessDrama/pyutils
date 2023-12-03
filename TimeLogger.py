import time


class TimeLogger:
    def __enter__(self):
        self.t = time.time()
        return self


    def __exit__(self, type, value, traceback):
        print('Execution time: {:.2f} с'.format(time.time() - self.t))
