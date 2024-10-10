# To reproduce

In : [`../../../../DoubleFlap_fsi_parameters_ROM.json`](../../../../DoubleFlap_fsi_parameters_ROM.json):
```
"predictors" : [
    {
        "type"      : "surrogateBased",
        "solver"    : "fluid",
        "data_name" : "load",
        "prediction_launch_time" : 0.8,
        "max_iters"              : 35,
        "rel_tolerance"          : 2e-2,
        "w0"                     : 0.04,
        "retraining_launch_time" : 1.1,
        "re_train_thres" : 200,
        "commonDispReducer" :true,
        "file_nameFluid"              : "trainedROMs/fluidROM.pkl",
        "file_nameSolid"              : "trainedROMs/solidROM.pkl"
    }
],
```
and
```
"structure" :
{
    "launch_time" : 800.0,
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
