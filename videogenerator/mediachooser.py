import random
import os
from videosettings import VideoSettings

def get_random_sound_file(filename, settings: VideoSettings):        
    sound_folder_path = os.path.join(settings.project_directory, "Sounds")
    sound_files = [
        f
        for f in os.listdir(sound_folder_path)
        if os.path.isfile(os.path.join(sound_folder_path, f))
    ]
    random_sound_file = random.choice(sound_files)
    return os.path.join(sound_folder_path, random_sound_file)



def get_random_video_file(settings: VideoSettings):
    video_folder_path = os.path.join(settings.project_directory, "Videos")
    video_files = [
        f
        for f in os.listdir(video_folder_path)
        if os.path.isfile(os.path.join(video_folder_path, f))
    ]
    random_video_file = random.choice(video_files)
    return os.path.join(video_folder_path, random_video_file)
