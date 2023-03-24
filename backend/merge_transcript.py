import json

# Load the input JSON file
with open("data/transcripts.json", "r") as f:
    transcript_data = json.load(f)

merged_transcript = []
chunk_size = 20
# Merge the start and end time for every chunk_size blocks of transcript in each episode
for episode in transcript_data:
    episode_number = episode["episodeNumber"]
    episode_transcript = episode["transcript"]
    num_blocks = len(episode_transcript)

    for i in range(0, num_blocks, chunk_size):
        merged_content = []
        for j in range(i, min(i + chunk_size, num_blocks)):
            merged_content.append(episode_transcript[j]["content"])

        merged_block = {
            "start": episode_transcript[i]["start"],
            "end": episode_transcript[min(i + chunk_size, num_blocks - 1)]["end"],
            "content": " ".join(merged_content),
        }

        merged_transcript.append(
            {
                "episodeNumber": episode_number,
                "chunk": i // chunk_size,
                "transcript": merged_block,
            }
        )

# Save the merged transcript to a new JSON file
with open("data/merged_transcripts.json", "w") as f:
    json.dump(merged_transcript, f, indent=4)

# Print the total number of blocks in the merged transcript
num_blocks = len(merged_transcript)
print(f"Total number of blocks in merged_transcript: {num_blocks} written to {f.name}")
