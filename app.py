import re

with open("lookup_table", "r") as f:
    lookup_table = [line.strip() for line in f.readlines()]
lookup_table_dct = {}
for entry in lookup_table[1:]:
    entry = entry.split(",")
    lookup_table_dct[int(entry[0])] = {entry[1]:entry[2]}


with open("logs.log", "r") as f:
    logs = [line.strip() for line in f.readlines()]


def extract_port_from_log(log: str) -> int:
    pattern = r'(?:\S+\s+){5}(\d+)'
    match = re.search(pattern, log)
    if match:
        return int(match.group(1))
    else:
        return -1


for log in logs:
    port_number = extract_port_from_log(log)
    if port_number in lookup_table_dct:
        metadata = lookup_table_dct[port_number]
        protocol = list(metadata)[0]
        tag = lookup_table_dct[port_number][protocol]
    else:
        protocol, tag = "Unknown", "Untagged"
