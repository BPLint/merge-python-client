# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .engagement_request_account import EngagementRequestAccount
from .engagement_request_contacts_item import EngagementRequestContactsItem
from .engagement_request_direction import EngagementRequestDirection
from .engagement_request_engagement_type import EngagementRequestEngagementType
from .engagement_request_owner import EngagementRequestOwner
from .remote_field_request import RemoteFieldRequest


class EngagementRequest(pydantic_v1.BaseModel):
    """
    # The Engagement Object

    ### Description

    The `Engagement` object is used to represent an interaction noted in a CRM system.

    ### Usage Example

    TODO
    """

    owner: typing.Optional[EngagementRequestOwner] = pydantic_v1.Field()
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

    direction: typing.Optional[EngagementRequestDirection] = pydantic_v1.Field()
    """
    The engagement's direction.
    
    - `INBOUND` - INBOUND
    - `OUTBOUND` - OUTBOUND
    """

    engagement_type: typing.Optional[EngagementRequestEngagementType] = pydantic_v1.Field()
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

    account: typing.Optional[EngagementRequestAccount] = pydantic_v1.Field()
    """
    The account of the engagement.
    """

    contacts: typing.Optional[typing.List[typing.Optional[EngagementRequestContactsItem]]]
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

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
