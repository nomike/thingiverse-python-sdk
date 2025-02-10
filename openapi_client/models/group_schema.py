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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.group_featured_images_inner import GroupFeaturedImagesInner
from openapi_client.models.group_featured_inner import GroupFeaturedInner
from openapi_client.models.group_members import GroupMembers
from typing import Optional, Set
from typing_extensions import Self

class GroupSchema(BaseModel):
    """
    GroupSchema
    """ # noqa: E501
    id: StrictInt
    name: Optional[StrictStr] = None
    slug: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    public_url: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    image: Optional[StrictStr] = None
    creator: Optional[StrictInt] = None
    is_member: Optional[StrictBool] = None
    members: Optional[GroupMembers] = None
    things: Optional[GroupMembers] = None
    group_topics: Optional[GroupMembers] = None
    featured: Optional[List[GroupFeaturedInner]] = None
    featured_images: Optional[List[GroupFeaturedImagesInner]] = None
    pinned_topics: Optional[StrictInt] = Field(default=None, alias="pinnedTopics")
    __properties: ClassVar[List[str]] = ["id", "name", "slug", "description", "public_url", "url", "image", "creator", "is_member", "members", "things", "group_topics", "featured", "featured_images", "pinnedTopics"]

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
        """Create an instance of GroupSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of members
        if self.members:
            _dict['members'] = self.members.to_dict()
        # override the default output from pydantic by calling `to_dict()` of things
        if self.things:
            _dict['things'] = self.things.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group_topics
        if self.group_topics:
            _dict['group_topics'] = self.group_topics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in featured (list)
        _items = []
        if self.featured:
            for _item_featured in self.featured:
                if _item_featured:
                    _items.append(_item_featured.to_dict())
            _dict['featured'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in featured_images (list)
        _items = []
        if self.featured_images:
            for _item_featured_images in self.featured_images:
                if _item_featured_images:
                    _items.append(_item_featured_images.to_dict())
            _dict['featured_images'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GroupSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "description": obj.get("description"),
            "public_url": obj.get("public_url"),
            "url": obj.get("url"),
            "image": obj.get("image"),
            "creator": obj.get("creator"),
            "is_member": obj.get("is_member"),
            "members": GroupMembers.from_dict(obj["members"]) if obj.get("members") is not None else None,
            "things": GroupMembers.from_dict(obj["things"]) if obj.get("things") is not None else None,
            "group_topics": GroupMembers.from_dict(obj["group_topics"]) if obj.get("group_topics") is not None else None,
            "featured": [GroupFeaturedInner.from_dict(_item) for _item in obj["featured"]] if obj.get("featured") is not None else None,
            "featured_images": [GroupFeaturedImagesInner.from_dict(_item) for _item in obj["featured_images"]] if obj.get("featured_images") is not None else None,
            "pinnedTopics": obj.get("pinnedTopics")
        })
        return _obj


