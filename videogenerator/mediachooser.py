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



def get_random_video_file(settings: VideoSettings, scene):
    scene_videos = {
        "inspiring landscapes": "inspiring landscapes.mp4",
        "mountain climb": "mountain climb.mp4",
        "people facing obstacles": "people facing obstacles.mp4",
        "empowering mentorship": "empowering mentorship.mp4",
        "achievement of success": "achievement of success.mp4"
        # Add more scene types and corresponding video files as needed
    }

    video_folder_path = os.path.join(settings.project_directory, "Videos")
    random_video_file = scene_videos [scene['background_video_type']]
    
    return os.path.join(video_folder_path, random_video_file)
