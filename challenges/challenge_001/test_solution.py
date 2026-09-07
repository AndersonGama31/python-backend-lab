from copy import deepcopy

from challenges.challenge_001.solution import deduplicate_events


def test_empty_input() -> None:
    assert deduplicate_events([]) == []


def test_keeps_latest_event_per_id() -> None:
    events = [
        {"id": "A1", "timestamp": 10, "payload": "old"},
        {"id": "B2", "timestamp": 15, "payload": "only"},
        {"id": "A1", "timestamp": 20, "payload": "new"},
    ]

    assert deduplicate_events(events) == [
        {"id": "B2", "timestamp": 15, "payload": "only"},
        {"id": "A1", "timestamp": 20, "payload": "new"},
    ]


def test_orders_result_by_timestamp() -> None:
    events = [
        {"id": "C3", "timestamp": 30},
        {"id": "A1", "timestamp": 10},
        {"id": "B2", "timestamp": 20},
    ]

    assert deduplicate_events(events) == [
        {"id": "A1", "timestamp": 10},
        {"id": "B2", "timestamp": 20},
        {"id": "C3", "timestamp": 30},
    ]


def test_does_not_mutate_input() -> None:
    events = [
        {"id": "A1", "timestamp": 10, "payload": {"value": 1}},
        {"id": "A1", "timestamp": 20, "payload": {"value": 2}},
    ]
    original = deepcopy(events)

    deduplicate_events(events)

    assert events == original
