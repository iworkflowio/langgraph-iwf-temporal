from abc import ABC

from sdks.python.src.saf.bg_step_def import StepDef


class AgentDef(ABC):
    """AgentDef is the interface to define an agent.
    """

    def get_bg_steps(self) -> list[StepDef]:
        pass