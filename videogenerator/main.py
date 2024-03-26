import os
import cv2
import time
import random
import textwrap
from cutVideo import cut_video
from PIL import Image, ImageFont, ImageDraw
from getShortestLength import get_shortest_length
from moviepy.editor import VideoFileClip, AudioFileClip
import numpy as np
import json
class videoSettings:
    def __init__(self):
        self.project_directory = "C:/Projects/silent_autopost/Docs/Example"
        self.output_video_path = os.path.join(self.project_directory, "Temp/output.mp4")
        self.temp_frame_path = os.path.join(self.project_directory, "Temp/frame.jpg")
        self.font_path = "C:/Projects/silent_autopost/Engine/Utils/ProximaNovaSemibold.otf"
        self.video_with_music_path = os.path.join(
            self.project_directory, "Temp/video_with_music.mp4"
        )
        self.cap = None
        self.videowriter = None
        self.frame_path = os.path.join(self.project_directory, "Temp/frame.jpeg")
        self.auxx_path = os.path.join(self.project_directory, "Temp/auxx.jpeg") 
        self.video_file = None
        self.sound_file = None
        self.large_text = None
        self.small_text = None

    def get_settings(self, scene_definition):
        self.large_text = scene_definition['large_text']
        self.small_text = scene_definition['small_text']
        self.sound_file = get_sound_file("", self)
        self.video_file = get_video_file(self)

        return self


def add_subtitle(
    settings: videoSettings,
    bg,
    text="text",
    author="author",
    ):
    # Configurable variables
    stroke_color = (0, 0, 0)
    font_color = (255, 255, 255)


    # Function to center the text
    def center_wrap(text, cwidth=80, **kw):
        lines = textwrap.wrap(text, **kw)
        return "\n".join(line.center(cwidth) for line in lines)

    # Wrap the text
    text = center_wrap(text, cwidth=40, width=40)

    # Get the width and height of the background image
    W, H = bg.width, bg.height

    # Draw the background image
    draw = ImageDraw.Draw(bg)

    # Set the font size and stroke width
    font_size = int(35 * W / 720)
    stroke_width = int(3 * W / 720)

    # Set the font
    font = ImageFont.truetype(settings.font_path, font_size)

    # Get the width and height of the text
    xy = (0, 0)
    box = draw.multiline_textbbox(xy, text, font=font)

    # Calculate the x and y coordinates of the text (centered horizontally and vertically)
    # (x,y) is top left corner of the text
    x = (W - box[2]) / 2
    y = ((H - box[3]) / 2) - (H * 700 / 3840)

    # Draw the text
    draw.multiline_text(
        (x, y),
        text,
        font=font,
        align="center",
        fill=font_color,
        stroke_width=stroke_width,
        stroke_fill=stroke_color,
    )

    # Get the width and height of the author text
    author_box_width = draw.textbbox((0, 0), author, font=font)[2]
    author_box_height = draw.textbbox((0, 0), author, font=font)[3]

    # Calculate the x and y coordinates of the author text (centered horizontally and vertically)
    # (author_x,author_y) is top left corner of the author text
    author_x = x + box[2] - author_box_width - 30
    author_y = y + box[3] + author_box_height + 30

    # Draw the author text on the image opened
    drawAuthor = ImageDraw.Draw(bg)
    drawAuthor.text(
        (author_x, author_y),
        "- " + author,
        font=font,
        align="center",
        fill=font_color,
        stroke_width=stroke_width,
        stroke_fill=(15, 15, 15),
    )

    # Return the final image
    return bg

def get_sound_file(filename, settings):
    
    sound_folder_path = os.path.join(settings.project_directory, "Sounds")
    sound_files = [
        f
        for f in os.listdir(sound_folder_path)
        if os.path.isfile(os.path.join(sound_folder_path, f))
    ]
    random_sound_file = random.choice(sound_files)

    # Get the path to the random file
    sound_file = os.path.join(sound_folder_path, random_sound_file)
    return sound_file

def get_video_file(settings):
    videos_path = "Videos"
    video_folder_path = os.path.join(settings.project_directory, videos_path)
    video_files = [
        f
        for f in os.listdir(video_folder_path)
        if os.path.isfile(os.path.join(video_folder_path, f))
    ]
    random_video_file = random.choice(video_files)
    video_file = os.path.join(video_folder_path, random_video_file)
    return video_file

def process_scene(settings: videoSettings):
    settings.sound_file = get_sound_file("", settings)
    settings.video_file = get_video_file(settings)
    if settings.video_file:
        open_video(settings)
    # if video is present then open the video

    counter = 0
    # Read frames from video and add text
    while settings.cap.isOpened():
        ret, frame = settings.cap.read()
        counter += 1
        if ret and counter < 50:
            # Convert frame to PIL Image
            frame_pil = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_pil)
            # Add the text to the frame
            frame_with_text = add_subtitle(settings, frame_pil, settings.large_text, settings.small_text)
            # frame_with_text.save(settings.temp_frame_path)
            # Convert frame back to OpenCV format
            frame_with_text = cv2.cvtColor(np.array(frame_with_text), cv2.COLOR_RGB2BGR)
            # Write the frame to the output file
            settings.videowriter.write(frame_with_text)
            print ("processing frame ", counter)
        else:
            break

def open_video(settings: videoSettings):
    # Load the video
    cap = cv2.VideoCapture(settings.video_file)
    settings.cap = cap

def get_video_writer(settings: videoSettings):
    # Get the frame rate of the video
    fps = 24 #cap.get(cv2.CAP_PROP_FPS)
    height = 3840 # 2160 # 1080 #cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = 2160 # 608 # 1920 #cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(
        settings.output_video_path, fourcc, fps, (width, height))
    settings.videowriter = out

def make_video(video_definition):
    settings = videoSettings()
    # Delete the output video if it already exists
    if os.path.exists(settings.output_video_path):
        os.remove(settings.output_video_path)
    get_video_writer(settings)

    for scene in video_definition['scenes']:
        settings.get_settings(scene)
        process_scene(settings)

    # Release the objects
    settings.cap.release()
    settings.videowriter.release()

    # Load the video clip
    video = VideoFileClip(settings.output_video_path)

    # Load the audio clip
    audio = AudioFileClip(settings.sound_file)

    # Overlay the audio on the video
    final_video = video.set_audio(audio)

    # Write the final video to disk
    final_video.write_videofile(settings.video_with_music_path)
    shortest_length = get_shortest_length(settings.video_file, settings.sound_file)
    print ("shortest length ", shortest_length)

    # Cut the video to the shortest length
    """
    cut_video(
        settings.video_with_music_path,
        shortest_length,
        settings.video_with_music_path,
    )
    """

    cv2.destroyAllWindows()
    # Copy the video to the output folder with the name as "id.mp4"
    output_path = os.path.join(settings.project_directory, "Output")
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, str(video_definition['video_id']) + ".mp4")
    os.rename(settings.video_with_music_path, output_file)
    

if __name__ == "__main__":
    # read the json file from data.json, get the structure for the video
    videos = json.load(open("./videogenerator/data.json"))
    for video in videos:
        make_video(video)

    print("Video created successfully!")