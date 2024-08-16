import os
import requests
import csv
from tqdm import tqdm

# Unsplash API credentials
UNSPLASH_ACCESS_KEY = ''

def download_image(url, folder_path, image_name):
    """
    Downloads an image from the given URL and saves it to the specified folder with the given image name.
    """
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(os.path.join(folder_path, image_name), 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded image: {image_name}")
        else:
            print(f"Failed to download image from {url}, status code: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred while downloading image from {url}: {e}")

def parse_csv(file_path):
    """
    Parses a CSV file to extract a list of titles.
    Assumes titles are in the first column of the CSV file.
    """
    titles = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                titles.append(row[0])  # Assuming titles are in the first column
        print(f"Loaded {len(titles)} titles from CSV file.")
    except Exception as e:
        print(f"Exception occurred while reading CSV file: {e}")
    return titles

def search_and_download_images(titles, folder_path, orientation=None, color=None, query=None, page=1, per_page=10, featured=False):
    """
    Searches for images on Unsplash based on the given titles and downloads them.
    Optional filters can be applied for orientation, color, query, page, per_page, and featured.
    """
    headers = {
        'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}'
    }

    for title in tqdm(titles, desc="Searching and downloading images"):
        # Construct search URL with filters
        search_url = f'https://api.unsplash.com/search/photos?query={title}&orientation={orientation}&color={color}&page={page}&per_page={per_page}&featured={featured}'
        
        response = requests.get(search_url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                img_url = data['results'][0]['urls']['regular']  # URL for the regular size image
                image_name = f"{title.replace(' ', '_')}.jpg"
                print(f"Downloading image from {img_url}")
                download_image(img_url, folder_path, image_name)
            else:
                print(f"No images found for {title}.")
        else:
            print(f"Failed to search for images with status code: {response.status_code}")

if __name__ == "__main__":
    # Path to the CSV file containing the list of titles
    csv_file_path = 'downloadlist.csv'
    # Path to the folder where images will be downloaded
    download_folder_path = 'downloaded_images'
    
    # Create the download folder if it doesn't exist
    if not os.path.exists(download_folder_path):
        os.makedirs(download_folder_path)
    
    # Parse the CSV file to get the list of titles
    titles = parse_csv(csv_file_path)
    
    # Optional filters for image search
    orientation = None  # Options: 'landscape', 'portrait', 'squarish'
    color = None        # Optional color filter (e.g., 'black', 'blue', 'red', etc.)
    query = None        # Custom search query (e.g., 'nature', 'technology')
    page = 1            # Page number (default is 1)
    per_page = 10       # Number of results per page (max is 30)
    featured = False    # Whether to filter for featured images (True/False)
    
    # Search for images and download them
    search_and_download_images(titles, download_folder_path, orientation, color, query, page, per_page, featured)