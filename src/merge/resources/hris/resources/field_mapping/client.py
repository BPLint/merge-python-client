# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ...types.external_target_field_api_response import ExternalTargetFieldApiResponse
from ...types.field_mapping_api_instance_response import FieldMappingApiInstanceResponse
from ...types.field_mapping_instance_response import FieldMappingInstanceResponse
from ...types.remote_field_api_response import RemoteFieldApiResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FieldMappingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def field_mappings_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldMappingApiInstanceResponse:
        """
        Get all Field Mappings for this Linked Account. Field Mappings are mappings between third-party Remote Fields and user defined Merge fields. [Learn more](https://docs.merge.dev/supplemental-data/field-mappings/overview/).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldMappingApiInstanceResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.field_mapping.field_mappings_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/field-mappings", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FieldMappingApiInstanceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def field_mappings_create(
        self,
        *,
        target_field_name: str,
        target_field_description: str,
        remote_field_traversal_path: typing.Sequence[typing.Any],
        remote_method: str,
        remote_url_path: str,
        common_model_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FieldMappingInstanceResponse:
        """
        Create new Field Mappings that will be available after the next scheduled sync. This will cause the next sync for this Linked Account to sync **ALL** data from start.

        Parameters
        ----------
        target_field_name : str
            The name of the target field you want this remote field to map to.

        target_field_description : str
            The description of the target field you want this remote field to map to.

        remote_field_traversal_path : typing.Sequence[typing.Any]
            The field traversal path of the remote field listed when you hit the GET /remote-fields endpoint.

        remote_method : str
            The method of the remote endpoint where the remote field is coming from.

        remote_url_path : str
            The path of the remote endpoint where the remote field is coming from.

        common_model_name : str
            The name of the Common Model that the remote field corresponds to in a given category.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldMappingInstanceResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.field_mapping.field_mappings_create(
            target_field_name="example_target_field_name",
            target_field_description="this is a example description of the target field",
            remote_field_traversal_path=["example_remote_field"],
            remote_method="GET",
            remote_url_path="/example-url-path",
            common_model_name="ExampleCommonModel",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/field-mappings",
            method="POST",
            json={
                "target_field_name": target_field_name,
                "target_field_description": target_field_description,
                "remote_field_traversal_path": remote_field_traversal_path,
                "remote_method": remote_method,
                "remote_url_path": remote_url_path,
                "common_model_name": common_model_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FieldMappingInstanceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def field_mappings_destroy(
        self, field_mapping_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldMappingInstanceResponse:
        """
        Deletes Field Mappings for a Linked Account. All data related to this Field Mapping will be deleted and these changes will be reflected after the next scheduled sync. This will cause the next sync for this Linked Account to sync **ALL** data from start.

        Parameters
        ----------
        field_mapping_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldMappingInstanceResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.field_mapping.field_mappings_destroy(
            field_mapping_id="field_mapping_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"hris/v1/field-mappings/{jsonable_encoder(field_mapping_id)}",
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FieldMappingInstanceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def field_mappings_partial_update(
        self,
        field_mapping_id: str,
        *,
        remote_field_traversal_path: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        remote_method: typing.Optional[str] = OMIT,
        remote_url_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FieldMappingInstanceResponse:
        """
        Create or update existing Field Mappings for a Linked Account. Changes will be reflected after the next scheduled sync. This will cause the next sync for this Linked Account to sync **ALL** data from start.

        Parameters
        ----------
        field_mapping_id : str

        remote_field_traversal_path : typing.Optional[typing.Sequence[typing.Any]]
            The field traversal path of the remote field listed when you hit the GET /remote-fields endpoint.

        remote_method : typing.Optional[str]
            The method of the remote endpoint where the remote field is coming from.

        remote_url_path : typing.Optional[str]
            The path of the remote endpoint where the remote field is coming from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldMappingInstanceResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.field_mapping.field_mappings_partial_update(
            field_mapping_id="field_mapping_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"hris/v1/field-mappings/{jsonable_encoder(field_mapping_id)}",
            method="PATCH",
            json={
                "remote_field_traversal_path": remote_field_traversal_path,
                "remote_method": remote_method,
                "remote_url_path": remote_url_path,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FieldMappingInstanceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remote_fields_retrieve(
        self,
        *,
        common_models: typing.Optional[str] = None,
        include_example_values: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemoteFieldApiResponse:
        """
        Get all remote fields for a Linked Account. Remote fields are third-party fields that are accessible after initial sync if remote_data is enabled. You can use remote fields to override existing Merge fields or map a new Merge field. [Learn more](https://docs.merge.dev/supplemental-data/field-mappings/overview/).

        Parameters
        ----------
        common_models : typing.Optional[str]
            A comma seperated list of Common Model names. If included, will only return Remote Fields for those Common Models.

        include_example_values : typing.Optional[str]
            If true, will include example values, where available, for remote fields in the 3rd party platform. These examples come from active data from your customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteFieldApiResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.field_mapping.remote_fields_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/remote-fields",
            method="GET",
            params={"common_models": common_models, "include_example_values": include_example_values},
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RemoteFieldApiResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def target_fields_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExternalTargetFieldApiResponse:
        """
        Get all organization-wide Target Fields, this will not include any Linked Account specific Target Fields. Organization-wide Target Fields are additional fields appended to the Merge Common Model for all Linked Accounts in a category. [Learn more](https://docs.merge.dev/supplemental-data/field-mappings/target-fields/).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExternalTargetFieldApiResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.field_mapping.target_fields_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/target-fields", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExternalTargetFieldApiResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncFieldMappingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def field_mappings_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldMappingApiInstanceResponse:
        """
        Get all Field Mappings for this Linked Account. Field Mappings are mappings between third-party Remote Fields and user defined Merge fields. [Learn more](https://docs.merge.dev/supplemental-data/field-mappings/overview/).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldMappingApiInstanceResponse


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.field_mapping.field_mappings_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/field-mappings", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FieldMappingApiInstanceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def field_mappings_create(
        self,
        *,
        target_field_name: str,
        target_field_description: str,
        remote_field_traversal_path: typing.Sequence[typing.Any],
        remote_method: str,
        remote_url_path: str,
        common_model_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FieldMappingInstanceResponse:
        """
        Create new Field Mappings that will be available after the next scheduled sync. This will cause the next sync for this Linked Account to sync **ALL** data from start.

        Parameters
        ----------
        target_field_name : str
            The name of the target field you want this remote field to map to.

        target_field_description : str
            The description of the target field you want this remote field to map to.

        remote_field_traversal_path : typing.Sequence[typing.Any]
            The field traversal path of the remote field listed when you hit the GET /remote-fields endpoint.

        remote_method : str
            The method of the remote endpoint where the remote field is coming from.

        remote_url_path : str
            The path of the remote endpoint where the remote field is coming from.

        common_model_name : str
            The name of the Common Model that the remote field corresponds to in a given category.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldMappingInstanceResponse


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.field_mapping.field_mappings_create(
            target_field_name="example_target_field_name",
            target_field_description="this is a example description of the target field",
            remote_field_traversal_path=["example_remote_field"],
            remote_method="GET",
            remote_url_path="/example-url-path",
            common_model_name="ExampleCommonModel",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/field-mappings",
            method="POST",
            json={
                "target_field_name": target_field_name,
                "target_field_description": target_field_description,
                "remote_field_traversal_path": remote_field_traversal_path,
                "remote_method": remote_method,
                "remote_url_path": remote_url_path,
                "common_model_name": common_model_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FieldMappingInstanceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def field_mappings_destroy(
        self, field_mapping_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldMappingInstanceResponse:
        """
        Deletes Field Mappings for a Linked Account. All data related to this Field Mapping will be deleted and these changes will be reflected after the next scheduled sync. This will cause the next sync for this Linked Account to sync **ALL** data from start.

        Parameters
        ----------
        field_mapping_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldMappingInstanceResponse


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.field_mapping.field_mappings_destroy(
            field_mapping_id="field_mapping_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"hris/v1/field-mappings/{jsonable_encoder(field_mapping_id)}",
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FieldMappingInstanceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def field_mappings_partial_update(
        self,
        field_mapping_id: str,
        *,
        remote_field_traversal_path: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        remote_method: typing.Optional[str] = OMIT,
        remote_url_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FieldMappingInstanceResponse:
        """
        Create or update existing Field Mappings for a Linked Account. Changes will be reflected after the next scheduled sync. This will cause the next sync for this Linked Account to sync **ALL** data from start.

        Parameters
        ----------
        field_mapping_id : str

        remote_field_traversal_path : typing.Optional[typing.Sequence[typing.Any]]
            The field traversal path of the remote field listed when you hit the GET /remote-fields endpoint.

        remote_method : typing.Optional[str]
            The method of the remote endpoint where the remote field is coming from.

        remote_url_path : typing.Optional[str]
            The path of the remote endpoint where the remote field is coming from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldMappingInstanceResponse


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.field_mapping.field_mappings_partial_update(
            field_mapping_id="field_mapping_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"hris/v1/field-mappings/{jsonable_encoder(field_mapping_id)}",
            method="PATCH",
            json={
                "remote_field_traversal_path": remote_field_traversal_path,
                "remote_method": remote_method,
                "remote_url_path": remote_url_path,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(FieldMappingInstanceResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remote_fields_retrieve(
        self,
        *,
        common_models: typing.Optional[str] = None,
        include_example_values: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RemoteFieldApiResponse:
        """
        Get all remote fields for a Linked Account. Remote fields are third-party fields that are accessible after initial sync if remote_data is enabled. You can use remote fields to override existing Merge fields or map a new Merge field. [Learn more](https://docs.merge.dev/supplemental-data/field-mappings/overview/).

        Parameters
        ----------
        common_models : typing.Optional[str]
            A comma seperated list of Common Model names. If included, will only return Remote Fields for those Common Models.

        include_example_values : typing.Optional[str]
            If true, will include example values, where available, for remote fields in the 3rd party platform. These examples come from active data from your customers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteFieldApiResponse


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.field_mapping.remote_fields_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/remote-fields",
            method="GET",
            params={"common_models": common_models, "include_example_values": include_example_values},
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RemoteFieldApiResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def target_fields_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExternalTargetFieldApiResponse:
        """
        Get all organization-wide Target Fields, this will not include any Linked Account specific Target Fields. Organization-wide Target Fields are additional fields appended to the Merge Common Model for all Linked Accounts in a category. [Learn more](https://docs.merge.dev/supplemental-data/field-mappings/target-fields/).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExternalTargetFieldApiResponse


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.field_mapping.target_fields_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/target-fields", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExternalTargetFieldApiResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
