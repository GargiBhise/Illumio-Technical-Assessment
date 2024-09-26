import re


with open("lookup_table", "r") as f:
    lookup_table = [line.strip() for line in f.readlines()]

with open("logs.log", "r") as f:
    logs = [line.strip() for line in f.readlines()]


def extract_port_from_log(log: str) -> int:
    pattern = r'(?:\S+\s+){5}(\d+)'
    match = re.search(pattern, log)
    if match:
        return int(match.group(1))
    else:
        return -1


