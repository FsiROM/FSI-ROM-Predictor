# To replicate

In : [`../../../../settingsDoubleFlap3D.json`](../../../../settingsDoubleFlap3D.json):
```
"predictors" : [
    {
        "type"      : "surrogateBased",
        "solver"    : "fluid",
        "data_name" : "load",
        "prediction_launch_time" : 0.02,
        "max_iters"              : 60,
        "rel_tolerance"          : 1e-4,
        "w0"                     : 0.04,
        "retraining_launch_time" : 0.1,
        "commonDispReducer"		: true,
        "file_nameFluid"              : "./trainedROMs/fluidROM.pkl",
        "file_nameSolid"              : "trainedROMs/solidROM.pkl",
        "re_train_thres" : 240
    }
],
```
and
```
"structure" :
{
    "launch_time" : 0.02,
    "start_collecting_time": 200.0,
    "stop_collecting_time": -10.0,
    "imported_model" : false,
    "save_model" : false,
    "save_training_data" : false,
...
}
```

In [`../../../../ProjectParametersCFD.json`](../../../../ProjectParametersCFD.json):
```
"boundary_conditions_process_list" : [
...
            {
                "python_module" : "apply_inlet_process",
                "kratos_module" : "KratosMultiphysics.FluidDynamicsApplication",
                "process_name"  : "ApplyInletProcess",
                "Parameters"    : {
                    "model_part_name"    : "FluidModelPart.inlet",
                    "variable_name"      : "VELOCITY",
                    "interval"        : [1.5, "End"],
                    "modulus"         : "(1+(1/16)*(cos(2*pi*(t-1.5)))+(1/16)*(cos(3*pi*(t-1.5))))*y*(0.492-y)*11.8032539",
                "direction"       : "automatic_inwards_normal"
                }
            },
...
]
```