# main.py
import os
import json
from videosettings import VideoSettings
import mediachooser 
from scenes import VideoSceneProcessor, getSceneProcessor
from utils import get_video_writer, rename_final_output
from youtube_upload import upload_video, UploadSettings, load_credentials

# Pipeline statuses
PIPELINE_STATUSES = ['created', 'processing', 'completed', 'failed', 'denied', 'pending',
                     'validated', 'invalid', 'approved', 'rejected', 'uploaded', 'published', 'deleted']

def validate_video_script(video_definition):
    # Simulate validation process, can be extended
    if 'scenes' in video_definition:
        return True
    else:
        return False

def process_video_script(video_definition):
    if not validate_video_script(video_definition):
        return False
    
    make_video(video_definition)
    return True

def handle_resources(video_definition):
    # Simulate handling resources, can be extended
    if 'resources' in video_definition:
        return True
    else:
        return False

def notify_user(message):
    # Simulate notifying user, can be extended (e.g., sending email or push notification)
    print(message)

def pipeline_workflow(video_definition):
    if video_definition['status'] == 'created':
        video_definition['status'] = 'processing'
        if process_video_script(video_definition):
            video_definition['status'] = 'completed'
            if handle_resources(video_definition):
                video_definition['status'] = 'approved'
                notify_user("Video processing completed and resources handled. Video approved.")
            else:
                video_definition['status'] = 'denied'
                notify_user("Video processing completed but resources not handled. Video denied.")
        else:
            video_definition['status'] = 'failed'
            notify_user("Video processing failed.")
    else:
        notify_user("Invalid status for video processing.")

if __name__ == "__main__":
    videos = json.load(open("./videogenerator/data_video.json"))
    for video in videos:
        pipeline_workflow(video)
