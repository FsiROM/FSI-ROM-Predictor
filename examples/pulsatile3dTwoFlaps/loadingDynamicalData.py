import numpy as np
import collections

def bringDynamicalLoadDispData():

    map_ = np.load("./meshData/map_used.npy")
    RepflLoadDataConv = []
    iterLoadData = []
    iterDispData = []

    trainRepflLoadDataConv = []
    trainiterLoadData = []
    trainiterDispData = []

    testRepflLoadDataConv = []
    testiterLoadData = []
    testiterDispData = []

    cutoffs = {"4_5" : 660, "2_3" : 20}
    folders = {"4_5" : "trainingData/4_5/", "2_3" : "results/FOM-FOM/2_3/ConstantExtrapolation/coSimData/"}

    for i in ["4_5", "2_3"]:
        iters = np.load(folders[i]+"/iters.npy")
        flLoadData = np.load(folders[i]+"/outfluid_load_data.npy")
        dispData = np.load(folders[i]+"/disp_data.npy")
        dispInterf = dispData[map_, :].copy()
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

    return trainiterDispData, trainRepflLoadDataConv, trainiterLoadData
