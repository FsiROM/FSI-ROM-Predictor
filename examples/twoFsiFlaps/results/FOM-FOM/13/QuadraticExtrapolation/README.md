# To replicate

In : [`../../../../fsi_ROM_parameters.json`](../../../../fsi_ROM_parameters.json):
```
"predictors" : [
            {
                "type"      : "quadratic",
                "solver"    : "fluid",
                "data_name" : "load",
                "prediction_launch_time" : 0.8
            }
],
```

In [`../../../../FluidMaterials.json`](../../../../FluidMaterials.json):
```
"DYNAMIC_VISCOSITY" : 1.3
```
