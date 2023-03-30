import re
import json

with open('playlist.m3u8', 'r', encoding='utf-8') as f:
    content = f.readlines()

channels = []

for line in content:
    if '#EXTINF' in line:
        tvg_id = re.search('tvg-id="(.*?)"', line).group(1)
        tvg_chno = re.search('tvg-chno="(.*?)"', line).group(1)
        tvg_logo = re.search('tvg-logo="(.*?)"', line).group(1)
        group_title = re.search('group-title="(.*?)"', line).group(1)
        channel_name = line.split(',')[1].strip()
        url = content[content.index(line) + 1].strip()

        channels.append({
            'id': tvg_id,
            'channel_number': tvg_chno,
            'logo': tvg_logo,
            'category': group_title,
            'channel_name': channel_name,
            'url': url
        })

with open('channels.json', 'w') as f:
    json.dump(channels, f)

print("File saved as channels.json")