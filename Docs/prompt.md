# Prompt for generating videos

I am creating a video on the topic "xxxx" related to "xxxxx". The theme of the video should be "xxxxx". I will display both large and small text on the video/image. The audio text will be read. Through out the video I will use single bgm.
The video sequencing format I want is given at the end under "Example model video". 
Please provide the scenes in this structure. The overall video length should not be more than 30 seconds.
[
  {
    "video_id": "1",
    "topic": "improve mindset",
    "scenes": [
      {
        "scene_id": "1",
        "scene_type": "video",
        "duration": "2",
        "bgm_type": "uplifting music",
        "large_text": "Mindset Matters: Shifting from Scarcity to Abundance",
        "small_text": "Swamy Vivekananda",
        "exit_transition": "fade out",
        "audio_text": "Today, we're exploring shifting from a scarcity mindset to one of abundance.",
        "font": "ProximaNovaSemibold.otf",
        "voice": "Male",
        "background_image": "",
        "background_video_type": "rain drops"
      }
    ]
  },
]
Possible values for the fields are as follows:
- scene_type: video, image
- bgm_type: Intense Music, Uplifting Music, Dramatic Music, Traditional Indian Music, Epic Music, Soothing Veena, Soothing Flute, Beach Waves, Devotional Chants, Sitar Melodies, Tabla Rhythms, Ghazals, Classical Vocals, Folk Music, Qawwali, Bhangra Beats, Rajasthani Music, Carnatic Music, Hindustani Classical


Example model video: 
1. Scene 1: Video of raindrops with the text "Mindset Matters: Shifting from Scarcity to Abundance" and "Swamy Vivekananda". The audio text is "Today, we're exploring shifting from a scarcity mindset to one of abundance."

# List of BG Music
Intense Music
Uplifting Music
Dramatic Music
Traditional Indian Music
Epic Music
Soothing Veena
Soothing Flute
Beach Waves
Devotional Chants
Sitar Melodies
Tabla Rhythms
Ghazals
Classical Vocals
Folk Music
Qawwali
Bhangra Beats
Rajasthani Music
Carnatic Music
Hindustani Classical

# List of videos
