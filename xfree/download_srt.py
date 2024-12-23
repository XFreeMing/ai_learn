import requests

def download_srt(url, save_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Open a file to write the SRT content
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"SRT downloaded successfully and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading SRT: {e}")
download_srt(
    'https://www.coursera.org/api/subtitleAssetProxy.v1/7y34Hn7RTZSt-B5-0T2ULg?expiry=1729987200000&hmac=YMBTzwwpFGobwczq0YbJ1LYNoIGonkmnXpus2WtXE8o&fileExtension=vtt',
    'C:\\Users\\xiaolt1\\pythonWorkspace\\ai_learn\\xfree\\mls\\downloaded_videos\\Week_1__Introduction_to_Machine_Learning\\welcome-to-machine-learning\\welcome-to-machine-learning.srt'
    
)  