from datetime import datetime
import time
import datetime


class Time:
    @staticmethod
    def time_Stamp():
        time_stamp = time.time()
        s_t = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y_%b_%d_%H_%M_%p')
        return s_t




# date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
