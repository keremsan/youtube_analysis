from googleapiclient.discovery import build

import time
import json

youtube_api_key = 'AIzaSyB9UlGN9HNGavKUHxXPYngBy3IGKhwduPs'
youtube = build('youtube', 'v3', developerKey=youtube_api_key)

from_date = '2019-03-01T00:00:00Z'
to_date = '2019-11-30T00:00:00Z'
search_api = youtube.search()
videos_api = youtube.videos()
video_categories_api = youtube.videoCategories()

location = '39.0, 35.0'
location_radius = '600km'
query_string = ''

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


def fetch_category_names(videos):
    categories = get_categories()

    for video in videos:
        category_id = video['categoryId']
        category_name = categories[category_id]
        video['categoryName'] = category_name

    return videos


def simplify_videos_data(videos, required_properties):
    videos = fetch_category_names(videos)

    simplified_video_list = []
    for video in videos:
        simplified_video = {}
        for key, properties in required_properties.items():
            video_property_values = video.get(key)
            for _property in properties:
                simplified_video[_property] = video_property_values.get(_property)
        simplified_video_list.append(simplified_video)

    return simplified_video_list
