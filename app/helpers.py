import json
from shapely.geometry import Point


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
