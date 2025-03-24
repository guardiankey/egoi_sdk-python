# egoi_api.model.push_stats.PushStats

Push report stats schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Push report stats schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sends** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of sent messages | [optional] 
**opens** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of opened messages | [optional] 
**delivered** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of delivered messages | [optional] 
**received** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of received messages | [optional] 
**bounces** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of bounces | [optional] 
**error** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of error messages | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

