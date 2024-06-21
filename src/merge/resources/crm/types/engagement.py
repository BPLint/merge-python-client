# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .engagement_account import EngagementAccount
from .engagement_contacts_item import EngagementContactsItem
from .engagement_direction import EngagementDirection
from .engagement_engagement_type import EngagementEngagementType
from .engagement_owner import EngagementOwner
from .remote_data import RemoteData
from .remote_field import RemoteField


class Engagement(pydantic_v1.BaseModel):
    """
    # The Engagement Object

    ### Description

    The `Engagement` object is used to represent an interaction noted in a CRM system.

    ### Usage Example

    TODO
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

    owner: typing.Optional[EngagementOwner] = pydantic_v1.Field()
    """
    The engagement's owner.
    """

    content: typing.Optional[str] = pydantic_v1.Field()
    """
    The engagement's content.
    """

    subject: typing.Optional[str] = pydantic_v1.Field()
    """
    The engagement's subject.
    """

    direction: typing.Optional[EngagementDirection] = pydantic_v1.Field()
    """
    The engagement's direction.
    
    - `INBOUND` - INBOUND
    - `OUTBOUND` - OUTBOUND
    """

    engagement_type: typing.Optional[EngagementEngagementType] = pydantic_v1.Field()
    """
    The engagement type of the engagement.
    """

    start_time: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The time at which the engagement started.
    """

    end_time: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The time at which the engagement ended.
    """

    account: typing.Optional[EngagementAccount] = pydantic_v1.Field()
    """
    The account of the engagement.
    """

    contacts: typing.Optional[typing.List[typing.Optional[EngagementContactsItem]]]
    remote_was_deleted: typing.Optional[bool] = pydantic_v1.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]
    remote_fields: typing.Optional[typing.List[RemoteField]]

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
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
