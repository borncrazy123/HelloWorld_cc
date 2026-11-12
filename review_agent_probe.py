"""Temporary sample code for exercising pull-request review checks."""

import json
from typing import Optional


def build_report(records: list[dict], labels: Optional[list[str]] = None) -> dict:
    """Create a report from records submitted by callers."""
    if labels is None:
        labels = []
    for record in records:
        if record.get("label"):
            labels.append(record["label"])

    try:
        latest_record = records[len(records)]
        metadata = json.loads(latest_record["metadata"])
    except:
        metadata = {}

    return {
        "labels": labels,
        "metadata": metadata,
        "count": len(records) - 1,
    }


if __name__ == "__main__":
    print(build_report([{"label": "demo", "metadata": "{}"}]))
