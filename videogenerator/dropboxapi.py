import dropbox
# GEt the access token from .env file dropbox_access_token
import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_TOKEN = os.getenv("dropbox_access_token")

# Initialize Dropbox client
dbx = dropbox.Dropbox(ACCESS_TOKEN)

def download_file(file_path, save_path):
    try:
        # Download the file
        _, file_contents = dbx.files_download(file_path)

        # Save the file locally
        with open(save_path, 'wb') as f:
            f.write(file_contents.content)
        # make the file visible in windows
        return save_path
        print(f"Downloaded file: {save_path}")

    except dropbox.exceptions.ApiError as e:
        print(f"Dropbox API error: {e}")
        return None

def download_file_by_tag(tag, save_path):
    try:
        # Search for files containing the specified tag
        search_result = dbx.files_search_v2(query=f"#{tag}").matches[0]
        
        # Download the file based on the search result
        _, file_contents = dbx.files_download(search_result.metadata._value.path_display)

        # Save the file locally
        with open(save_path, 'wb') as f:
            f.write(file_contents.content)
        os.system(f"attrib +a -h {save_path}")
        
        print(f"Downloaded file: {save_path}")
        return save_path

    except dropbox.exceptions.ApiError as e:
        print(f"Dropbox API error: {e}")
        return None

if __name__ == "__main__":
    tag = 'smallwaves'
    save_path = 'downloaded_file.mp4'  # Provide the path where you want to save the downloaded file
    download_file_by_tag(tag, save_path)

    """

    # Below code is for testing purpose
    # and showing the example how to use the function
    file_path = '/videos/16.mp4'
    save_path = 'video.mp4'
    download_file(file_path, save_path)
    """