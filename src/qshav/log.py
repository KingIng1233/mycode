import json

def append_record(record: dict, path="data/audit.log.jsonl"):
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")

def read_records(path="data/audit.log.jsonl") -> list[dict]:
    records = []
    with open(path, "r") as f:
        for line in f:
            records.append(json.loads(line))
    return records

def tamper_check(path="data/audit.log.jsonl") -> bool:
    try:
        _ = read_records(path)
        return True
    except Exception:
        return False
