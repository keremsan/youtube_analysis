def check_point_in_polygon(point, polygon):
    return polygon.contains(point)


def filter_wrong_location(videos, country_polygon):
    correct_video = []
    for video in videos['items']:
        recording_details = video['recordingDetails']
        video_lat = recording_details['location']['latitude']
        video_long = recording_details['location']['longitude']
        video_point = Point(video_lat, video_long)

        if check_point_in_polygon(video_point, country_polygon):
            correct_video.append(video)

    return video


def normalize_video_data(videos):
    for video in videos['items']:

