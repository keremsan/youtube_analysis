TURKEY_LOCATION = '39.0, 35.0'
TURKEY_RADIUS = '750km'
TURKEY_VIDEOS_PATH_BEFORE = '../data/turkey_before.txt'
TURKEY_VIDEOS_PATH_AFTER = '../data/turkey_after.txt'

USA_LOCATION = '39.009730,-99.662595'
USA_RADIUS = '2500km'
USA_VIDEOS_PATH_BEFORE = '../data/usa_before.txt'
USA_VIDEOS_PATH_AFTER = '../data/usa_after.txt'

REQUIRED_PROPERTIES = {
    'snippet': ['publishedAt', 'title', 'categoryId'],
    'contentDetails': ['duration'],
    'statistics': ['viewCount', 'likeCount', 'dislikeCount', 'favoriteCount', 'commentCount'],
    'recordingDetails': ['location']
}
