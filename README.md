# Mashup ❄️

Mashup ❄️ is a web application that allows you to create music mashups by combining audio clips from YouTube videos of your favorite singers. With Mashup ❄️, you can download multiple audio clips, truncate them to a specified duration, and then merge them into a single audio file, resulting in a unique music mashup.

## Table of Contents
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [How to Use](#how-to-use)
- [Important Notes](#important-notes)

## Getting Started

To get started with Mashup ❄️, make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Next, you'll need to install the required Python libraries by running the following command in your terminal or command prompt:

```
pip install streamlit smtplib pytube youtube_search moviepy pydub
```

## Dependencies

Mashup ❄️ relies on the following Python libraries:

- streamlit: For creating the web application interface.
- smtplib: For sending emails with the combined audio file.
- pytube: For downloading YouTube videos.
- youtube_search: For searching YouTube videos.
- moviepy: For editing video and audio files.
- pydub: For working with audio files.

## How to Use

1. Clone the repository to your local machine or download the code as a ZIP file.

2. Install the required Python dependencies, as mentioned in the "Getting Started" section.

3. Open a terminal or command prompt and navigate to the project's directory.

4. Run the Streamlit application using the following command:
   ```
   streamlit run app.py
   ```
5. The web application should now be running locally.

6. In the application, enter the name of the singer, the number of videos to consider (between 10 and 60), the duration of each audio clip (between 20 and 90 seconds), and the recipient's email address.

7. Click the "Send Mail" button to start the audio preparation process. The application will download the specified number of audio clips from YouTube, truncate them to the specified duration, combine them into a mashup, and then send the mashup audio file as an email attachment to the recipient's email address.

## Important Notes
- The email functionality in the application is currently using a Gmail account for sending emails. Please replace "your_sender_email@gmail.com" and "your_sender_password" in the sendMail() function with your Gmail email address and password.

- The application may take a few minutes to process and prepare the audio, especially if you are downloading and combining a large number of videos.
