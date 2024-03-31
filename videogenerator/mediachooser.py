import random
import os
from videosettings import VideoSettings
from dropboxapi import download_file_by_tag
import sys


def get_random_sound_file(filename, settings: VideoSettings):        
    sound_folder_path = os.path.join(settings.project_directory, "Sounds")
    sound_files = [
        f
        for f in os.listdir(sound_folder_path)
        if os.path.isfile(os.path.join(sound_folder_path, f))
    ]
    random_sound_file = random.choice(sound_files)
    return os.path.join(sound_folder_path, random_sound_file)



def get_random_video_file_old(settings: VideoSettings, scene):
    scene_videos = {
        "nature": "nature.mp4",
            "healthy food": "healthy food.mp4",
            "exercise": "exercise.mp4",
            "relaxation":"relaxation.mp4",
            "sleeping":"sleeping.mp4" 
        # Add more scene types and corresponding video files as needed
    }

    video_folder_path = os.path.join(settings.project_directory, "Videos")
    try:
        random_video_file = scene_videos [scene['background_video_type']]
        return os.path.join(video_folder_path, random_video_file)
    except KeyError:
        random_video_file = None
    return None

def get_random_video_file(settings: VideoSettings, scene):
    tag = scene['background_video_type']
    tag = "raindrops"
    try:
        temppath = os.path.join(settings.project_directory, "Temp", f"{tag}.mp4")
        # Delete temp.mp4 if it exists
        if not os.path.exists(temppath):
            if not download_file_by_tag(tag, temppath):
                print (f"File with tag {tag} not found")
                sys.exit(1)
                return None

        return temppath
    except Exception as e:
        print (f"Video with tag {tag} is not found!")
        random_video_file = None
        sys.exit(1)
    return None
 
def get_random_image_file (settings: VideoSettings, scene):
    images = {
        "lion": "lion.jpg",
    }

    image_folder_path = os.path.join(settings.project_directory, "Images")
    try:
        random_image_file = images[scene['background_image_type']]
        return os.path.join(image_folder_path, random_image_file)
    except KeyError:
        random_image_file = None
    return None