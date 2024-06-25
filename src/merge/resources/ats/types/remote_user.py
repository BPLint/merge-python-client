# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .remote_data import RemoteData
from .remote_user_access_role import RemoteUserAccessRole


class RemoteUser(pydantic_v1.BaseModel):
    """
    # The RemoteUser Object

    ### Description

    The `RemoteUser` object is used to represent a user with a login to the ATS system.

    ### Usage Example

    Fetch from the `LIST RemoteUsers` endpoint to show all users for a third party.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic_v1.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was modified by Merge.
    """

    first_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The user's first name.
    """

    last_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The user's last name.
    """

    email: typing.Optional[str] = pydantic_v1.Field()
    """
    The user's email.
    """

    disabled: typing.Optional[bool] = pydantic_v1.Field()
    """
    Whether the user's account had been disabled.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the third party's user was created.
    """

    access_role: typing.Optional[RemoteUserAccessRole] = pydantic_v1.Field()
    """
    The user's role.
    
    - `SUPER_ADMIN` - SUPER_ADMIN
    - `ADMIN` - ADMIN
    - `TEAM_MEMBER` - TEAM_MEMBER
    - `LIMITED_TEAM_MEMBER` - LIMITED_TEAM_MEMBER
    - `INTERVIEWER` - INTERVIEWER
    """

    remote_was_deleted: typing.Optional[bool] = pydantic_v1.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
