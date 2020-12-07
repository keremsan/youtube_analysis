from constants import (
    REQUIRED_PROPERTIES as required_properties,
    TURKEY_LOCATION as turkey_location,
    TURKEY_RADIUS as turkey_radius,
    USA_LOCATION as usa_location,
    USA_RADIUS as usa_radius,
    TURKEY_VIDEOS_PATH_AFTER as turkey_videos_after_path,
    TURKEY_VIDEOS_PATH_BEFORE as turkey_videos_before_path,
    USA_VIDEOS_PATH_AFTER as usa_videos_after_path,
    USA_VIDEOS_PATH_BEFORE as usa_videes_before_path,
)
from helpers import write_data_to_file
from youtube_api import search_all_videos, get_videos_from_search_data_list, simplify_videos_data

from_date_before = '2019-03-01T00:00:00Z'
to_date_before = '2019-11-30T00:00:00Z'

from_date_after = '2020-03-01T00:00:00Z'
to_date_after = '2020-11-30T00:00:00Z'

query_string = ''

## USA BEFORE COVID
usa_search_data = search_all_videos(
    query_string,
    from_date_before,
    to_date_before,
    usa_location,
    usa_radius
)
usa_videos = get_videos_from_search_data_list(usa_search_data)
usa_simplified_videos = simplify_videos_data(usa_videos, REQUIRED_PROPERTIES)
write_data_to_file(usa_simplified_videos, usa_videos_path)

## TURKEY BEFORE COVID
turkey_search_data = search_all_videos(
    query_string,
    from_date_before,
    to_date_before,
    turkey_location,
    turkey_radius
)
turkey_videos = get_videos_from_search_data_list(turkey_search_data)
turkey_simplified_videos = simplify_videos_data(turkey_videos, required_properties)
write_data_to_file(turkey_simplified_videos, turkey_videos_path)



## USA AFTER COVID
usa_search_data = search_all_videos(
    query_string,
    from_date_after,
    to_date_after,
    usa_location,
    usa_radius
)
usa_videos = get_videos_from_search_data_list(usa_search_data)
usa_simplified_videos = simplify_videos_data(usa_videos, REQUIRED_PROPERTIES)
write_data_to_file(usa_simplified_videos, usa_videos_path)

## TURKEY AFTER COVID
turkey_search_data = search_all_videos(
    query_string,
    from_date_after,
    to_date_after,
    turkey_location,
    turkey_radius)
turkey_videos = get_videos_from_search_data_list(turkey_search_data)
turkey_simplified_videos = simplify_videos_data(turkey_videos, required_properties)
write_data_to_file(turkey_simplified_videos, turkey_videos_path)


