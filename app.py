import streamlit as st
import smtplib
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pytube import YouTube
from pytube import Search
from youtube_search import YoutubeSearch
import moviepy.editor as mp
import pydub
from pydub import AudioSegment
import os

st.set_page_config("Mashup ❄️")
st.title("Mashup ❄️")

def download_videos(n, x):
    # Create a directory to store the videos
    if not os.path.exists("Videos"):
        os.mkdir("Videos")

    # Search for videos of the singer
    query = x + " songs"
    s = Search(query)
    searchResults = {}
    i = 0
    for v in s.results:
        if i <n and v.length < 1200:
            try:
                searchResults[v.title] = v.watch_url
                youtubeObject = YouTube(v.watch_url)
                youtubeObject = youtubeObject.streams.get_highest_resolution().download(
                    output_path='Videos', filename=f"video{i+1}.mp4")
                print(f"Downloaded video {i + 1}: {v.title}")
                i = i+1
            except:
                print("error occured")


def convertToAudio(duration, n):
    if not os.path.exists("Audios"):
        os.mkdir("Audios")
    for i in range(n):
        clip = mp.VideoFileClip(f"Videos/video{i+1}.mp4").subclip(0, duration)
        clip.audio.write_audiofile(f"Audios/audio{i+1}.mp3")

def makeMashup(n):
    audio_clips = [mp.AudioFileClip(
        f"Audios/audio{i+1}.mp3") for i in range(0, n)]
    final_clip = mp.concatenate_audioclips(audio_clips)
    final_clip.export(f"combined.mp3", format="mp3")

def sendMail(recp):
    # Email details
    sender = 'noordeepk2002@gmail.com'
    recipient = recp
    password = 'yhofghzgsaktuuqg'
    subject = 'Mash up'
    # Create the message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    # Add the text
    text = MIMEText(f'Please find attached the mashed up audio file of {singer}')
    msg.attach(text)
    # Add the audio file
    audi = MIMEAudio(open('output.mp3', 'rb').read(), 'mp3')
    msg.attach(audi)
    # Send the email
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender, password)
    smtp.sendmail(sender, recipient, msg.as_string())
    smtp.quit()

singer = st.text_input("Name of the singer:")
n = st.number_input("Number of Videos:", min_value=2, max_value=18)
m = st.number_input("Duration of each Audio Clip (in seconds):", min_value=20, max_value=90)
recp = st.text_input("Email ID:")
bt1 = st.button("Send Mail")
if bt1:
    with st.spinner('Preparing Audio... (this may take upto a few minutes)'):
        try:
            download_videos(n,singer)
            convertToAudio(m,n)
            makeMashup(n)
            sendMail(recp)
            st.success('Your file was mailed successfully!')
        except:
            st.error("Too much traffic at the moment, please try again in a few minutes")