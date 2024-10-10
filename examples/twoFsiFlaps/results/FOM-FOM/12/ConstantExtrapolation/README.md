# To reproduce

In : [`../../../../fsi_ROM_parameters.json`](../../../../fsi_ROM_parameters.json):
```
"predictors" : [
],
```
and
```
"structure" :
{
    "launch_time" : 800.0,
    "start_collecting_time": 200.0,
    "stop_collecting_time": -10.0,
    "imported_model" : true,
    "save_model" : false,
    "save_training_data" : false,
...
}
```

In [`../../../../FluidMaterials.json`](../../../../FluidMaterials.json):
```
"DYNAMIC_VISCOSITY" : 1.2
```
