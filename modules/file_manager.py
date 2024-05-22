import os


class FileManager:
    def __init__(self):
        if not os.path.exists('./videos'):
            self.music_folder
        if not os.path.exists('./logs'):
            self.logs_folder

    @property
    def logs_folder(self):
        os.makedirs("./logs")


    @property
    def music_folder(self):
        os.makedirs("./videos")
