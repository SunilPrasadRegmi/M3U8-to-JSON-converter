import re
import json

with open('playlist.m3u8', 'r', encoding='utf-8') as f:
    content = f.readlines()

channels = []

for line in content:
    if '#EXTINF' in line:
        tvg_id_match = re.search('tvg-id="(.*?)"', line)
        tvg_chno_match = re.search('tvg-chno="(.*?)"', line)
        tvg_logo_match = re.search('tvg-logo="(.*?)"', line)
        group_title_match = re.search('group-title="(.*?)"', line)
        
        tvg_id = tvg_id_match.group(1) if tvg_id_match else None
        tvg_chno = tvg_chno_match.group(1) if tvg_chno_match else None
        tvg_logo = tvg_logo_match.group(1) if tvg_logo_match else None
        group_title = group_title_match.group(1) if group_title_match else None
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
