import numpy as np

def peakpickingVOP(evidence,VLROP_th):

    # To find all negative to positive zero-crossing  points

    line_th = 0
    N = 3

    gci = np.where(np.diff((evidence > 0).astype(int)) == 1)[0]
    z = np.zeros(len(evidence))
    for i in range(len(gci)):
        z[gci[i]] = 0.5

    npz_spu = z

    # To remove the spurious  negative  to positive  zero crossing

    npz_indices1 = np.nonzero(npz_spu)[0].astype(int)


    for i in range(0,len(npz_indices1)-1):
        if max(evidence[npz_indices1[i]: npz_indices1[i+1]+1]) == 0:
            npz_indices1[i] = 0

    if max(evidence[npz_indices1[-1]:]) == 0:
        npz_indices1[-1] = 0
    
    ind_npz_final = npz_indices1[npz_indices1 != 0]

    #To find peak location between two zerocrossings % % % % % % % %%

    maxvalue_indices = []
    if max(evidence[0: ind_npz_final[0]+1]) == 0:

        for j in range(0,len(ind_npz_final)-1):
            temp=evidence[ind_npz_final[j]:ind_npz_final[j+1]+1]
            ind_temp=max(np.where(temp==max(temp))[0])
            maxvalue_indices.append(ind_temp)

        temp=evidence[ind_npz_final[-1]:]
        ind_temp=max(np.where(temp==max(temp))[0])
        maxvalue_indices.append(ind_temp)
        peak_loc = ind_npz_final+maxvalue_indices

    else:

        for j in range(0, len(ind_npz_final)-1):
            temp = evidence[ind_npz_final[j]:ind_npz_final[j+1]+1]
            ind_temp = max(np.where(temp == max(temp))[0])
            maxvalue_indices.append(ind_temp)

        temp = evidence[ind_npz_final[-1]:]
        ind_temp = max(np.where(temp == max(temp))[0])
        maxvalue_indices.append(ind_temp)
        peak_loc = ind_npz_final+maxvalue_indices

        maxvalue_indices_abnormal=[]
        temp_2 = evidence[0:ind_npz_final[0]+1]
        ind_temp_2 = max(np.where(temp_2 == max(temp_2))[0])
        maxvalue_indices_abnormal.append(ind_temp_2)

        peak_loc=np.array(list(maxvalue_indices_abnormal)+list(peak_loc))

    peak_loc=peak_loc[peak_loc>160]
    peak_loc=peak_loc[peak_loc<len(evidence)]

    for i in range(len(peak_loc)):
        if evidence[peak_loc[i]]<VLROP_th:
            peak_loc[i]=0
        
    vlrop=peak_loc[peak_loc!=0]
    pp = np.zeros(len(evidence))
    pp[np.array(vlrop)] = 1

    return vlrop,pp








