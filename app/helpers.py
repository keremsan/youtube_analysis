import json
from shapely.geometry import Point

from app.constants import CATEGORY_NAMES as categories


def check_point_in_polygon(point, polygon):
    return polygon.contains(point)


def filter_wrong_location(videos, country_polygon):
    video_point = None
    true_count, false_count, null_count = 0, 0, 0
    for video in videos:
        location = video.get('location')
        if location:
            video_lat = location.get('latitude')
            video_long = location.get('longitude')
            if video_lat and video_long:
                video_point = Point(video_lat, video_long)

            
        
        if video_point and check_point_in_polygon(video_point, country_polygon):
            correct_videu.append(video)

    return true_count, false_count, null_count


def read_data_from_file(path):
    data_file = open(path, 'r')
    data_txt = data_file.read()
    data = json.loads(data_txt)

    return data


def write_data_to_file(path):
    with open(path, 'w') as _file:
        _file.write(json.dumps(after_corona_amerika))


def fetch_category_name(video):
    category_id = video['categoryId']
    category_name = categories[category_id]

    return category_name


def simplify_videos_data(videos, required_properties):
    simplified_video_list = []

    for video in videos:
        simplified_video = {}
        for key, properties in required_properties.items():
            video_property_values = video.get(key)
            for _property in properties:
                simplified_video[_property] = video_property_values.get(_property)

        category_name = fetch_category_name(simplified_video)
        simplified_video['categoryName'] = category_name

        simplified_video_list.append(simplified_video)

    return simplified_video_list
