import os

api_key = 'rkGqu2zVkHwmfGkOmEMgaWu2OIiCs0xtvZMd57K3kxvMlDV8IH8UlbtK'

import requests
import sys
import os

video_trans_table = {
    "rain drops": "Raindrops falling into puddle",
    "mountain view": "River Stream On A Bed Of Rocks",
    "open sky": "River Stream On A Bed Of Rocks",
    "nature path": "River Stream On A Bed Of Rocks",
    "success":  "River Stream On A Bed Of Rocks",
    "rain drops leaves": "Close-up of plant with leaves during rain"
}

def download_pexels_video(query, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.join(folder, f"{query}.mp4")
    if os.path.exists(filename):
        return filename
    if query not in video_trans_table:
        print(f"Query '{query}' not found in the translation table.")
        sys.exit(1)
    pexel_query = video_trans_table.get(query)
    
    if not fetch_pexels_video(pexel_query, filename):
        return filename
    return None
    

def fetch_pexels_video(query, filename ):
    per_page=1
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
                with open(filename, 'wb') as f:
                    f.write(video_data.content)
                print(f"Video '{video_title}' downloaded successfully!")
                return filename
                
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

if __name__ == "__main__":
    download_pexels_video = fetch_pexels_video("eagle", ".")
    print(downloaded_video_info)  # Print information about the downloaded video
