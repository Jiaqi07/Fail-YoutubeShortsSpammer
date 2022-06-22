import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload


def run():
    CLIENT_SECRET_FILE = 'ClientSecretFile.json'  # Private INFO
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    upload_date_time = datetime.datetime(2022, 6, 24, 16, 30, 0).isoformat() + '.000Z'

    request_body = {
        'snippet': {
            'categoryI': 20,
            'title': 'Which cat hit the juul best? #shorts',
            'description': 'Hope you enjoyed!',
            'tags': ['Cat', 'Animal', 'Memes', 'Cute', 'Funny', 'Happy', 'Dogs', 'Nature', 'Minecraft', 'Fortnite',
                     'Valorant', 'Tenz', 'VCT', 'NBA', 'Kendrick Lamar', 'bot']
        },
        'status': {
            'privacyStatus': 'private',
            'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload("WhichCatHitJuul.mp4")

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()
