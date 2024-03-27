import os
import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
from videosettings import VideoSettings
from mediachooser import get_random_sound_file, get_random_video_file
from getShortestLength import get_shortest_length
def get_video_writer(settings: VideoSettings):
    fps = 24
    height = 1920 #3840
    width = 1080 #2160
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(settings.output_video_path, fourcc, fps, (width, height))
    settings.videowriter = out

def cut_video(settings):
    shortest_length = get_shortest_length(settings.video_file, settings.sound_file)
    print("shortest length ", shortest_length)

def rename_final_output(settings: VideoSettings, video_id):
    output_path = os.path.join(settings.project_directory, "Output")
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, video_id + ".mp4")
    os.rename(settings.video_with_music_path, output_file)

