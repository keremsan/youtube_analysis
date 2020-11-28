from googleapiclient.discovery import build

youtube_api_key = 'AIzaSyAoMVrb_tLnRss6ith5PgzrfZZasMvghCk'
youtube = build('youtube', 'v3', developerKey=youtube_api_key)

from_date = '2020-04-01T00:00:00Z'
to_date = '2020-05-01T00:00:00Z'
search_api = youtube.search()
videos_api = youtube.videos()
video_categories_api = youtube.videoCategories()

def get_categories():
    category_ids = ','.join(list(range(45)))
    list_parameters = {
        'part': 'snippet',
        'id': category_ids,
    }

    categories = video_categories_api.list(**list_parameters).execute()
    categories = {category['id']:category['snippet']['title'] for 
                  category in categories['items']}

    return categories


def search_videos(query_string, from_date, to_date, location, location_radius, pageToken=None):
    list_parameters = {
        'part': 'snippet',
        'type': 'video',
        'maxResults': 50,
        'order': 'viewCount',
        'q': query_string,
        'location': location,
        'locationRadius': location_radius,
        'publishedAfter': from_date,
        'publishedBefore': to_date,
    }

    videos = search_api.list(**list_parameters).execute()

    return videos


def get_video_ids_from_search_data(search_data):
    video_ids = [data['id']['videoId'] for data in search_data['items']]
    video_ids_str = ','.join(video_ids)

    return video_ids_str


def get_videos_from_search_data(search_data):
    video_ids = get_video_ids_from_search_data(search_data)

    list_parameters = {
        'id': video_ids,
        'part': 'snippet,contentDetails,statistics'
    }

    videos = videos_api.list(**list_parameters).execute()

    return videos
