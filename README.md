# Image Downloader for Unsplash

This Python script allows you to download images from Unsplash based on a list of titles provided in a CSV file. The script uses the Unsplash API to search for images and download them to a specified folder.

## Features

- **Download Images**: Downloads images from Unsplash based on titles.
- **Customizable Filters**: Apply filters for orientation, color, query, and more.
- **Progress Tracking**: Displays download progress using a progress bar.

## Prerequisites

Before running the script, ensure you have the following:

- **Python 3.x**: The script is written in Python 3.
- **Requests Library**: For making HTTP requests.
- **tqdm Library**: For displaying the progress bar.

## Setup

1. **Get Unsplash API Key**:
   - Sign up at [Unsplash](https://unsplash.com/developers) and create an app to get your Access Key.
   - Replace the `UNSPLASH_ACCESS_KEY` variable in the script with your Access Key.

2. **Prepare Your CSV File**:
   - Create a CSV file named `downloadlist.csv` in the same directory as the script.
   - Ensure the CSV file contains titles in the first column.

3. **Create Download Folder**:
   - The script will automatically create a folder named `downloaded_images` to save the images.

## Usage

1. **Configure Script**:
   - Open the script and set optional filters as needed:
     - `orientation`: Image orientation (e.g., 'landscape', 'portrait', 'squarish').
     - `color`: Optional color filter (e.g., 'black', 'blue').
     - `query`: Custom search query (e.g., 'nature').
     - `page`: Page number of results (default is 1).
     - `per_page`: Number of results per page (max is 30).
     - `featured`: Whether to filter for featured images (True/False).

2. **Run the Script**:
   - Execute the script using Python.

## Example

1. **CSV File (`downloadlist.csv`)**:
   - Nature
   - Technology
   - Food

2. **Run the Script**:
   - Execute the script to start downloading images.

3. **Result**:
   - Images matching the titles in the CSV file will be downloaded to the `downloaded_images` folder.

## Code Overview

- **`download_image(url, folder_path, image_name)`**: Downloads and saves an image from a URL.
- **`parse_csv(file_path)`**: Parses a CSV file to extract titles.
- **`search_and_download_images(titles, folder_path, orientation, color, query, page, per_page, featured)`**: Searches for images on Unsplash and downloads them.

## Troubleshooting

- **API Key Issues**: Ensure your Unsplash Access Key is valid and correctly placed in the script.
- **CSV File Format**: Verify that the CSV file has titles in the first column and is correctly formatted.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Contributing

Feel free to open issues or pull requests for improvements or bug fixes.

---

For more information on the Unsplash API, refer to the [Unsplash API Documentation](https://unsplash.com/documentation).
