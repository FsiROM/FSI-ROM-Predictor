# To reproduce

In : [`../../cosim_fsi_parameters.json`](../../cosim_fsi_parameters.json):
```
"predictors" : [
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
    "launch_time" : 0.0
}
```
