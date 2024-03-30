import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload

class UploadSettings:
    def __init__(self, filepath, title="", description="", tags=[]):
        if title == "":
            title = "My Test Video"
        if description == "":
            description = "Description of my test video"
        if tags == []:
            tags = ["tag1", "tag2", "tag3"]

        self.filepath = filepath
        self.title = title
        self.description = description
        self.tags = tags

def upload_video(settings: UploadSettings):
    # Set up the OAuth 2.0 flow for user authorization.
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = InstalledAppFlow.from_client_secrets_file(
        "videogenerator/client_secrets.json", scopes=scopes
    )
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    # Upload video
    request_body = {
        "snippet": {
            "title": settings.title,
            "description": settings.description,
            "tags": settings.tags,
        },
        "status": {
            "privacyStatus": "private",  # Change privacy status as needed
        },
    }
    media_file = MediaFileUpload(settings.filepath, chunksize=-1, resumable=True)
    try:
        response = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=media_file
        ).execute()
        video_id = response['id']
        print("Video uploaded successfully! Video ID:", video_id)
        return video_id
    except googleapiclient.errors.HttpError as e:
        print("An HTTP error occurred:", e)
        return None

# Example usage:
if __name__ == "__main__":
    video_path = "C:\\Projects\\silent_autopost\\Docs\\Example\\Videos\\16.mp4"  # Change to the path of your video file
    video_title = "My Test Video"
    video_description = "Description of my test video"
    video_tags = ["tag1", "tag2", "tag3"]  # List of tags for the video

    upload_video(video_path, video_title, video_description, video_tags)
