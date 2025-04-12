import json

def debug_music_blocks(data):
    issues = []
    for block in data.get("blocks", []):
        block_id = block.get("id")
        if block["type"] == "repeat" and block.get("value", 1) == 0:
            issues.append(f"Issue in Block {block_id}: Warning: Infinite loop detected")
        elif block["type"] == "tempo" and block.get("value", 120) < 30:
            issues.append(f"Issue in Block {block_id}: Warning: Tempo too low, may result in inaudible playback")
        elif block["type"] == "play" and (block.get("pitch", 60) < 30 or block.get("pitch", 60) > 100):
            issues.append(f"Issue in Block {block_id}: Note outside musical range")
    return issues

if __name__ == "__main__":
    with open("block_examples/sample_block.json", "r") as f:
        data = json.load(f)
    result = debug_music_blocks(data)
    for r in result:
        print(r)