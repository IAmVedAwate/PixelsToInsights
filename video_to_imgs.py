import os
import requests
import mimetypes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import preprocessing as pr

# # Measure the execution time for the following block of code
start_time = time.time()


# def get_redirected_url(url):

#     # Send a HEAD request to get the final URL after following redirections
#     response = requests.head(url, allow_redirects=True)
#     return response.url

# def download_with_progress(url, save_path):
#     # Get the final redirected URL
#     final_url = get_redirected_url(url)
    
#     # Send a HEAD request to get the file size
#     response_head = requests.head(final_url)
#     content_length_header = response_head.headers.get('content-length')
    
#     if content_length_header is None:
#         print("Content-Length header not provided. Unable to determine download progress.")
#         return
    
#     total_size = int(content_length_header)
    
#     # Initialize the progress bar
#     progress_bar_length = 50
#     print("Downloading...")
#     print("[{}] 0%".format(" " * progress_bar_length), end='\r')
    
#     # Download the file with progress tracking
#     response = requests.get(final_url, stream=True)
#     with open(save_path, 'wb') as file:
#         chunk_size = 1024  # 1 KB
#         downloaded_size = 0
#         for chunk in response.iter_content(chunk_size=chunk_size):
#             if chunk:
#                 file.write(chunk)
#                 downloaded_size += len(chunk)
#                 # Calculate the download progress percentage
#                 progress = int(progress_bar_length * downloaded_size / total_size)
#                 print("[{}{}] {}%".format("=" * progress, " " * (progress_bar_length - progress), int(downloaded_size / total_size * 100)), end='\r')
#     print("\nDownload complete!")

# # Specify the path to the Brave browser executable for Windows
# brave_browser_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'

# # Set up the Brave browser options
# brave_options = webdriver.ChromeOptions()
# brave_options.binary_location = brave_browser_path

# # Add any other options you may need, such as specifying a download directory
# brave_options.add_argument('--disable-extensions')
# brave_options.add_argument('--disable-gpu')
# brave_options.add_argument('--disable-dev-shm-usage')
# brave_options.add_argument('--headless')  # You can remove this line if you want to run the browser in a visible window

# # Initialize the web driver with Brave options
# driver = webdriver.Chrome(options=brave_options)

# # Open the YouTube link with 'ss' prefix
# video_url = 'https://www.ssyoutube.com/watch?v=ADV-AjAXHdc&list=WL&index=3&t=25s'
# driver.get(video_url)

# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time for HEADLESS Browser to open: {execution_time:.2f} seconds")

# # Wait for the redirect to complete (10 seconds after the redirect, adjust the wait time as needed)
# WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.download-icon')))

# # Find the download link (anchor tag) by its class name
# download_link = driver.find_element(By.CSS_SELECTOR, '.download-icon')

# # Get the href attribute of the download link
# download_url = download_link.get_attribute('href')

# # Download the file using the requests library
# response = requests.get(download_url)

# # Determine the file extension based on the content type (MIME type)
# content_type = response.headers.get('Content-Type')
# file_extension = mimetypes.guess_extension(content_type)

# # Specify the directory where you want to save the downloaded file
# download_directory = r'D:\Ved_Project_Work\prac\videos'

# # Generate a unique file name with the determined extension
# file_name = 'downloaded_video' + file_extension
# file_path = os.path.join(download_directory, file_name)

# # Download the file with progress tracking
# download_with_progress(download_url, file_path)

# # # Save the downloaded content to the file
# # with open(file_path, 'wb') as file:
# #     file.write(response.content)

# # Close the browser when done
# driver.quit()

# from pytube import YouTube

# # Replace 'youtube_video_url' with the URL of the YouTube video you want to download
# youtube_video_url = 'https://www.youtube.com/watch?v=ogsRn1XSy5c&pp=ygUbcHl0aG9uIGdyYXBoaWNzIDUgbWluIHZpZGVv'

# # Create a YouTube object
# yt = YouTube(youtube_video_url)

# # Get the highest resolution stream available
# video_stream = yt.streams.get_highest_resolution()

# # Optional: Set the download path (default is the current working directory)
# download_path = r'D:\Ved_Project_Work\Mini_Project\videos'
# print("Download Start.....")
# downloaded_file_path = video_stream.download(download_path)

# # Rename the downloaded file
# new_file_name = 'downloaded_video123123.mp4'  # Replace with your desired new file name
# new_file_path = os.path.join(download_path, new_file_name)

# # Check if the downloaded file exists
# if os.path.exists(downloaded_file_path):
#     # Rename the file
#     os.rename(downloaded_file_path, new_file_path)
#     print(f"File renamed to '{new_file_name}'")
# else:
#     print("Downloaded file not found.")
# print("Download completed!")


import os
import cv2

# Specify the path to the directory where you want to save the extracted frames
output_directory = r'D:\Ved_Project_Work\Mini_Project\photos'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Open the video file
video_path = r"D:/Ved_Project_Work/Mini_Project/videos/downloaded_video.mp4"
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Specify the frame rate (frames per second) for extracting frames
frame_rate = 50  # Change this value as needed

frame_number = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    
# Create the output directory if it doesn't exist
    if not os.path.exists("D:/Ved_Project_Work/Mini_Project/temp2"):
        os.makedirs("D:/Ved_Project_Work/Mini_Project/temp2")
    if not os.path.exists("D:/Ved_Project_Work/Mini_Project/temp3"):
        os.makedirs("D:/Ved_Project_Work/Mini_Project/temp3")    
        
    # Save the frame as an image in the specified output directory
    frame_filename = os.path.join(output_directory, f'frame_{frame_number:04d}.png')
    cv2.imwrite(frame_filename, frame)
    pr.preprocessor(frame_filename,f'temp3/inverted{frame_number:04d}.png')
    
    frame_number += 1
    
    # Skip frames to achieve the desired frame rate
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number * frame_rate)

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()

# # Delete the video file
# if os.path.exists(video_path):
#     os.remove(video_path)
#     print('Video file deleted successfully.')
# else:
#     print('Video file does not exist.')

# Measure the execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for downloading: {execution_time:.2f} seconds")
