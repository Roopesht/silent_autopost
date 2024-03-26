import os
import cv2
import random
import textwrap
from moviepy.editor import VideoFileClip, AudioFileClip
from PIL import Image, ImageFont, ImageDraw
from getShortestLength import get_shortest_length
import numpy as np
import json

class VideoSettings:
    def __init__(self):
        self.project_directory = "C:/Projects/silent_autopost/Docs/Example"
        self.output_video_path = os.path.join(self.project_directory, "Temp/output.mp4")
        self.temp_frame_path = os.path.join(self.project_directory, "Temp/frame.jpg")
        self.font_path = "C:/Projects/silent_autopost/Engine/Utils/ProximaNovaSemibold.otf"
        self.video_with_music_path = os.path.join(self.project_directory, "Temp/video_with_music.mp4")
        self.cap = None
        self.videowriter = None
        self.frame_path = os.path.join(self.project_directory, "Temp/frame.jpeg")
        self.auxx_path = os.path.join(self.project_directory, "Temp/auxx.jpeg")
        self.video_file = None
        self.sound_file = None
        self.large_text = None
        self.small_text = None

    def load_settings(self, scene_definition):
        self.large_text = scene_definition["large_text"]
        self.small_text = scene_definition["small_text"]
        self.sound_file = get_random_sound_file("", self)
        self.video_file = get_random_video_file(self)
        return self


def add_subtitle(settings: VideoSettings, background, main_text="text", author="author"):
    # Configurable variables
    stroke_color = (0, 0, 0)
    font_color = (255, 255, 255)

    # Function to center the text
    def center_wrap(text, char_width=80, **kwargs):
        lines = textwrap.wrap(text, **kwargs)
        return "\n".join(line.center(char_width) for line in lines)

    # Wrap the text
    main_text = center_wrap(main_text, char_width=40, width=40)

    # Get the width and height of the background image
    width, height = background.width, background.height

    # Draw the background image
    draw = ImageDraw.Draw(background)

    # Set the font size and stroke width
    font_size = int(35 * width / 720)
    stroke_width = int(3 * width / 720)

    # Set the font
    font = ImageFont.truetype(settings.font_path, font_size)

    # Get the width and height of the text
    xy = (0, 0)
    box = draw.multiline_textbbox(xy, main_text, font=font)

    # Calculate the x and y coordinates of the text (centered horizontally and vertically)
    x = (width - box[2]) / 2
    y = ((height - box[3]) / 2) - (height * 700 / 3840)

    # Draw the text
    draw.multiline_text(
        (x, y),
        main_text,
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
    author_x = x + box[2] - author_box_width - 30
    author_y = y + box[3] + author_box_height + 30

    # Draw the author text on the image
    draw_author = ImageDraw.Draw(background)
    draw_author.text(
        (author_x, author_y),
        "- " + author,
        font=font,
        align="center",
        fill=font_color,
        stroke_width=stroke_width,
        stroke_fill=(15, 15, 15),
    )

    return background


def get_random_sound_file(filename, settings):
    sound_folder_path = os.path.join(settings.project_directory, "Sounds")
    sound_files = [f for f in os.listdir(sound_folder_path) if os.path.isfile(os.path.join(sound_folder_path, f))]
    random_sound_file = random.choice(sound_files)
    return os.path.join(sound_folder_path, random_sound_file)


def get_random_video_file(settings):
    video_folder_path = os.path.join(settings.project_directory, "Videos")
    video_files = [f for f in os.listdir(video_folder_path) if os.path.isfile(os.path.join(video_folder_path, f))]
    random_video_file = random.choice(video_files)
    return os.path.join(video_folder_path, random_video_file)


def process_scene(settings: VideoSettings):
    settings.sound_file = get_random_sound_file("", settings)
    settings.video_file = get_random_video_file(settings)
    if settings.video_file:
        open_video(settings)
    
    counter = 0
    while settings.cap.isOpened():
        ret, frame = settings.cap.read()
        counter += 1
        if ret and counter < 50:
            frame_pil = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_pil)
            frame_with_text = add_subtitle(
                settings, frame_pil, settings.large_text, settings.small_text
            )
            frame_with_text = cv2.cvtColor(np.array(frame_with_text), cv2.COLOR_RGB2BGR)
            settings.videowriter.write(frame_with_text)
            print("processing frame ", counter)
        else:
            break


def open_video(settings: VideoSettings):
    cap = cv2.VideoCapture(settings.video_file)
    settings.cap = cap


def get_video_writer(settings: VideoSettings):
    fps = 24
    height = 3840
    width = 2160
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(settings.output_video_path, fourcc, fps, (width, height))
    settings.videowriter = out


def make_video(video_definition):
    settings = VideoSettings()
    if os.path.exists(settings.output_video_path):
        os.remove(settings.output_video_path)
    get_video_writer(settings)

    for scene in video_definition["scenes"]:
        settings.load_settings(scene)
        process_scene(settings)

    settings.cap.release()
    settings.videowriter.release()

    video = VideoFileClip(settings.output_video_path)
    audio = AudioFileClip(settings.sound_file)
    final_video = video.set_audio(audio)
    final_video.write_videofile(settings.video_with_music_path)
    shortest_length = get_shortest_length(settings.video_file, settings.sound_file)
    print("shortest length ", shortest_length)

    output_path = os.path.join(settings.project_directory, "Output")
    os.makedirs(output_path, exist_ok=True)
    output_file = os.path.join(output_path, str(video_definition["video_id"]) + ".mp4")
    os.rename(settings.video_with_music_path, output_file)


if __name__ == "__main__":
    videos = json.load(open("./videogenerator/data.json"))
    for video in videos:
        make_video(video)

    print("Video created successfully!")
