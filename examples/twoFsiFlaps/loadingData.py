import numpy as np

def bringLoadDispData(cutoff, end_incr, include_subiters=True, acceleratedData = True):

    if acceleratedData:
        loadFileName = "load_data"
    else:
        loadFileName = "outfluid_load_data"

    tr_disp_data = []
    tr_load_data = []
    test_disp_data = []
    test_load_data = []
    
    cutoff = cutoff
    end_incr = end_incr
    include_subiters = True
    
    tr_first_iters = []
    tr_converged_iters = [] 
    flat_tr_converged_iters = [] 
    flat_tr_first_iters = [] 
    
    tst_first_iters = []
    tst_converged_iters = []
    flat_tst_converged_iters = [] 
    flat_tst_first_iters = [] 
    
    param_map = []
    tst_param_map = []
    
    folder_names = ["./trainingData/10/", "./trainingData/12/",
                    "./trainingData/14/"]
    
    num_of_params = len(folder_names)
    
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    
    for i in range(num_of_params):
        iters = np.load(folder_names[i]+"/./iters.npy")[:cutoff]
        iters[0] -= 1
        param_map.append(np.arange(0, iters.sum())+j)
        
        iters_tst = np.load(folder_names[i]+"/./iters.npy")[cutoff:end_incr]
        tst_param_map.append(np.arange(0, iters_tst.sum())+o)
    
        tr_first_iters.append(np.append(0, iters[:-1].cumsum().astype(int)))
        tr_converged_iters.append((iters.cumsum()-1).astype(int))
        flat_tr_converged_iters.append(tr_converged_iters[-1]+ k)
        flat_tr_first_iters.append(tr_first_iters[-1]+ l)
    
        tst_first_iters.append(np.append(0, iters_tst[:-1].cumsum().astype(int)))
        tst_converged_iters.append((iters_tst.cumsum()-1).astype(int))
        flat_tst_converged_iters.append(tst_converged_iters[-1]+ m)
        flat_tst_first_iters.append(tst_first_iters[-1]+ n)
        
        if include_subiters:
            tr_disp_data.append(np.load(folder_names[i]+"/./disp_data.npy")[:, :tr_converged_iters[-1][-1]+1])
            tr_load_data.append(np.load(folder_names[i]+"/./"+loadFileName+".npy")[:, :tr_converged_iters[-1][-1]+1])
    
            test_disp_data.append(np.load(folder_names[i]+"/./disp_data.npy")[:, tr_converged_iters[-1][-1]+1:
                                                                                      tst_converged_iters[-1][-1]+1+tr_converged_iters[-1][-1]+1])
            test_load_data.append(np.load(folder_names[i]+"/./"+loadFileName+".npy")[:, tr_converged_iters[-1][-1]+1:
                                                                                      tst_converged_iters[-1][-1]+1+tr_converged_iters[-1][-1]+1])
    
        else:            
            tr_disp_data.append(np.load(folder_names[i]+"/./disp_data.npy")[:, tr_converged_iters[-1]])
            tr_load_data.append(np.load(folder_names[i]+"/./"+loadFileName+".npy")[:, tr_converged_iters[-1]])
            
            test_disp_data.append(np.load(folder_names[i]+"/./disp_data.npy")[:, tst_converged_iters[-1]])
            test_load_data.append(np.load(folder_names[i]+"/./"+loadFileName+".npy")[:, tst_converged_iters[-1]])
            
        j += iters.sum()
        o += iters_tst.sum()
        k += tr_converged_iters[-1][-1]
        l += tr_first_iters[-1][-1]
        m += tst_converged_iters[-1][-1]
        n += tst_first_iters[-1][-1]
    
    tr_disp_data = np.concatenate(tr_disp_data, axis=1)
    tr_load_data = np.concatenate(tr_load_data, axis = 1)
    test_disp_data = np.concatenate(test_disp_data, axis=1)
    test_load_data = np.concatenate(test_load_data, axis = 1)
    flat_tr_converged_iters = np.concatenate((flat_tr_converged_iters))

    return tr_disp_data, tr_load_data, test_disp_data, test_disp_data, test_load_data, flat_tr_converged_iters