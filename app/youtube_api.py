from googleapiclient.discovery import build

from app.constants import YOUTUBE_API_KEY

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
search_api = youtube.search()
videos_api = youtube.videos()
video_categories_api = youtube.videoCategories()


def get_categories():
    category_ids = ','.join([str(cid) for cid in list(range(45))])
    list_parameters = {
        'part': 'snippet',
        'id': category_ids,
    }

    categories = video_categories_api.list(**list_parameters).execute()
    categories = {category['id']:category['snippet']['title'] for 
                  category in categories['items']}

    return categories


def search_videos(query_string, from_date, to_date, location, radius, page_token=None):
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
    if page_token:
        list_parameters['pageToken'] = page_token

    videos = search_api.list(**list_parameters).execute()

    return videos


def search_all_videos(query_string, from_date, to_date, location, radius, page_token=None):
    all_search_data = []
    for i in range(90):
        search_data = search_videos(
            query_string,
            from_date,
            to_date,
            location,
            radius,
            page_token=page_token
        )

        print(page_token, search_data['pageInfo'], len(search_data['items']))
        all_search_data.append(search_data)

        page_token = search_data.get('nextPageToken')
        if not page_token or len(search_data['items']) == 0:
            return all_search_data

    return all_search_data


def get_video_ids_from_search_data(search_data):
    video_ids = [data['id']['videoId'] for data in search_data['items']]
    video_ids_str = ','.join(video_ids)

    return video_ids_str


def get_videos_from_search_data(search_data):
    video_ids = get_video_ids_from_search_data(search_data)

    list_parameters = {
        'id': video_ids,
        'part': 'snippet,contentDetails,statistics,recordingDetails'
    }

    videos = videos_api.list(**list_parameters).execute()

    return videos


def get_videos_from_search_data_list(search_datas):
    all_videos = []
    for search_data in search_datas:
        videos = get_videos_from_search_data(search_data)
        all_videos.extend(videos['items'])

    return all_videos
