import requests
import subprocess

def get_access_token(file_path):
    with open(file_path, 'r') as file:
        token_line = file.readline().strip()
        return token_line.split('=')[1].strip('"')

def upload_to_mixcloud(mp3_path, token_file):

    # read in the access token
    access_token = get_access_token(token_file)

    url = f"https://api.mixcloud.com/upload/?access_token={access_token}"

    # Correct form data and file upload
    data = {
        'name': 'API Upload',
        'tags-0-tag': 'Test',
        'tags-1-tag': 'API',
        # 'sections-0-chapter': 'Introduction',
        # 'sections-0-start_time': '0',
        'sections-1-artist': 'Artist Name',
        'sections-1-song': 'Song Title',
        # 'sections-1-start_time': '10',
        'description': 'My test upload'
    }

    files = {
        'mp3': (mp3_path, open(mp3_path, 'rb'), 'audio/mpeg')
    }

    response = requests.post(url, files=files, data=data)

    # Print detailed response for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code in [200, 201]:
        print("Upload successful")
    else:
        print(f"Failed to upload. Status code: {response.status_code}")
        print(f"Response: {response.text}")


def upload_with_curl(mp3_path, token_file):
    token = get_access_token(token_file)
    command = [
        'curl', '-F', f'mp3=@{mp3_path}',
        '-F', 'name=API Upload',
        '-F', 'tags-0-tag=Test',
        '-F', 'tags-1-tag=API',
        # '-F', 'sections-0-chapter=Introduction',
        # '-F', 'sections-0-start_time=0',
        '-F', 'sections-1-artist=Artist Name',
        '-F', 'sections-1-song=Song Title',
        # '-F', 'sections-1-start_time=10',
        '-F', 'description=My test upload',
        f'https://api.mixcloud.com/upload/?access_token={token}'
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)