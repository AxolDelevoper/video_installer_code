import os
import random
import time
import json


class Logger:
    def __init__(self, action, status, exp = None, data = None):
        self.__status = status
        self.__exp = str(exp),
        self.__action = action

        self.__log_form = {
            'status': self.__status,
            'action': self.__action,
            'time': time.time(),
            'exp': self.__exp or 'None',
            'video_data': data
        }

        self._writer

    @property
    def _writer(self):
        try:
            with open(f'../logs/log_{random.randint(1,9999999999)}.json', 'w+') as file:
                json.dump({'logs': self.__log_form}, file, indent=4)

        except FileNotFoundError:
            with open(f'./logs/log_{random.randint(1, 9999999999)}.json', 'w+') as file:
                json.dump({'logs': self.__log_form}, file, indent=4)

