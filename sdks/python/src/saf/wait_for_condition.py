from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union


@dataclass
class TimerCondition:
    condition_id: str
    duration_seconds: int

    @classmethod
    def by_seconds(cls, duration_seconds: int, condition_id: Optional[str] = None):
        return TimerCondition(
            condition_id if condition_id is not None else "", duration_seconds
        )


@dataclass
class LocalQueueCondition:
    condition_id: str
    channel_name: str

    @classmethod
    def by_name(cls, queue_name: str, condition_id: Optional[str] = None):
        return LocalQueueCondition(
            condition_id if condition_id is not None else "", queue_name
        )


BaseWaitForCondition = Union[TimerCondition, LocalQueueCondition]

class WaitForType(Enum):
    ANY_OF = 1
    ALL_OF = 2
    ANY_COMBINATION_OF = 3

@dataclass
class WaitForCondition:
    Conditions: list[BaseWaitForCondition]
    condition_waiting_type: WaitForType
    any_combinations = list[list[str]]
