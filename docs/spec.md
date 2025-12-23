# QSHAV – Simple Audit Log Spec

## Goal
Create a simple, append-only audit log for trading strategies and trades.
Each record is hashed and signed so tampering can be detected.

## Record Types
1. Strategy record
2. Trade record

## Hashing
- Payload is converted to canonical JSON
- SHA256 hash is computed

## Signing
- Dummy signing is used
- Signature format: DUMMY_SIG_<first 16 chars of hash>

## Verification
- Recompute hash from payload
- Recompute signature
- Compare with stored values
- If all records match → PASS

