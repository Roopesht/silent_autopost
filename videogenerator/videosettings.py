import os

class VideoSettings:
    def __init__(self):
        self.project_directory = "C:/Projects/silent_autopost/Docs/Example"
        self.output_video_path = os.path.join(self.project_directory, "Temp/output.mp4")
        self.temp_frame_path = os.path.join(self.project_directory, "Temp/frame.jpg")
        self.font_path = "C:/Projects/silent_autopost/Engine/Utils/ProximaNovaSemibold.otf"
        self.video_with_music_path = os.path.join(self.project_directory, "Temp/video_with_music.mp4")
        self.cap = None
        self.videowriter = None
        self.auxx_path = os.path.join(self.project_directory, "Temp/auxx.jpeg")
        self.video_file = None
        self.sound_file = None
        self.large_text = None
        self.small_text = None
        self.scene_type = None
        self.duration = 0
        self.width = 0
        self.height = 0
        self.fps = 24

    def load_settings(self, scene_definition, sound_file=None, video_file=None):
        self.large_text = scene_definition["large_text"]
        self.small_text = scene_definition["small_text"]
        self.scene_type = scene_definition["scene_type"]
        self.sound_file = sound_file 
        self.video_file = video_file
        self.duration = int(scene_definition["duration"])
        return self
    def cleanup(self):
        try:
            self.videowriter.release()
        except:
            pass


    def delete_temp_files(self):
        try:
            os.remove(self.output_video_path)
        except:
            pass
        try:
            os.remove(self.temp_frame_path)
        except:
            pass


    def remove_old_files(self):
        try:
            os.remove(self.output_video_path)
        except:
            pass
        try:
            os.remove(self.temp_frame_path)
        except:
            pass

