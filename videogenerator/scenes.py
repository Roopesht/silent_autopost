import cv2
import numpy as np
from PIL import Image
from subtitles import SubtitleAdder
from videosettings import VideoSettings

def getSceneProcessor (scenetype: str, settings):
    if scenetype == "video":
        return VideoSceneProcessor(settings)
    elif scenetype == "image":
        return ImageSceneProcessor(settings)
    else:
        raise ValueError("Invalid scene type") 

class SceneProcessor:
    def __init__(self, settings: VideoSettings):
        self.settings = settings
    
    def __enter__(self):
        self.cap = cv2.VideoCapture(self.settings.video_file)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.cap.release()
    
    def process(self):
        raise NotImplementedError("Subclasses must implement process_scene method")

class VideoSceneProcessor(SceneProcessor):
    def process(self):
        counter = 0
        self.cap = cv2.VideoCapture(self.settings.video_file)
        while self.cap.isOpened():
            flag, frame = self.cap.read()
            counter += 1
            if flag and counter < self.settings.duration * 10: # change 24 to self.settings.fps
                frame_pil = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_pil = Image.fromarray(frame_pil)
                titles = SubtitleAdder(self.settings, frame_pil)
                frame_with_text = titles.add_subtitle(self.settings.large_text, self.settings.small_text)
                frame_with_text = cv2.cvtColor(np.array(frame_with_text), cv2.COLOR_RGB2BGR)
                self.settings.videowriter.write(frame_with_text)
                print("processing frame ", counter)
            else:
                break

class ImageSceneProcessor(SceneProcessor):
    def process(self):
        # Implement processing for image scenes
        pass
