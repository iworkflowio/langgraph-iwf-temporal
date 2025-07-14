
from dataclasses import dataclass
from typing import Optional


@dataclass
class ExecutionInternalLocalMemoryContext:
    pass


@dataclass
class ExecutionInternalLocalQueueContext:
    pass

@dataclass
class ExecutionInternalContext:
    local_memory: Optional[ExecutionInternalLocalMemoryContext] = None
    local_queue: Optional[ExecutionInternalLocalQueueContext] = None

@dataclass
class ExecutionContext:
    # agent_id is the given identifier of agent instance, when creating it from client
    agent_id: str
    # The same agent_id can be reused to creat new agent instance if the previous is closed.
    # agent_run_uuid is to differentiate them
    agent_run_uuid: str
    agent_run_start_timestamp_seconds: int
    step_execution_id: Optional[str] = None
    step_first_attempt_timestamp_seconds: Optional[int] = None
    num_of_attempt: Optional[int] = None
    internal_context: Optional[ExecutionInternalContext] = None