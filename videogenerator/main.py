import os
import cv2
import random
import textwrap
from moviepy.editor import VideoFileClip, AudioFileClip
from PIL import Image, ImageFont, ImageDraw
from videosettings import VideoSettings
from getShortestLength import get_shortest_length
import numpy as np
from subtitles import SubtitleAdder
import json


def get_random_sound_file(filename, settings):        
    sound_folder_path = os.path.join(settings.project_directory, "Sounds")
    sound_files = [
        f
        for f in os.listdir(sound_folder_path)
        if os.path.isfile(os.path.join(sound_folder_path, f))
    ]
    random_sound_file = random.choice(sound_files)
    return os.path.join(sound_folder_path, random_sound_file)


def get_random_video_file(settings):
    video_folder_path = os.path.join(settings.project_directory, "Videos")
    video_files = [
        f
        for f in os.listdir(video_folder_path)
        if os.path.isfile(os.path.join(video_folder_path, f))
    ]
    random_video_file = random.choice(video_files)
    return os.path.join(video_folder_path, random_video_file)


def process_scene(settings: VideoSettings):
    settings.sound_file = get_random_sound_file("", settings)
    settings.video_file = get_random_video_file(settings)
    if settings.video_file:
        open_video(settings)

    counter = 0
    while settings.cap.isOpened():
        flag, frame = settings.cap.read()
        counter += 1
        if flag and counter < 50:
            frame_pil = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_pil)
            titles = SubtitleAdder(settings, frame_pil)
            frame_with_text = titles.add_subtitle(
                settings.large_text, settings.small_text
            )
            frame_with_text = cv2.cvtColor(np.array(frame_with_text), cv2.COLOR_RGB2BGR)
            settings.videowriter.write(frame_with_text)
            print("processing frame ", counter)
        else:
            break


def open_video(settings: VideoSettings):
    cap = cv2.VideoCapture(settings.video_file)
    settings.cap = cap


def get_video_writer(settings: VideoSettings):
    fps = 24
    height = 3840
    width = 2160
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(settings.output_video_path, fourcc, fps, (width, height))
    settings.videowriter = out


def add_audio_to_video(settings: VideoSettings):
    video = VideoFileClip(settings.output_video_path)
    audio = AudioFileClip(settings.sound_file)
    final_video = video.set_audio(audio)
    final_video.write_videofile(settings.video_with_music_path)


def remove_old_files(settings: VideoSettings):
    try:
        os.remove(settings.output_video_path)
        os.remove(settings.temp_frame_path)
    except:
        pass


def cut_video(settings):
    shortest_length = get_shortest_length(settings.video_file, settings.sound_file)
    print("shortest length ", shortest_length)


def rename_finaloutput(settings: VideoSettings, video_id):
    output_path = os.path.join(settings.project_directory, "Output")
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, video_id + ".mp4")
    os.rename(settings.video_with_music_path, output_file)


def delete_temp_files(settings: VideoSettings):
    try:
        os.remove(settings.output_video_path)
    except:
        pass
    try:
        os.remove(settings.temp_frame_path)
    except:
        pass


def make_video(video_definition):
    settings = VideoSettings()
    remove_old_files(settings)
    get_video_writer(settings)

    for scene in video_definition["scenes"]:
        settings.load_settings(scene)
        process_scene(settings)

    settings.cleanup()
    add_audio_to_video(settings)
    cut_video(settings)
    rename_finaloutput(settings, str(video_definition["video_id"]))
    delete_temp_files(settings)


if __name__ == "__main__":
    videos = json.load(open("./videogenerator/data.json"))
    for video in videos:
        make_video(video)

    print("Video created successfully!")
