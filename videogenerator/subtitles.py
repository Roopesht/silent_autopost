import textwrap
from PIL import ImageDraw, ImageFont
from videosettings import VideoSettings



class SubtitleAdder:
    def __init__(self, settings: VideoSettings, background):
        self.settings = settings
        self.background = background
        self.stroke_color = (0, 0, 0)
        self.font_color = (255, 255, 255)
    
    def center_wrap(self, text, char_width=80, **kwargs):
        lines = textwrap.wrap(text, **kwargs)
        return "\n".join(line.center(char_width) for line in lines)
    
    def get_text_style(self, width):
        font_size = int(35 * width / 720)
        stroke_width = int(3 * width / 720)
        font = ImageFont.truetype(self.settings.font_path, font_size)
        return font, stroke_width
    
    def get_position(self, horizontal_pos, vertical_pos, width, height):
        x = ((width - horizontal_pos) / 2) - (width * 30 / 720)
        y = ((height + vertical_pos) / 2) + (height * 30 / 3840)
        return x, y
    
    def add_main_text(self, main_text, font, stroke_width, width, height):
        draw = ImageDraw.Draw(self.background)
        main_text = self.center_wrap(main_text, char_width=40, width=40)
        xy = (0, 0)
        box = draw.multiline_textbbox(xy, main_text, font=font)
        x = (width - box[2]) / 2
        y = ((height - box[3]) / 2) - (height * 700 / 3840)
        draw.multiline_text(
            (x, y),
            main_text,
            font=font,
            align="center",
            fill=self.font_color,
            stroke_width=stroke_width,
            stroke_fill=self.stroke_color,
        )
    
    def add_author(self, author, font, stroke_width, position):
        draw = ImageDraw.Draw(self.background)
        draw.text(
            position,
            "- " + author,
            font=font,
            align="center",
            fill=self.font_color,
            stroke_width=stroke_width,
            stroke_fill=(15, 15, 15),
        )
    
    def add_subtitle(self, main_text="text", author="author"):
        width, height = self.background.width, self.background.height
        font, stroke_width = self.get_text_style(width)
        self.add_main_text(main_text, font, stroke_width, width, height)
        author_font = font
        author_position = self.get_position(30, 30, width, height)
        self.add_author(author, author_font, stroke_width, author_position)
        return self.background
