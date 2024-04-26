import json
import os
import dropbox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Dropbox access token from environment variable
ACCESS_TOKEN = os.getenv("dropbox_access_token")

# Initialize Dropbox client
dbx = dropbox.Dropbox(ACCESS_TOKEN)

def generate_data_video(topic, input_data, template, scenes):
    # Construct the JSON content with scenes
    data = {
        "topic": topic,
        
    }
    return json.dumps(data)

def write_to_file(data):
    # Write the data to data_video.json file
    with open('data_video.json', 'w') as file:
        file.write(data)

def upload_to_dropbox(file_path, access_token):
    # Connect to Dropbox
    dbx = dropbox.Dropbox(access_token)   

    # Upload the file to Dropbox
    with open(file_path, 'rb') as f:
        dbx.files_upload(f.read(), '/data_video.json')


def create_data_video_json(topic, context):
    topic = """
[
  {
    "video_id": "1",
    "topic": "improve mindset",
    "bgm_type": "uplifting music",
    "description": "This video is about how constructive thinking can help you become an achiever. The context is mindset for peak performance. The mood of the video is reassurance.",
    "voice": "Male",
    "tags": ["mindset", "peak performance", "constructive thinking"],
    "scenes": [
      {
        "scene_id": "1",
        "scene_type": "video",
        "duration": "2",
        "large_text": "Who took away your success?",
        "small_text": "",
        "entry_transition": "fade in",
        "exit_transition": "fade out",
        "audio_text": "Today, we're exploring shifting from a scarcity mindset to one of abundance.",
        "font": "ProximaNovaSemibold.otf",
        "background_image": "",
        "background_video_type": "rain drops"
      }
    ]
  },
]
    """
    prompt = f"""
You are a youtube video content creator. You have created many videos which has gone viral. Your focus will be on how to make the video widely acceptable. The content and voice must be catchy in the first scenes, as first 5 seconds are very important, especially the first scene, start with a intriguing question, or question the status quo. End of the video, there must a satisfaction of watching the video. 
Please provide the content for the video with below details:
Topic: "{topic}", 
Context: "{context}"
Mood of video: "Reassurance"

Considerations: The large_text should have fewer words, easy to read and catchy.

Use both large and small text overlays along with voiceover narration. Maintain a consistent background music throughout. 

Provide the output in the below format.
Possible values for the fields are as follows:
- scene_type: video, image
    """


  

#def send_email(subject, body, from_email, to_email, password):
    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def main():
    # Parameters
    topic = "success"
    input_data = "Your input data"
    template = "Your template"

    def generate_data_video(topic, input_data, template):
     
    
    # Define scenes
     scenes = [
        {
            "scene_id": "1",
            "scene_type": "video",
            "duration": "5",
            "large_text": "strangely life gets harder when you try to make it easy",
            "small_text": "",
            "entry_transition": "fade in",
            "exit_transition": "fade out",
            "audio_text": "Today, we're exploring shifting from a scarcity mindset to one of abundance.",
            "font": "ProximaNovaSemibold.otf",
            "background_image": "",
            "background_video_type": "foam"
        },
        {
            "scene_id": "2",
            "scene_type": "video",
            "duration": "5",
            "large_text": "Exercising might be hard but never moving makes life harder",
            "small_text": "Discover the Power of Constructive Thinking",
            "entry_transition": "fade in",
            "exit_transition": "fade out",
            "audio_text": "Let's dive deep into the strategies that can unleash your true potential.",
            "font": "ProximaNovaSemibold.otf",
            "background_image": "",
            "background_video_type": "honey"
        },
        {
            "scene_id": "3",
            "scene_type": "video",
            "duration": "5",
            "large_text": "Uncomfortable conversations are hard but avoiding every conflict make it harder",
            "small_text": "Transform Your Mindset, Transform Your Life",
            "entry_transition": "fade in",
            "exit_transition": "fade out",
            "audio_text": "It's time to break the chains holding you back and embrace a mindset of limitless possibilities.",
            "font": "ProximaNovaSemibold.otf",
            "background_image": "",
            "background_video_type": "squeezing"
        }
        # Add more scenes as needed
    ]

def generate_data_video(topic, input_data, template):
    
    

    # Construct the JSON content
    data = {
        "video_id": "1",
        "topic": topic,
        "bgm_type": "short music",
        "description": "This video is about how constructive thinking can help you become an achiever. The context is mindset for peak performance. The mood of the video is reassurance.",
        "voice": "Male",
        "tags": ["mindset", "peak performance", "constructive thinking"],
        "scenes": "scenes"
    }
    return json.dumps(data)


    
    # Parameters
    topic = "success"
    input_data = "Your input data"
    template = "Your template"

    # Generate data_video.json content
    json_content = generate_data_video(topic, input_data, template)

    # Write content to file
    write_to_file(json_content)

    # Upload file to Dropbox
    upload_to_dropbox('data_video.json', ACCESS_TOKEN) 

    # Send email
    email_subject = "New file uploaded to Dropbox"
    email_body = "The file data_video.json is uploaded to Dropbox. Please check the file."
    sender_email = "peakperformance728@gmail.com"
    sender_password = "eixy oaaf tyfc byvo"
    recipient_email = "roopesht@gmail.com"

    #send_email(email_subject, email_body, sender_email, recipient_email, sender_password)

if __name__ == "__main__":
    main()

# Generate data_video.json content
json_content = generate_data_video("success", "Your input data", "Your template")

    # Write content to file
write_to_file(json_content)

    # Upload file to Dropbox
upload_to_dropbox('data_video.json', ACCESS_TOKEN) 

    # Send email
email_subject = "New file uploaded to Dropbox"
email_body = "The file data_video.json is uploaded to Dropbox. Please check the file."
sender_email = "peakperformance728@gmail.com"
sender_password = "eixy oaaf tyfc byvo"
recipient_email = "roopesht@gmail.com"
send_email(email_subject, email_body, sender_email, recipient_email, sender_password)

if __name__ == "__main__":
    main()
