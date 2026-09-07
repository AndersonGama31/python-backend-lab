def deduplicate_events(events: list[dict[str, object]]) -> list[dict[str, object]]:
    """Return only the latest event for each id, ordered by timestamp."""
    raise NotImplementedError
