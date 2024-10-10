# To reproduce

In : [`../../fsi_ROM_parameters.json`](../../fsi_ROM_parameters.json):
```
"predictors" : [
],
```
and
```
"structure" :
{
    "launch_time" : 800.0,
    "start_collecting_time": 0.0,
    "stop_collecting_time": 10.0,
    "imported_model" : false,
    "save_model" : false,
    "save_training_data" : true,
...
}
```

In [`../../FluidMaterials.json`](../../FluidMaterials.json):
```
"DYNAMIC_VISCOSITY" : 1.4
```
