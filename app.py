with open("lookup_table", "r") as f:
    lookup_table = [line.strip() for line in f.readlines()]

with open("logs.log", "r") as f:
    logs = [line.strip() for line in f.readlines()]


