import os
import requests
import mimetypes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Measure the execution time for the following block of code
start_time = time.time()

def get_redirected_url(url):

    # Send a HEAD request to get the final URL after following redirections
    response = requests.head(url, allow_redirects=True)
    return response.url

def download_with_progress(url, save_path):
    # Get the final redirected URL
    final_url = get_redirected_url(url)
    
    # Send a HEAD request to get the file size
    response_head = requests.head(final_url)
    content_length_header = response_head.headers.get('content-length')
    
    if content_length_header is None:
        print("Content-Length header not provided. Unable to determine download progress.")
        return
    
    total_size = int(content_length_header)
    
    # Initialize the progress bar
    progress_bar_length = 50
    print("Downloading...")
    print("[{}] 0%".format(" " * progress_bar_length), end='\r')
    
    # Download the file with progress tracking
    response = requests.get(final_url, stream=True)
    with open(save_path, 'wb') as file:
        chunk_size = 1024  # 1 KB
        downloaded_size = 0
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
                downloaded_size += len(chunk)
                # Calculate the download progress percentage
                progress = int(progress_bar_length * downloaded_size / total_size)
                print("[{}{}] {}%".format("=" * progress, " " * (progress_bar_length - progress), int(downloaded_size / total_size * 100)), end='\r')
    print("\nDownload complete!")

# Set up the Chrome options for headless mode
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)

# Initialize the web driver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Open the YouTube link with 'ss' prefix
video_url = 'https://www.yout.com/watch?v=NB5LGzmSiCs&pp=ygUPZm9yIGxvb3AgcHl0aG9u'
driver.get(video_url)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for HEADLESS Browser to open: {execution_time:.2f} seconds")

# Wait for the redirect to complete (10 seconds after the redirect, adjust the wait time as needed)
# WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.download-icon')))
# Wait for the MP4 button to be clickable
mp4_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'option-switch') and contains(text(), 'MP4')]"))
)
# Click the MP4 button
mp4_button.click()


# Find the download link (anchor tag) by its class name
download_link = driver.find_element(By.CSS_SELECTOR, '.download-icon')

# Get the href attribute of the download link
download_url = download_link.get_attribute('href')

# Download the file using the requests library
response = requests.get(download_url)

# Determine the file extension based on the content type (MIME type)
content_type = response.headers.get('Content-Type')
file_extension = mimetypes.guess_extension(content_type)

# Specify the directory where you want to save the downloaded file
download_directory = r'D:/Ved_Project_Work/Mini_Project/videos'

# Generate a unique file name with the determined extension
file_name = 'downloaded_video123123' + file_extension
file_path = os.path.join(download_directory, file_name)

# Download the file with progress tracking
download_with_progress(download_url, file_path)
time.sleep(50)
# # Save the downloaded content to the file
# with open(file_path, 'wb') as file:
#     file.write(response.content)

# Close the browser when done
driver.quit()

import os
import cv2

# Specify the path to the directory where you want to save the extracted frames
output_directory = r'D:\Ved_Project_Work\Mini_Project\photos'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Open the video file
video_path = file_path
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Specify the frame rate (frames per second) for extracting frames
frame_rate = 18  # Change this value as needed

frame_number = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save the frame as an image in the specified output directory
    frame_filename = os.path.join(output_directory, f'frame_{frame_number:04d}.jpg')
    cv2.imwrite(frame_filename, frame)
    
    frame_number += 1
    
    # Skip frames to achieve the desired frame rate
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number * frame_rate)

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()

# Delete the video file
if os.path.exists(video_path):
    os.remove(video_path)
    print('Video file deleted successfully.')
else:
    print('Video file does not exist.')

# Measure the execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time for downloading: {execution_time:.2f} seconds")
