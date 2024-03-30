import os
import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
from videosettings import VideoSettings
from mediachooser import get_random_sound_file, get_random_video_file
from getShortestLength import get_shortest_length
from cutVideo import cut_video

def get_video_writer(settings: VideoSettings):
    fps = 24
    settings.height = 1920 #3840
    settings.width = 1080 #2160
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(settings.output_video_path, fourcc, fps, (settings.width, settings.height))
    settings.videowriter = out


def rename_final_output(settings: VideoSettings, video_id, duration=60):
    output_path = os.path.join(settings.project_directory, "Output")
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, video_id + ".mp4")
    # if output_file exists, delete it
    try:
        os.remove(output_file)
    except:
        pass

    cut_video(settings.video_with_music_path,        duration,        output_file    )
    #os.rename(settings.video_with_music_path, output_file)
    return output_file


