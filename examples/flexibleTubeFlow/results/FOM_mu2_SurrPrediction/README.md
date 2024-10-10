# To reproduce

In : [`../../cosim_fsi_parameters.json`](../../cosim_fsi_parameters.json):
```
"predictors" : [
            {
                "type" : "surrogateBased",
                "solver"    : "blood",
                "data_name" : "pressure",
                "prediction_launch_time" : 0.0,
                "max_iters"              : 35,
                "rel_tolerance"          : 2e-2,
                "w0"                     : 0.04,
                "retraining_launch_time" : 0,
                "commonDispReducer"      : false,
                "file_nameFluid"              : "./trainedROMs/fluidSurrog.pkl",
                "file_nameSolid"              : "./trainedROMs/solidROM.pkl"
            }
],
```

In : [`../../fsi_par/fluidParams.json.json`](../../fsi_par/fluidParams.json):
```
"mu" :
{
    "mu_0" : 0.9,
    "mu_1" : 4.0
}
```

And in : [`../../fsi_par/solidParams.json`](../../fsi_par/solidParams.json):
```
{
    "file_name" : "trainedROMs/solidROM.pkl",
    "launch_time" : 3000.0
}
```
