# GroupFeaturedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**thumbnail** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**creator** | [**UserSummarySchema1**](UserSummarySchema1.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**is_published** | **int** |  | [optional] 
**is_nsfw** | **bool** |  | [optional] 
**is_purchased** | **int** |  | [optional] 
**is_private** | **int** |  | [optional] 
**collect_count** | **int** |  | [optional] 
**comment_count** | **int** |  | [optional] 
**make_count** | **int** |  | [optional] 
**like_count** | **int** |  | [optional] 
**preview_image** | **str** |  | [optional] 
**tags** | [**List[GroupFeaturedInnerTagsInner]**](GroupFeaturedInnerTagsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.group_featured_inner import GroupFeaturedInner

# TODO update the JSON string below
json = "{}"
# create an instance of GroupFeaturedInner from a JSON string
group_featured_inner_instance = GroupFeaturedInner.from_json(json)
# print the JSON string representation of the object
print(GroupFeaturedInner.to_json())

# convert the object into a dict
group_featured_inner_dict = group_featured_inner_instance.to_dict()
# create an instance of GroupFeaturedInner from a dict
group_featured_inner_from_dict = GroupFeaturedInner.from_dict(group_featured_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


