# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .remote_field_request import RemoteFieldRequest


class AccountRequest(pydantic.BaseModel):
    """
    # The Account Object
    ### Description
    The `Account` object is used to represent a company in a CRM system.
    ### Usage Example
    TODO
    """

    owner: typing.Optional[str] = pydantic.Field(description="The account's owner.")
    name: typing.Optional[str] = pydantic.Field(description="The account's name.")
    description: typing.Optional[str] = pydantic.Field(description="The account's description.")
    industry: typing.Optional[str] = pydantic.Field(description="The account's industry.")
    website: typing.Optional[str] = pydantic.Field(description="The account's website.")
    number_of_employees: typing.Optional[int] = pydantic.Field(description="The account's number of employees.")
    last_activity_at: typing.Optional[str] = pydantic.Field(
        description="The last date (either most recent or furthest in the future) of when an activity occurs in an account."
    )
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}