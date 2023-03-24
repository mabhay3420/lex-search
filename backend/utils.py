import time
from content_loader import lex_video_info


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.2f} seconds to run.")
        return result
    return wrapper


def timestamp_to_sec(timestamp: str) -> int:
    timestamp = timestamp.split(".")[0]
    time_components = timestamp.split(":")
    if len(time_components) == 3:
        hours, minutes, seconds = time_components
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    elif len(time_components) == 2:
        minutes, seconds = time_components
        return int(minutes) * 60 + int(seconds)



def get_timed_link(episode_number: str, start_time: str) -> str:
    return f"{lex_video_info[episode_number]['link']}&t={timestamp_to_sec(start_time)}"

def get_title(episode_number: str) -> str:
    return lex_video_info[episode_number]["title"]

def get_video_info(episode_number: str,start:str) -> dict:
    return {
        "title": get_title(episode_number),
        "link": get_timed_link(episode_number, start),
    }