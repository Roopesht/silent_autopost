import os
import pickle
import logging
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

class UploadSettings:
    def __init__(self, filepath, title="My Test Video", description="Description of my test video", tags=["tag1", "tag2", "tag3"]):
        self.filepath = filepath
        self.title = title
        self.description = description
        self.tags = tags

def authenticate():
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        "videogenerator/client_secrets.json", scopes=scopes
    )
    flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
    authorization_url, _ = flow.authorization_url(access_type='offline', prompt='consent')

    print('Please go to this URL: {}'.format(authorization_url))
    authorization_code = input('Enter the authorization code: ')

    flow.fetch_token(code=authorization_code)
    credentials = flow.credentials

    with open('youtube_credentials.pickle', 'wb') as token:
        pickle.dump(credentials, token)

    return credentials

def load_credentials():
    if os.path.exists('youtube_credentials.pickle'):
        with open('youtube_credentials.pickle', 'rb') as token:
            credentials = pickle.load(token)
        return credentials
    else:
        return authenticate()
    

def upload_video(settings: UploadSettings, credentials=None):
    if credentials is None:
        credentials = load_credentials()
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

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
        logging.info("Video uploaded successfully! Video ID: %s", video_id)
        return video_id
    except googleapiclient.errors.HttpError as e:
        logging.error("An HTTP error occurred: %s", e)
        return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    video_path = "C:/Projects/silent_autopost/Docs/Example/Videos/16.mp4"  # Adjust the path format for consistency
    video_title = "My Test Video"
    video_description = "Description of my test video"
    video_tags = ["tag1", "tag2", "tag3"]

    credentials = None

    upload_settings = UploadSettings(video_path, video_title, video_description, video_tags)
    upload_video(upload_settings, credentials)
