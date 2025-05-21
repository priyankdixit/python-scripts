# from pytube import YouTube

# try:
#     # Ask the user to input the YouTube URL
#     url = input("Enter the YouTube URL: ").strip()
    
#     yt = YouTube(url)
    
#     print("Title:", yt.title)
#     print("Views:", yt.views)

#     # Get the highest resolution stream
#     yd = yt.streams.get_highest_resolution()
    
#     # Download the video to the current directory
#     yd.download()
    
#     print("Download complete.")
# except Exception as e:
#     print("An error occurred:", str(e))

# pytube is broken due to a recent YouTube change, and thus switched to yt-dlp as a workaround.

import subprocess

url = input("Enter YouTube URL: ").strip()
try:
    subprocess.run(["yt-dlp", url], check=True)
    print("Download complete.")
except subprocess.CalledProcessError as e:
    print("An error occurred:", e)

