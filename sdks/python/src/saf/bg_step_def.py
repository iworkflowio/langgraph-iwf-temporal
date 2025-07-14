from abc import ABC
from typing import Generic, TypeVar, get_args
from sdks.python.src.saf.execution_context import ExecutionContext
from sdks.python.src.saf.step_decision import StepDecision
from sdks.python.src.saf.step_options import StepOptions
from sdks.python.src.saf.wait_for_condition import WaitForCondition

T = TypeVar("T")

class StepDef(ABC):
    """StepDef is the interface to define a background step.
       A background step is executed in the background, with distributed backoff retry(default to infinite)
       to recover from any instance failures.
    """

not_implemented_error_msg = "This implementation shouldn't be invoked. It has to be implemented by application."

class BgStep(ABC, Generic[T]):
    """BgStep is the interface to define a background step.
       Args:
            T: The input type of the background step.
    """

    def wait_until(
        self,
        ctx: ExecutionContext,
        input: T,
    ) -> WaitForCondition:
        """
        WaitUntil is optional method to set up condition to wait for, before below `action` method is invoked.
        Again, it's optional -- the `action` will be invoked instead if this is not implemented.

        Args:
            ctx: the context info of this method execution, include agent run start time, agent, etc.
                 It also holds the necessary data for invoking APIs for memory, queue etc.
            input: input: the step input
        Returns: the request to wait for
        """
        raise NotImplementedError(not_implemented_error_msg)

    def action(
        self,
        ctx: ExecutionContext,
        input: T,
    ) -> StepDecision:
        """
        Execute is the method to execute and decide what to do next. Invoke after commands from WaitUntil are completed,
        or there is WaitUntil is not implemented for the state.

        Args:
          ctx: the context info of this API invocation, like workflow start time, workflowId, etc
          input:  the step input

        Returns: the decision of what to do next(e.g. transition to next steps or closing workflow)
        """
        raise NotImplementedError(not_implemented_error_msg)

    def get_step_options(self) -> StepOptions:
        """GetStateOptions can just return nil to use the default Options
        StateOptions is optional configuration to adjust the step behaviors. Default values:
             StateId:  name of the implementation class
             waitUntilApiFailurePolicy: FAIL_WORKFLOW_ON_FAILURE
             PersistenceLoadingPolicy for dataAttributes/searchAttributes: LOAD_ALL_WITHOUT_LOCKING
             waitUntil/execute API:
                timeout: 30s
                retryPolicy:
                    InitialIntervalSeconds: 1
                    MaxInternalSeconds:100
                    MaximumAttempts: 0
                    BackoffCoefficient: 2
        Returns: WorkflowStateOptions
        """
        return StepOptions()


def get_step_id(step: BgStep) -> str:
    return step.__class__.__name__
    # TODO: use below code to support overriding step_id
    # options = step.get_step_options()
    # if options is None or options.step_id is None:
    #     return step.__class__.__name__
    # return options.step_id


def get_step_id_by_class(step: type[BgStep]) -> str:
    return step.__name__


def should_skip_wait_until(step: BgStep) -> bool:
    func_name = step.wait_until.__name__
    parent_method = getattr(super(type(step), step), func_name)
    return parent_method == step.wait_until


def get_input_type(step):
    bases = step.__orig_bases__
    for b in bases:
        if b.__origin__ == BgStep:
            return get_args(b)[0]
    return None


def get_step_execution_id(step: type[BgStep], number: int):
    return f"{get_step_id_by_class(step)}-{number}"