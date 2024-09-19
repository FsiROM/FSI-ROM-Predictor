import numpy as np

def bringDynamicalLoadDispData(cutoff_names = ["18"], cutoff_incr = [800], trainingData=False):

    assert len(cutoff_names) == len(cutoff_incr)

    RepflLoadDataConv = []
    iterLoadData = []
    iterDispData = []
    
    trainRepflLoadDataConv = []
    trainiterLoadData = []
    trainiterDispData = []
    
    testRepflLoadDataConv = []
    testiterLoadData = []
    testiterDispData = []
    inVeloc = []
    traininVeloc = []
    testinVeloc = []
    
    cutoffs = {}
    for i in range(len(cutoff_names)):
        cutoffs[cutoff_names[i]] =  cutoff_incr[i]
    
    map = np.load("./meshData/map_used.npy")
    
    
    for i in cutoff_names:
        if trainingData:
            iters = np.load("./trainingData/"+i+"/iters.npy")#[:449]
            flLoadData = np.load("./trainingData/"+i+"/outfluid_load_data.npy")#[:, :iters[:449].sum()]
            dispData = np.load("./trainingData/"+i+"/disp_data.npy")#[:, :iters[:449].sum()]
        else:
            iters = np.load("./results/FOM-FOM/"+i+"/QuadraticExtrapolation/coSimData/iters.npy")
            flLoadData = np.load("./results/FOM-FOM/"+i+"/QuadraticExtrapolation/coSimData/outfluid_load_data.npy")
            dispData = np.load("./results/FOM-FOM/"+i+"/QuadraticExtrapolation/coSimData/disp_data.npy")
        dispInterf = dispData[map, :]
        dispData = dispInterf.copy()
        lastIters = iters.cumsum()-1
    
        trainLastId = lastIters[cutoffs[i]]
    
        flLoadDataConv = flLoadData[:, lastIters][:, :-1]
        flLoadDataConv_rep = np.repeat(flLoadDataConv, iters[1:], axis = 1)
        iterLoadData_ = flLoadData[:, iters[0]:]
        iterDispData_ = dispData[:, iters[0]:]
        RepflLoadDataConv.append(flLoadDataConv_rep.copy())
        iterLoadData.append(iterLoadData_.copy())
        iterDispData.append(iterDispData_.copy())
    
    
        trainflLoadDataConv_rep = flLoadDataConv_rep[:, :trainLastId]
        trainiterLoadData_ = iterLoadData_[:, :trainLastId]
        trainiterDispData_ = iterDispData_[:, :trainLastId]
        trainRepflLoadDataConv.append(trainflLoadDataConv_rep.copy())
        trainiterLoadData.append(trainiterLoadData_.copy())
        trainiterDispData.append(trainiterDispData_.copy())
    
        testflLoadDataConv_rep = flLoadDataConv_rep[:, trainLastId:]
        testiterLoadData_ = iterLoadData_[:, trainLastId:]
        testiterDispData_ = iterDispData_[:, trainLastId:]
        testRepflLoadDataConv.append(testflLoadDataConv_rep.copy())
        testiterLoadData.append(testiterLoadData_.copy())
        testiterDispData.append(testiterDispData_.copy())
    
    RepflLoadDataConv = np.hstack((RepflLoadDataConv))
    iterLoadData = np.hstack((iterLoadData))
    iterDispData = np.hstack((iterDispData))
    
    trainRepflLoadDataConv = np.hstack((trainRepflLoadDataConv))
    trainiterLoadData = np.hstack((trainiterLoadData))
    trainiterDispData = np.hstack((trainiterDispData))
    
    testRepflLoadDataConv = np.hstack((testRepflLoadDataConv))
    testiterLoadData = np.hstack((testiterLoadData))
    testiterDispData = np.hstack((testiterDispData))

    return iterLoadData, iterDispData, RepflLoadDataConv, trainiterLoadData, trainiterDispData, trainRepflLoadDataConv, testiterLoadData, testiterDispData, testRepflLoadDataConv
