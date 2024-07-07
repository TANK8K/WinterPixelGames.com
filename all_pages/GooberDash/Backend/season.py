import json
import requests
import numpy as np
import time
import datetime
from math import ceil
from all_pages.GooberDash.Backend.get_config import get_config

goober_dash_config = get_config()


def current_season(current_timestamp):
    duration, start_number, start_time = ([] for i in range(3))
    for key in goober_dash_config["metadata"]["seasons"]["season_templates"]:
        duration.append(key["duration"])
        start_number.append(key["start_number"])
        start_time.append(key["start_time"])

    index = np.searchsorted(start_time, current_timestamp)
    accumulate_start_time = start_time[index - 1]
    count = 0
    while accumulate_start_time <= current_timestamp:
        accumulate_start_time += duration[index - 1]
        count += 1
    current_season_res = start_number[index - 1] + count - 1
    return current_season_res


def season_info(season, mode):
    duration, start_number, start_time = ([] for i in range(3))
    for key in goober_dash_config["metadata"]["seasons"]["season_templates"]:
        duration.append(key["duration"])
        start_number.append(key["start_number"])
        start_time.append(key["start_time"])

    season_index = np.searchsorted(start_number, season + 1) - 1

    season_start_timestamp = (
        start_time[season_index]
        + (season - start_number[season_index]) * duration[season_index]
    )
    season_start = f"{datetime.datetime.utcfromtimestamp(season_start_timestamp):%Y-%m-%d %H:%M:%S} UTC"

    season_end_timestamp = season_start_timestamp + duration[season_index]
    season_end = f"{datetime.datetime.utcfromtimestamp(season_end_timestamp):%Y-%m-%d %H:%M:%S} UTC"

    season_duration = duration[season_index]

    if mode == "long":
        season_days = f"{season_duration // (24 * 3600)} days {season_duration % (24 * 3600) // 3600} hours"
    elif mode == "short":
        s = season_duration / (24 * 3600)
        season_days = f"{'{:.2f}'.format(s) if isinstance(s, float) else s} days"

    current_timestamp = time.time()
    if current_timestamp > season_end_timestamp:
        status = ":red[Ended]"
    else:
        status = f":green[In progress] ({((current_timestamp - season_start_timestamp)/season_duration)*100:.0f} %)"

    if season == current_season(time.time()):
        season_difference = (
            current_timestamp - season_start_timestamp
        ) / season_duration
        season_seconds_remaining = (
            ceil(season_difference) - season_difference
        ) * season_duration
        day = season_seconds_remaining // (24 * 3600)
        hour = season_seconds_remaining % (24 * 3600) // 3600
        minute = season_seconds_remaining % (24 * 3600) % 3600 // 60
        second = season_seconds_remaining % (24 * 3600) % 3600 % 60
        time_remaining = f"{int(day)}d {int(hour)}h {int(minute)}m {int(second)}s"
    else:
        time_remaining = ""

    goober_dash_all_season_info = [
        season_start,
        season_end,
        season_days,
        status,
        time_remaining,
    ]
    return goober_dash_all_season_info


def season_leaderboard(
    season: int,
    leaderboard_id: str,
    limit: int = 100,
    cursor: str = "",
    owner_ids: str = "",
):
    with open("../storage/goober_dash_token.txt", "r") as f:
        token = f.readline()  # goober_dash_token

    headers = {"authorization": f"Bearer {token}"}

    url = "https://gooberdash-api.winterpixel.io/v2/leaderboard/"
    url += f"{leaderboard_id}.{season}"
    url += f"?limit={limit}"
    url += f"&cursor={cursor}" if cursor != "" else ""
    url += f"&owner_ids={owner_ids}" if owner_ids != "" else ""

    response = requests.get(
        url,
        headers=headers,
    )
    return json.loads(response.content)
