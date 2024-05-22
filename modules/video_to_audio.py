import os
import sys
from moviepy.editor import VideoFileClip

from modules.logger import Logger


class Audio_Work:
      ALLOWED_FORMATS = ['mp3', 'wav', 'wma', 'mpeg2', 'ape']

      def __init__(self, video_file, output_ext):
            self.__video_file = video_file
            self.__output_ext = output_ext
            self.__file_path = f'../videos/{video_file}'

            self.allowed_form

      def convert_video_to_audio_moviepy(self):
            filename, ext = os.path.splitext(self.__video_file)
            clip = VideoFileClip(self.__file_path)
            clip.audio.write_audiofile(f"../audio/{filename}.{self.__output_ext}")

            return Logger('Convert video to audio', 'successfully', Exception)

      @property
      def allowed_form(self):
            for form in self.ALLOWED_FORMATS:
                  if self.__output_ext == form.lower():
                        self.convert_video_to_audio_moviepy()
                        return Logger('Convert video to audio (form checker)', 'successfully', Exception)

                  else:
                        return Logger('raise runtime error', 'error', Exception)


if __name__ == "__main__":
      name = '123.mp4'
      Audio_Work(name, 'mp3')


