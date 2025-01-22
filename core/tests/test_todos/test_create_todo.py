from datetime import datetime, timedelta

from unittest.mock import patch
import uuid

import pytest
from freezegun import freeze_time

from core.todos.create_todo import init_todo


def test_create_basic_valid_todo() -> None:
    mock_uuid4 = uuid.UUID('4b235a2c-e7d7-465f-88b1-173d9e2d6178')

    with freeze_time("2025-12-12"), patch("uuid.uuid4", return_value=mock_uuid4):
        todo: dict[str, str] = init_todo(
            name="Learn Flask"
        )

        assert todo == {
            "name": "Learn Flask",
            "status": "pending",
            "id": mock_uuid4,
            "created_at": datetime(2025, 12, 12),
        }


def test_create_todo_with_empty_name():
    with pytest.raises(ValueError, match='Task name is required.'):
        init_todo(name="")


def test_create_todo_invalid_name():
    with pytest.raises(ValueError, match='Task name is required.'):
        init_todo(name="  ")


@pytest.mark.skip(reason="Not implemented yet.")
def test_create_todo_with_all_options():
    with freeze_time("2025-12-12"):
        start_datetime = datetime.now() + timedelta(days=1)
        data = {
            "name": "Learn Flask",
            "description": "Learn Flask",
            "start_dt": start_datetime,
            "duration": timedelta(minutes=10),
            "estimated_duration": timedelta(minutes=10),
            "type": "workshop",
            "priority": "critical"
        }

        todo = create_todo(**data)

        assert todo == {
            **data,
            'id': 1,
            'status': 'pending',
            'created_at': datetime(2025, 12, 12),
        }


def test_create_todo_with_past_stat_date():
    pass


def test_create_todo_with_non_positive_duration():
    pass


def test_create_todo_with_non_positive_estimated_duration():
    pass
