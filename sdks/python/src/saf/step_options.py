from dataclasses import dataclass
from typing import Any, Optional

from iwf.iwf_api.models import (
    PersistenceLoadingPolicy,
    RetryPolicy, WaitUntilApiFailurePolicy,
)


@dataclass
class StepOptions:
    # below are wait_until API specific options:
    wait_until_api_timeout_seconds: Optional[int] = None
    wait_until_api_retry_policy: Optional[RetryPolicy] = None
    """
       By default, agent would fail after waitUntil API retry exhausted.
       This policy to allow proceeding to the action API after waitUntil API exhausted all retries.
       This is useful for some advanced use cases like SAGA pattern.
       RetryPolicy is required to be set with maximumAttempts or maximumAttemptsDurationSeconds for waitUntil API.
       NOTE: action API will use commandResults to check whether the waitUntil has succeeded or not.
       See more in <a href="https://github.com/indeedeng/iwf/wiki/WorkflowStateOptions">wiki</a>
    """
    proceed_to_action_when_wait_until_retry_exhausted: Optional[
        WaitUntilApiFailurePolicy
    ] = None
    wait_until_api_local_kv_loading_policy: Optional[
        PersistenceLoadingPolicy
    ] = None
    wait_until_api_indexed_kv_loading_policy: Optional[
        PersistenceLoadingPolicy
    ] = None
    # below are action API specific options:
    action_api_timeout_seconds: Optional[int] = None
    action_api_retry_policy: Optional[RetryPolicy] = None
    """
        By default, agent would fail after action API retry exhausted.
        Set this to proceed to the specified step after the action API exhausted all retries
        This is useful for some advanced use cases like SAGA pattern.
        RetryPolicy is required to be set with maximumAttempts or maximumAttemptsDurationSeconds for action API.
        Note that the failure handling step will take the same input as this "failed from step".
        TODO the type should be the type is Optional[type[BgStep]] but -- there is an issue with circular import...
    """
    proceed_to_state_when_execute_retry_exhausted: Optional[type] = None
    execute_api_data_attributes_loading_policy: Optional[PersistenceLoadingPolicy] = (
        None
    )
    execute_api_search_attributes_loading_policy: Optional[PersistenceLoadingPolicy] = (
        None
    )