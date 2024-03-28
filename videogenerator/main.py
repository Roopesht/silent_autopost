import os
from moviepy.editor import VideoFileClip, AudioFileClip
import json
from videosettings import VideoSettings
from mediachooser import get_random_sound_file, get_random_video_file
from scenes import VideoSceneProcessor, getSceneProcessor
from utils import get_video_writer, cut_video, rename_final_output

def add_audio_to_video(settings: VideoSettings):
    video = VideoFileClip(settings.output_video_path)
    audio = AudioFileClip(settings.sound_file)
    final_video = video.set_audio(audio)
    final_video.write_videofile(settings.video_with_music_path)

def make_video(video_definition):
    settings = VideoSettings()
    settings.remove_old_files()
    get_video_writer(settings)

    for scene in video_definition["scenes"]:
        settings.load_settings(scene)
        settings.video_file = get_random_video_file(settings,scene)
        settings.sound_file = get_random_sound_file("", settings)
        
        with getSceneProcessor (settings.scene_type, settings) as processor:
            processor.process()

    settings.cleanup()
    add_audio_to_video(settings)
    cut_video(settings)
    rename_final_output(settings, str(video_definition["video_id"]))
    settings.delete_temp_files()

if __name__ == "__main__":
    videos = json.load(open("./videogenerator/data.json"))
    for video in videos:
        make_video(video)

    print("Video created successfully!")
