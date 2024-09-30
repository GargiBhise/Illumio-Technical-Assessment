import re


with open("lookup_table", "r") as f:
    lookup_table = [line.strip() for line in f.readlines()]
lookup_table_dct = {}
for entry in lookup_table[1:]:
    entry = entry.split(",")
    ''' { port: {'protocol': 'tag'}, port: {'protocol': 'tag'}, ... } '''
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


tag_counts = {}
port_protocol_counts = {}
for log in logs:
    port_number = extract_port_from_log(log)
    if port_number in lookup_table_dct:
        metadata = lookup_table_dct[port_number]
        protocol = list(metadata)[0]
        tag = lookup_table_dct[port_number][protocol]
    else:
        protocol, tag = "Unknown", "Untagged"
    ''' { 'tag': count, 'tag': count, ... } '''
    tag_counts[tag] = tag_counts.get(tag, 0) + 1
    ''' { (port,'protocol'): count, (port,'protocol'): count, ... } '''
    port_protocol_counts[(port_number, protocol)] = port_protocol_counts.get((port_number, protocol), 0) + 1



tag_output = "Tag,Count\n"
for tag, count in tag_counts.items():
    tag_output += f"{tag},{count}\n"
with open("tags_counts", "w") as f:
    f.write(tag_output)

port_output = "Port,Protocol,Count\n"
for (port, protocol), count in port_protocol_counts.items():
    port_output += f"{port},{protocol},{count}\n"
with open("port_protocol_counts", "w") as f:
    f.write(port_output)

