import json

FILE_NAME = 'cenzure'

with open(f'{FILE_NAME}.txt', encoding='utf-8') as r:
    lines = [line.strip() for line in r.readlines()]

with open(f'{FILE_NAME}.json', 'w', encoding='utf-8') as w:
    json.dump(lines, w)