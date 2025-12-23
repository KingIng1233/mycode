import typer
import uuid
import datetime
import hashlib

from qshav.log import append_record, read_records
from qshav.crypto_dummy import hash_payload, sign, verify

app = typer.Typer()


@app.command()
def init_log():
    open("data/audit.log.jsonl", "a").close()
    typer.echo("Log initialized")


@app.command()
def lock_strategy(file: str, name: str):
    with open(file, "rb") as f:
        file_bytes = f.read()

    strategy_bytes_sha256 = hashlib.sha256(file_bytes).hexdigest()

    payload = {
        "strategy_name": name,
        "strategy_file": file,
        "strategy_bytes_sha256": strategy_bytes_sha256,
    }

    payload_hash = hash_payload(payload)

    record = {
        "record_type": "strategy",
        "id": str(uuid.uuid4()),
        "ts": datetime.datetime.utcnow().isoformat(),
        "payload": payload,
        "payload_hash": payload_hash,
        "sig_alg": "DUMMY",
        "signature": sign(payload_hash),
    }

    append_record(record)
    typer.echo(record["id"])


@app.command()
def log_trade(
    strategy_id: str,
    symbol: str,
    side: str,
    qty: int,
    price: float,
):
    payload = {
        "strategy_id": strategy_id,
        "trade_id": str(uuid.uuid4()),
        "symbol": symbol,
        "side": side,
        "qty": qty,
        "price": price,
    }

    payload_hash = hash_payload(payload)

    record = {
        "record_type": "trade",
        "id": str(uuid.uuid4()),
        "ts": datetime.datetime.utcnow().isoformat(),
        "payload": payload,
        "payload_hash": payload_hash,
        "sig_alg": "DUMMY",
        "signature": sign(payload_hash),
    }

    append_record(record)
    typer.echo("Trade logged")


@app.command()
def verify_log():
    records = read_records()
    ok = True

    for r in records:
        h = hash_payload(r["payload"])
        if h != r["payload_hash"]:
            ok = False
        if not verify(h, r["signature"]):
            ok = False

    if ok:
        typer.echo(f"PASS ({len(records)} records)")
    else:
        typer.echo("FAIL")
