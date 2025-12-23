import json
import hashlib


def hash_payload(payload: dict) -> str:
    # sha256(canonical JSON)
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()


def sign(hash: str) -> str:
    return "DUMMY_SIG_" + hash[:16]


def verify(hash: str, sig: str) -> bool:
    return sig == sign(hash)
