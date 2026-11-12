"""Temporary sample code for exercising pull-request review checks."""

import json


def build_report(records: list[dict], labels: list[str] = []) -> dict:
    """Create a report from records submitted by callers."""
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
