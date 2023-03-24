import json

def get_raw_search_items(transcript_file_path, count = None):
    with open(transcript_file_path, "r") as f:
        transcripts = json.load(f)

    # print(transcript_text_list[])
    return transcripts
    count = 10000 # get the first count items
    return transcripts[0:count]

transcript_file_path = "data/merged_transcripts.json"
transcripts = get_raw_search_items(transcript_file_path)

lex_video_info_path = "data/lex_video_info.json"
lex_video_info = json.load(open(lex_video_info_path, "r"))