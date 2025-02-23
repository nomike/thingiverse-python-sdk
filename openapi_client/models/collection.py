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
from openapi_client.models.user_summary_schema1 import UserSummarySchema1
from typing import Optional, Set
from typing_extensions import Self

class Collection(BaseModel):
    """
    Collection
    """ # noqa: E501
    id: StrictInt
    name: StrictStr
    description: StrictStr
    description_html: Optional[StrictStr] = None
    added: datetime
    modified: datetime
    creator: Optional[UserSummarySchema1]
    url: StrictStr
    count: StrictInt
    is_editable: StrictBool
    is_featured: StrictBool
    is_liked: Optional[StrictBool] = None
    is_watched: StrictBool
    featured_on: Optional[StrictStr] = Field(default=None, description="When thing was featured. Is only set when is_featured is true")
    featured_thing_id: Optional[StrictInt] = Field(description="ID of the thing that is marked by the creator as being the \"primary\" thing.")
    preview_image: StrictStr
    absolute_url: StrictStr
    thumbnail: StrictStr
    __properties: ClassVar[List[str]] = ["id", "name", "description", "description_html", "added", "modified", "creator", "url", "count", "is_editable", "is_featured", "is_liked", "is_watched", "featured_on", "featured_thing_id", "preview_image", "absolute_url", "thumbnail"]

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
        """Create an instance of Collection from a JSON string"""
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
        # set to None if creator (nullable) is None
        # and model_fields_set contains the field
        if self.creator is None and "creator" in self.model_fields_set:
            _dict['creator'] = None

        # set to None if featured_on (nullable) is None
        # and model_fields_set contains the field
        if self.featured_on is None and "featured_on" in self.model_fields_set:
            _dict['featured_on'] = None

        # set to None if featured_thing_id (nullable) is None
        # and model_fields_set contains the field
        if self.featured_thing_id is None and "featured_thing_id" in self.model_fields_set:
            _dict['featured_thing_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Collection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "description_html": obj.get("description_html"),
            "added": obj.get("added"),
            "modified": obj.get("modified"),
            "creator": UserSummarySchema1.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "url": obj.get("url"),
            "count": obj.get("count"),
            "is_editable": obj.get("is_editable"),
            "is_featured": obj.get("is_featured"),
            "is_liked": obj.get("is_liked"),
            "is_watched": obj.get("is_watched"),
            "featured_on": obj.get("featured_on"),
            "featured_thing_id": obj.get("featured_thing_id"),
            "preview_image": obj.get("preview_image"),
            "absolute_url": obj.get("absolute_url"),
            "thumbnail": obj.get("thumbnail")
        })
        return _obj


