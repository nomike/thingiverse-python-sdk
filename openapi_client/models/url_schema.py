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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.url_schema_port import UrlSchemaPort
from openapi_client.models.url_schema_query import UrlSchemaQuery
from typing import Optional, Set
from typing_extensions import Self

class UrlSchema(BaseModel):
    """
    UrlSchema
    """ # noqa: E501
    auth: Optional[StrictStr] = None
    hash: Optional[StrictStr] = None
    host: Optional[StrictStr] = None
    hostname: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    pathname: Optional[StrictStr] = None
    protocol: Optional[StrictStr] = None
    search: Optional[StrictStr] = None
    slashes: Optional[StrictBool] = None
    port: Optional[UrlSchemaPort] = None
    query: Optional[UrlSchemaQuery] = None
    __properties: ClassVar[List[str]] = ["auth", "hash", "host", "hostname", "href", "path", "pathname", "protocol", "search", "slashes", "port", "query"]

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
        """Create an instance of UrlSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of port
        if self.port:
            _dict['port'] = self.port.to_dict()
        # override the default output from pydantic by calling `to_dict()` of query
        if self.query:
            _dict['query'] = self.query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UrlSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auth": obj.get("auth"),
            "hash": obj.get("hash"),
            "host": obj.get("host"),
            "hostname": obj.get("hostname"),
            "href": obj.get("href"),
            "path": obj.get("path"),
            "pathname": obj.get("pathname"),
            "protocol": obj.get("protocol"),
            "search": obj.get("search"),
            "slashes": obj.get("slashes"),
            "port": UrlSchemaPort.from_dict(obj["port"]) if obj.get("port") is not None else None,
            "query": UrlSchemaQuery.from_dict(obj["query"]) if obj.get("query") is not None else None
        })
        return _obj


