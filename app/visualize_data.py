import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from constants import (
    TURKEY_VIDEOS_PATH_AFTER as turkey_videos_after_path,
    TURKEY_VIDEOS_PATH_BEFORE as turkey_videos_before_path,
    USA_VIDEOS_PATH_AFTER as usa_videos_after_path,
    USA_VIDEOS_PATH_BEFORE as usa_videes_before_path,
)
from helpers import read_data_from_file


## TURKEY
turkey_videos_before = read_data_from_file(TURKEY_VIDEOS_PATH_BEFORE)
turkey_videos_after = read_data_from_file(TURKEY_VIDEOS_PATH_AFTER)

turkey_before = pd.DataFrame(turkey_videos_before)
turkey_after = pd.DataFrame(turkey_videos_after)

turkey_before['publishedAt'] = pd.to_datetime(turkey_before['publishedAt'])
turkey_after['publishedAt'] = pd.to_datetime(turkey_after['publishedAt'])

turkey_before_like_count = turkey_before.copy()
turkey_after_like_count = turkey_after.copy()
turkey_before_view_count = turkey_before.copy()
turkey_after_view_count = turkey_after.copy()
turkey_before_comment_count = turkey_before.copy()
turkey_after_comment_count = turkey_after.copy()
turkey_before_dislike_count = turkey_before.copy()
turkey_after_dislike_count = turkey_after.copy()


## USA
usa_videos_before = read_data_from_file(USA_VIDEOS_PATH_BEFORE)
usa_videos_after = read_data_from_file(USA_VIDEOS_PATH_AFTER)

usa_before = pd.DataFrame(usa_videos_before)
usa_after = pd.DataFrame(usa_videos_after)

usa_before['publishedAt'] = pd.to_datetime(usa_before['publishedAt'])
usa_after['publishedAt'] = pd.to_datetime(usa_after['publishedAt'])

usa_before_like_count = usa_before.copy()
usa_after_like_count = usa_after.copy()
usa_before_view_count = usa_before.copy()
usa_after_view_count = usa_after.copy()
usa_before_comment_count = usa_before.copy()
usa_after_comment_count = usa_after.copy()
usa_before_dislike_count = usa_before.copy()
usa_after_dislike_count = usa_after.copy()
