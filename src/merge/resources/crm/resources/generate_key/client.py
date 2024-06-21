# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ...types.remote_key import RemoteKey

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GenerateKeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> RemoteKey:
        """
        Create a remote key.

        Parameters
        ----------
        name : str
            The name of the remote key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteKey


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.generate_key.create(
            name="Remote Deployment Key 1",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/v1/generate-key", method="POST", json={"name": name}, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RemoteKey, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncGenerateKeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> RemoteKey:
        """
        Create a remote key.

        Parameters
        ----------
        name : str
            The name of the remote key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteKey


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.generate_key.create(
            name="Remote Deployment Key 1",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/v1/generate-key", method="POST", json={"name": name}, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RemoteKey, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
