import json
import os
import dropbox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
# GEt the access token from .env file dropbox_access_token
import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_TOKEN = os.getenv("dropbox_access_token")
# Initialize Dropbox client
print (ACCESS_TOKEN)
dbx = dropbox.Dropbox(ACCESS_TOKEN)

def generate_data_video(topic, input_data, template):
    # Use OpenAI to generate the contents of data_video.json
    # Here, you'll use the provided topic, input_data, and template to generate the JSON content
    # I'll simulate generating some JSON content for demonstration purposes
    data = {
        "topic": topic,
        "input": input_data,
        "template": template
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

def send_email(subject, body, from_email, to_email, password):
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

     # Create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login credentials
    server.login(from_email, password)

    # Send email
    server.sendmail(from_email, to_email, msg.as_string())

    # Close SMTP session
    server.quit()

def main():
    # Parameters
    topic = "success"
    input_data = "Your input data"
    template = "Your template"

    # Generate data_video.json content
    json_content = generate_data_video(topic, input_data, template)

    # Write content to file
    write_to_file(json_content)

    upload_to_dropbox('data_video.json', ACCESS_TOKEN) 

# Send email
email_subject = "Video Creation has performed best"
email_body = "video is having a problem to send."
sender_email = "peakperformance728@gmail.com"
sender_password = "eixy oaaf tyfc byvo"
recipient_email = "roopesht@gmail.com"

send_email(email_subject, email_body, sender_email, recipient_email, sender_password)
   

if __name__ == "__main__":
    main()
