# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CollectionRetrieveParams"]


class CollectionRetrieveParams(TypedDict, total=False):
    expand: List[Literal["parent_collection"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal["collection_type"]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal["collection_type"]
    """Which fields should be returned in non-normalized form."""
