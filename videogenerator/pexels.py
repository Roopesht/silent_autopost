import os

api_key = 'rkGqu2zVkHwmfGkOmEMgaWu2OIiCs0xtvZMd57K3kxvMlDV8IH8UlbtK'

import requests
import os

def fetch_pexels_video(query, api_key, save_dir='videos', per_page=1):
    url = f"https://api.pexels.com/videos/search?query={query}&per_page={per_page}&orientation=portrait"
    headers = {"Authorization": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            videos = data.get("videos", [])
            if videos:
                video_url = videos[0]['video_files'][0]['link']  # Get the URL of the first video
                video_title = videos[0]['id']  # Use video ID as the title
                video_data = requests.get(video_url)
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                with open(os.path.join(save_dir, f"{video_title}.mp4"), 'wb') as f:
                    f.write(video_data.content)
                print(f"Video '{video_title}' downloaded successfully!")
                filename =os.path.join(save_dir, f"{video_title}.mp4")
                # rename the current file to the new name
                new_name = os.path.join(save_dir, f"{query.replace(' ', '')}.mp4")
                os.rename(filename, new_name)
                return {
                    'title': video_title,
                    'url': video_url,
                    'saved_path':  new_name,
                    'query': query,
                }
            else:
                print("No videos found for the given query.")
                return None
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Fetch and download a stock video related to nature
downloaded_video_info = fetch_pexels_video("eagle", api_key)
print(downloaded_video_info)  # Print information about the downloaded video
