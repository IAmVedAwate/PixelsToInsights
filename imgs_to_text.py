import os
import cv2
import pytesseract
import multiprocessing
import time  # Import the time module
import python_preprocessor as py_pr

import os
import shutil

# Record the start time at the beginning
start_time = time.time()

# Initialize the OCR engine (if using Tesseract)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Specify the path to the directory containing the extracted frames
frame_directory = r'D:\Ved_Project_Work\Mini_Project\temp2'

# Get a list of all the image files in the directory
image_files = [os.path.join(frame_directory, filename) for filename in os.listdir(frame_directory) if filename.endswith('.png')]
# Function to extract text from a set of images
def extract_text_from_images(image_set):
    extracted_texts = []
    for image_path in image_set:
        try:
            image = cv2.imread(image_path)
            extracted_text = pytesseract.image_to_string(image, lang='consolas')
            extracted_texts.append(f"{extracted_text}\n")
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")
    return extracted_texts

if __name__ == "__main__":
    # Specify the number of parallel processes (sets of images) you want to process simultaneously
    num_processes = 12  # You can adjust this value as needed
    image_sets = []
    # Split the image files into sets for parallel processing
    try:
        image_sets2 = [image_files[i:i + len(image_files) // num_processes] for i in range(0, len(image_files), len(image_files) // num_processes)]
        image_sets = image_sets2
    except:
        num_processes = 6  # You can adjust this value as needed
        image_sets2 = [image_files[i:i + len(image_files) // num_processes] for i in range(0, len(image_files), len(image_files) // num_processes)]
        image_sets = image_sets2
        
    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Use the pool to extract text from multiple sets of images in parallel
    results = pool.map(extract_text_from_images, image_sets)

    # Close the pool of worker processes
    pool.close()
    pool.join()

    # Specify the path to the text file where you want to append the extracted text
    text_file_path = r'D:\Ved_Project_Work\Mini_Project\text_file\extracted_text.txt'

    # Append the extracted text to the text file
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        for result in results:
            for extracted_text in result:
                extracted_text2= py_pr.python_detector(extracted_text)
                text_file.write(extracted_text2)
                text_file.write("((((((((((&&&&&))))))))))\n")


    
    directory_path = r'D:\Ved_Project_Work\Mini_Project\temp2'
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' and its contents have been deleted.")
    else:
        print(f"Directory '{directory_path}' does not exist.")
        
    directory_path = r'D:\Ved_Project_Work\Mini_Project\temp3'
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' and its contents have been deleted.")
    else:
        print(f"Directory '{directory_path}' does not exist.")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    print(f"Extracted text has been appended to {text_file_path}")
