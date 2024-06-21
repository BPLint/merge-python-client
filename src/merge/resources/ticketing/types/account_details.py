# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .category_enum import CategoryEnum


class AccountDetails(pydantic_v1.BaseModel):
    id: typing.Optional[str]
    integration: typing.Optional[str]
    integration_slug: typing.Optional[str]
    category: typing.Optional[CategoryEnum]
    end_user_origin_id: typing.Optional[str]
    end_user_organization_name: typing.Optional[str]
    end_user_email_address: typing.Optional[str]
    status: typing.Optional[str]
    webhook_listener_url: typing.Optional[str]
    is_duplicate: typing.Optional[bool] = pydantic_v1.Field()
    """
    Whether a Production Linked Account's credentials match another existing Production Linked Account. This field is `null` for Test Linked Accounts, incomplete Production Linked Accounts, and ignored duplicate Production Linked Account sets.
    """

    account_type: typing.Optional[str]

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
