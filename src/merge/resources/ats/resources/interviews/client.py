# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import typing_extensions

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ...types.interviews_list_request_expand import InterviewsListRequestExpand
from ...types.interviews_retrieve_request_expand import InterviewsRetrieveRequestExpand
from ...types.meta_response import MetaResponse
from ...types.paginated_scheduled_interview_list import PaginatedScheduledInterviewList
from ...types.scheduled_interview import ScheduledInterview
from ...types.scheduled_interview_request import ScheduledInterviewRequest
from ...types.scheduled_interview_response import ScheduledInterviewResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InterviewsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        application_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[InterviewsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        job_id: typing.Optional[str] = None,
        job_interview_stage_id: typing.Optional[str] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        organizer_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["status"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["status"]] = None,
    ) -> PaginatedScheduledInterviewList:
        """
        Returns a list of `ScheduledInterview` objects.

        Parameters:
            - application_id: typing.Optional[str]. If provided, will only return interviews for this application.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[InterviewsListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - job_id: typing.Optional[str]. If provided, wll only return interviews organized for this job.

            - job_interview_stage_id: typing.Optional[str]. If provided, will only return interviews at this stage.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - organizer_id: typing.Optional[str]. If provided, will only return interviews organized by this user.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[typing_extensions.Literal["status"]]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["status"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import Merge
        from merge.resources.ats import InterviewsListRequestExpand

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.interviews.list(
            expand=InterviewsListRequestExpand.APPLICATION,
            remote_fields="status",
            show_enum_origins="status",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/ats/v1/interviews"),
            params=remove_none_from_dict(
                {
                    "application_id": application_id,
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "job_id": job_id,
                    "job_interview_stage_id": job_interview_stage_id,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "organizer_id": organizer_id,
                    "page_size": page_size,
                    "remote_fields": remote_fields,
                    "remote_id": remote_id,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedScheduledInterviewList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: ScheduledInterviewRequest,
        remote_user_id: str,
    ) -> ScheduledInterviewResponse:
        """
        Creates a `ScheduledInterview` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: ScheduledInterviewRequest.

            - remote_user_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/ats/v1/interviews"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model, "remote_user_id": remote_user_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ScheduledInterviewResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[InterviewsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["status"]] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["status"]] = None,
    ) -> ScheduledInterview:
        """
        Returns a `ScheduledInterview` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[InterviewsRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[typing_extensions.Literal["status"]]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["status"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import Merge
        from merge.resources.ats import InterviewsRetrieveRequestExpand

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.interviews.retrieve(
            id="id",
            expand=InterviewsRetrieveRequestExpand.APPLICATION,
            remote_fields="status",
            show_enum_origins="status",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/ats/v1/interviews/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "remote_fields": remote_fields,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ScheduledInterview, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `ScheduledInterview` POSTs.

        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.interviews.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/ats/v1/interviews/meta/post"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInterviewsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        application_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[InterviewsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        job_id: typing.Optional[str] = None,
        job_interview_stage_id: typing.Optional[str] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        organizer_id: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["status"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["status"]] = None,
    ) -> PaginatedScheduledInterviewList:
        """
        Returns a list of `ScheduledInterview` objects.

        Parameters:
            - application_id: typing.Optional[str]. If provided, will only return interviews for this application.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[InterviewsListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - job_id: typing.Optional[str]. If provided, wll only return interviews organized for this job.

            - job_interview_stage_id: typing.Optional[str]. If provided, will only return interviews at this stage.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - organizer_id: typing.Optional[str]. If provided, will only return interviews organized by this user.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[typing_extensions.Literal["status"]]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["status"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import AsyncMerge
        from merge.resources.ats import InterviewsListRequestExpand

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.ats.interviews.list(
            expand=InterviewsListRequestExpand.APPLICATION,
            remote_fields="status",
            show_enum_origins="status",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/ats/v1/interviews"),
            params=remove_none_from_dict(
                {
                    "application_id": application_id,
                    "created_after": serialize_datetime(created_after) if created_after is not None else None,
                    "created_before": serialize_datetime(created_before) if created_before is not None else None,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "job_id": job_id,
                    "job_interview_stage_id": job_interview_stage_id,
                    "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                    "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                    "organizer_id": organizer_id,
                    "page_size": page_size,
                    "remote_fields": remote_fields,
                    "remote_id": remote_id,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedScheduledInterviewList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: ScheduledInterviewRequest,
        remote_user_id: str,
    ) -> ScheduledInterviewResponse:
        """
        Creates a `ScheduledInterview` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: ScheduledInterviewRequest.

            - remote_user_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/ats/v1/interviews"),
            params=remove_none_from_dict({"is_debug_mode": is_debug_mode, "run_async": run_async}),
            json=jsonable_encoder({"model": model, "remote_user_id": remote_user_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ScheduledInterviewResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[InterviewsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing_extensions.Literal["status"]] = None,
        show_enum_origins: typing.Optional[typing_extensions.Literal["status"]] = None,
    ) -> ScheduledInterview:
        """
        Returns a `ScheduledInterview` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[InterviewsRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[typing_extensions.Literal["status"]]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[typing_extensions.Literal["status"]]. Which fields should be returned in non-normalized form.
        ---
        from merge.client import AsyncMerge
        from merge.resources.ats import InterviewsRetrieveRequestExpand

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.ats.interviews.retrieve(
            id="id",
            expand=InterviewsRetrieveRequestExpand.APPLICATION,
            remote_fields="status",
            show_enum_origins="status",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/ats/v1/interviews/{id}"),
            params=remove_none_from_dict(
                {
                    "expand": expand,
                    "include_remote_data": include_remote_data,
                    "remote_fields": remote_fields,
                    "show_enum_origins": show_enum_origins,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ScheduledInterview, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self) -> MetaResponse:
        """
        Returns metadata for `ScheduledInterview` POSTs.

        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.ats.interviews.meta_post_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/ats/v1/interviews/meta/post"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
