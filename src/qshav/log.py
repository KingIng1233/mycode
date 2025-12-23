append_record(record, path="data/audit.log.jsonl")
read_records(path="data/audit.log.jsonl") -> list[dict]
tamper_check(path="data/audit.log.jsonl") -> bool