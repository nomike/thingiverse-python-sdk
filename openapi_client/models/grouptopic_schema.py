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
from openapi_client.models.comment_modified import CommentModified
from openapi_client.models.comment_schema import CommentSchema
from openapi_client.models.group_topic_comments import GroupTopicComments
from openapi_client.models.group_topic_tags import GroupTopicTags
from openapi_client.models.member_schema import MemberSchema
from typing import Optional, Set
from typing_extensions import Self

class GrouptopicSchema(BaseModel):
    """
    GrouptopicSchema
    """ # noqa: E501
    id: StrictInt
    name: Optional[StrictStr] = None
    user: Optional[MemberSchema] = None
    group_url: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    public_url: Optional[StrictStr] = None
    comments: Optional[GroupTopicComments] = None
    added: Optional[datetime] = None
    modified: Optional[CommentModified] = None
    pinned: Optional[Annotated[int, Field(le=1, strict=True, ge=0)]] = None
    comment_of_topic: Optional[CommentSchema] = None
    tags: Optional[GroupTopicTags] = None
    watched: Optional[StrictBool] = None
    type_name: Optional[StrictStr] = None
    root_comment_count: Optional[StrictInt] = None
    can_comment: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "name", "user", "group_url", "url", "public_url", "comments", "added", "modified", "pinned", "comment_of_topic", "tags", "watched", "type_name", "root_comment_count", "can_comment"]

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
        """Create an instance of GrouptopicSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comments
        if self.comments:
            _dict['comments'] = self.comments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified
        if self.modified:
            _dict['modified'] = self.modified.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comment_of_topic
        if self.comment_of_topic:
            _dict['comment_of_topic'] = self.comment_of_topic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GrouptopicSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "user": MemberSchema.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "group_url": obj.get("group_url"),
            "url": obj.get("url"),
            "public_url": obj.get("public_url"),
            "comments": GroupTopicComments.from_dict(obj["comments"]) if obj.get("comments") is not None else None,
            "added": obj.get("added"),
            "modified": CommentModified.from_dict(obj["modified"]) if obj.get("modified") is not None else None,
            "pinned": obj.get("pinned"),
            "comment_of_topic": CommentSchema.from_dict(obj["comment_of_topic"]) if obj.get("comment_of_topic") is not None else None,
            "tags": GroupTopicTags.from_dict(obj["tags"]) if obj.get("tags") is not None else None,
            "watched": obj.get("watched"),
            "type_name": obj.get("type_name"),
            "root_comment_count": obj.get("root_comment_count"),
            "can_comment": obj.get("can_comment")
        })
        return _obj


