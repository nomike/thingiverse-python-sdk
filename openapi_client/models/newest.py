# coding: utf-8

"""
    API documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.tag_schema import TagSchema
from openapi_client.models.user_summary_schema1 import UserSummarySchema1
from typing import Optional, Set
from typing_extensions import Self

class Newest(BaseModel):
    """
    Newest
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    public_url: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    thumbnail: Optional[StrictStr] = None
    preview_image: Optional[StrictStr] = None
    creator: Optional[UserSummarySchema1] = None
    is_private: Optional[Annotated[int, Field(le=1, strict=True, ge=0)]] = None
    is_purchased: Optional[Annotated[int, Field(le=1, strict=True, ge=0)]] = None
    is_published: Optional[Annotated[int, Field(le=1, strict=True, ge=0)]] = None
    like_count: Optional[StrictInt] = None
    collect_count: Optional[StrictInt] = None
    make_count: Optional[StrictInt] = None
    comment_count: Optional[StrictInt] = None
    tags: Optional[List[TagSchema]] = None
    is_nsfw: Optional[StrictBool] = None
    rank: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "name", "url", "public_url", "created_at", "thumbnail", "preview_image", "creator", "is_private", "is_purchased", "is_published", "like_count", "collect_count", "make_count", "comment_count", "tags", "is_nsfw", "rank"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Newest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # set to None if creator (nullable) is None
        # and model_fields_set contains the field
        if self.creator is None and "creator" in self.model_fields_set:
            _dict['creator'] = None

        # set to None if is_nsfw (nullable) is None
        # and model_fields_set contains the field
        if self.is_nsfw is None and "is_nsfw" in self.model_fields_set:
            _dict['is_nsfw'] = None

        # set to None if rank (nullable) is None
        # and model_fields_set contains the field
        if self.rank is None and "rank" in self.model_fields_set:
            _dict['rank'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Newest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "url": obj.get("url"),
            "public_url": obj.get("public_url"),
            "created_at": obj.get("created_at"),
            "thumbnail": obj.get("thumbnail"),
            "preview_image": obj.get("preview_image"),
            "creator": UserSummarySchema1.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "is_private": obj.get("is_private"),
            "is_purchased": obj.get("is_purchased"),
            "is_published": obj.get("is_published"),
            "like_count": obj.get("like_count"),
            "collect_count": obj.get("collect_count"),
            "make_count": obj.get("make_count"),
            "comment_count": obj.get("comment_count"),
            "tags": [TagSchema.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "is_nsfw": obj.get("is_nsfw"),
            "rank": obj.get("rank")
        })
        return _obj


