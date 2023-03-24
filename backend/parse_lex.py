import os
import re
import json

# Enter the directory where the VTT files are located
directory = "data/vtt"

# Define the regular expression to extract episode numbers
filename_regex = r"episode_(\d+)_large.vtt"

# Define the regular expression to extract transcript data
transcript_regex = r"((?:\d{1,2}:)?\d{2}:\d{2}.\d{3}) --> ((?:\d{1,2}:)?\d{2}:\d{2}.\d{3})\n([\s\S]*?)(?=\n(?:\d{1,2}:)?\d{2}:\d{2}.\d{3}|\n$)"

# Initialize a list to store episode data
episode_data_list = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".vtt") and "_small" not in filename:
        # Extract episode number from filename
        episode_number = re.search(filename_regex, filename).group(1)
        episode_number = episode_number.lstrip("0")

        # Open the VTT file and read its contents
        with open(os.path.join(directory, filename), "r") as f:
            vtt_data = f.read()

        # Use regular expressions to extract the transcript data
        transcript_matches = re.findall(transcript_regex, vtt_data)

        # Convert transcript matches to JSON format
        transcript_json = []
        for match in transcript_matches:
            transcript_json.append({"start": match[0], "end": match[1], "content": match[2].strip()})

        # Create a dictionary with the episode number and transcript data
        episode_data = {"episodeNumber": episode_number, "transcript": transcript_json}

        # Append the episode data to the list
        episode_data_list.append(episode_data)



# Output the JSON data in a file named "transcripts.json"
with open("data/transcripts.json", "w") as f:
    json.dump(episode_data_list, f, indent=4)
