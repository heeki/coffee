import argparse
import boto3
import json
import datetime


def send_event(event_bus):
    client = boto3.client("events")
    entries = []
    for seq in range(10):
        entries.append({
            "Time": datetime.datetime.now(),
            "Source": "heeki.custom",
            "DetailType": "custom",
            "Detail": json.dumps({
                "seq": seq,
                "key1": "value1",
                "key2": "value2",
                "key3": "value3"
            }),
            "EventBusName": event_bus

        })
    response = client.put_events(
        Entries=entries
    )
    print(json.dumps(response))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bus', required=True, help='EventBridge bus name')
    args = ap.parse_args()
    send_event(args.bus)


if __name__ == "__main__":
    main()
