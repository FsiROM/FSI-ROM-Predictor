# To replicate

In : [`../../../../DoubleFlap_fsi_parameters_ROM.json`](../../../../DoubleFlap_fsi_parameters_ROM.json):
```
"predictors" : [
    {
        "type"      : "linear",
        "solver"    : "fluid",
        "data_name" : "load",
        "prediction_launch_time" : 0.8
    }
],
```
and
```
"structure" :
{
    "launch_time" : 0.8,
    "start_collecting_time": 300.0,
    "stop_collecting_time": -10.0,
    "imported_model" : true,
    "save_model" : false,
    "save_training_data" : false,
...
}
```

In [`../../../../FluidMaterials.json`](../../../../FluidMaterials.json):
```
"DYNAMIC_VISCOSITY" : 0.833333333
```
