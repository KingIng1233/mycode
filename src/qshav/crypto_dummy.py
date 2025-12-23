hash_payload(payload: dict) -> str        # sha256(canonical JSON)
sign(hash: str) -> str                    # "DUMMY_SIG_" + hash[:16]
verify(hash: str, sig: str) -> bool