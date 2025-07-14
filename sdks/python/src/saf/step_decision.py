from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any


@dataclass
class StepTransition:
    next_step_id: str
    next_step_input: Any = None

class CloseType(Enum):
    FORCE_FAIL = 1
    FORCE_COMPLETE = 2
    GRACEFULLY_COMPLETE = 3

@dataclass
class AgentCloseDecision:
    closeType: CloseType
    closeOutput: Any = None


@dataclass
class StepDecision:
    next_steps: list[StepTransition]
    close_agent: Optional[AgentCloseDecision] = None
    deadEnd: Optional[bool] = None


