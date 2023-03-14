import pytest
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import MagicMock
from .mock_news import mock_news


def test_reading_plan_group_news():
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_news)

    with pytest.raises(ValueError, match="maior que zero"):
        ReadingPlanService.group_news_for_available_time(-10)

    plan = ReadingPlanService.group_news_for_available_time(12)

    assert len(plan["readable"]) == 2
    assert len(plan["unreadable"]) == 1

    print(plan["readable"])

    assert plan["readable"][0]["unfilled_time"] == 2
    assert plan["readable"][1]["unfilled_time"] == 1
