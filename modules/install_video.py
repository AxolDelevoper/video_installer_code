import os

import pytube
from pytube import YouTube

from modules.file_manager import FileManager
from modules.logger import Logger


class DownlandVideo:
    def __init__(self, link):
        self.__link = link
        self.downland()

    def downland(self):
        FileManager()

        try:
            yt = YouTube(self.__link)
        except Exception:
            return Logger('raise runtime error', 'error', Exception)

        if yt is not None:
            ys = yt.streams.get_highest_resolution()
            ys.download('./videos')
            print("Загрузка завершена!")

            return Logger('Download video', 'successfully', Exception, {
                'title': yt.title,
                'views': yt.views,
                'len': yt.length
            })

        else:
            Logger('raise runtime error', 'error')

