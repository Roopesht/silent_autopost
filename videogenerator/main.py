import os
from moviepy.editor import VideoFileClip, AudioFileClip
import json
from videosettings import VideoSettings
import mediachooser 
from scenes import VideoSceneProcessor, getSceneProcessor
from utils import get_video_writer, cut_video, rename_final_output
from youtube_upload import upload_video, UploadSettings, load_credentials

def add_audio_to_video(settings: VideoSettings):
    video = VideoFileClip(settings.output_video_path)
    audio = AudioFileClip(settings.sound_file)
    final_video = video.set_audio(audio)
    final_video.write_videofile(settings.video_with_music_path)

def make_video(video_definition):
    settings = VideoSettings()
    settings.remove_old_files()
    get_video_writer(settings)
    #getSceneProcessor("splash", settings).process()

    for scene in video_definition["scenes"]:
        settings.load_settings(scene)
        settings.video_file = mediachooser.get_random_video_file(settings,scene)
        settings.image_file = mediachooser.get_random_image_file(settings, scene)
        settings.sound_file = mediachooser.get_random_sound_file("", settings)
        
        with getSceneProcessor (settings.scene_type, settings) as processor:
            processor.process()

    settings.cleanup()
    add_audio_to_video(settings)
    #cut_video(settings)
    
    file_name = rename_final_output(settings, str(video_definition["video_id"]), sum_duration(video_definition))
    upload_video_helper(file_name, video_definition)
    settings.delete_temp_files()

def sum_duration(video_definition):
    duration = 0
    for scene in video_definition["scenes"]:
        duration += int(scene["duration"])
    return duration

def upload_video_helper(file_name, video_def: VideoSettings):
    settings = UploadSettings(file_name, video_def ["topic"] , video_def ["description"], video_def ["description"])
    if input("Press C to upload the video to YouTube Shorts") == "C":
        credentials = load_credentials()
        video_id = upload_video(settings, credentials)
        return video_id
    else:
        print("Video not uploaded to YouTube Shorts")

if __name__ == "__main__":
    videos = json.load(open("./videogenerator/data_video.json"))
    for video in videos:
        make_video(video)
