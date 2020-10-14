import argparse
import boto3
import json
import datetime


def send_event(event_bus, source, count, detail):
    client = boto3.client("events")
    entries = []
    for seq in range(count):
        detail["seq"] = seq
        entries.append({
            "Time": str(datetime.datetime.now()),
            "Source": source,
            "DetailType": "custom",
            "Detail": json.dumps(detail),
            "EventBusName": event_bus

        })
    print(json.dumps(entries))
    response = client.put_events(
        Entries=entries
    )
    print(json.dumps(response))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bus', required=True, help='bus name')
    ap.add_argument('--source', required=True, help='source')
    ap.add_argument('--payload', required=True, help='filename of json payload')
    ap.add_argument('--count', required=True, help='number of events to generate')
    args = ap.parse_args()

    with open(args.payload) as payload:
        detail = json.load(payload)
        detail["metered_date"] = str(datetime.datetime.now())
    send_event(args.bus, args.source, int(args.count), detail)


if __name__ == "__main__":
    main()
