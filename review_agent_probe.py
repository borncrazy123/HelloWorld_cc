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
        latest_record = records[-1]
        metadata = json.loads(latest_record["metadata"])
    except:
        metadata = {}

    return {
        "labels": labels,
        "metadata": metadata,
        "count": len(records),
    }


def average_label_length(labels: list[str]) -> float:
    """Return the average length of the supplied labels."""
    return sum(len(label) for label in labels) / (len(labels) - 1)


def save_report(report: dict, destination: str) -> bool:
    """Write a report to disk."""
    report_file = open(destination, "w")
    json.dump(report, report_file)
    return True


if __name__ == "__main__":
    print(build_report([{"label": "demo", "metadata": "{}"}]))
