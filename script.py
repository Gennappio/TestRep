##
#for vc in range(0, VOLUME_MESH.GetNumberOfCells()):
#        ids = vtk.vtkIdList()   
#        VOLUME_MESH.GetCellPoints(vc, ids)
#        t1 = 0
#        idli = []
#        for cp in range(0, ids.GetNumberOfIds()):
##                if (ids.GetId(cp) == 220): t1 = t1+1
##                if (ids.GetId(cp) == 1): t1 = t1+1
##                if (ids.GetId(cp) == 2): t1 = t1+1
#                if (ids.GetId(cp) ==14113645): t1 = t1+1
#        if( t1 ==1 ): print 1, vc
##        if( t1 ==2 ): print 2, vc
##        if( t1 ==3 ): print 3, vc
##        if( t1 ==4 ): print 4, vc



def midpoint(npoints, points, f_mid):

    m_pp = [] 
    m_pp.append(0.0)
    m_pp.append(0.0)
    m_pp.append(0.0)
    we = []
    we.append(0.0)
    we.append(0.0)
    we.append(0.0)
    we.append(0.0)
    we_sum = 0;
    ii=0
    jj=0;
    
    for ii in range(0, npoints):
        edge_vec= [] 
        w_module = 0

        next = 0
        if (ii+1 != npoints): 
            next = ii+1
                  
    
        edge_vec.append(points[next][0]-points[ii][0])
        edge_vec.append(points[next][1]-points[ii][1])
        edge_vec.append(points[next][2]-points[ii][2])
    
        w_module = edge_vec[0]**2+edge_vec[1]**2+edge_vec[2]**2
    
        we[ii]   += w_module;
        we[next] += w_module;
        we_sum   += w_module + w_module;
        
        
    if(we_sum <= 0.0):
        we[0] = 1.0
    else:
        for ii in range(0, npoints):
            we[ii] /= we_sum
        
    
    for ii in range(0, npoints):
        for jj in range(0, 3):
            m_pp[jj] += points[ii][jj] * we[ii]
    
    
    for ii in range(0, 3):
        f_mid[ii] = m_pp[ii]



p_set = []
p_set.append([ 1873.6170654296875,	1158.7012939453125,	270.15142822265625 ])
p_set.append([ 1873.6124267578125,	1158.6461181640625,	269.786376953125 ])
p_set.append([ 1872.818603515625,	1158.6741943359375,	269.70245361328125 ])
p_set.append([ 1872.821533203125,	1158.7293701171875,	270.08416748046875 ])
p_set.append([ 1873.216796875,	1158.6873779296875,	269.935302734375 ])

f_mid = [] 
f_mid.append(0.0)
f_mid.append(0.0)
f_mid.append(0.0)
    

midpoint(4, p_set, f_mid)

print f_mid


p_set1 = []
p_set1.append([ 1873.6165771484375,	1158.7005615234375,	270.15130615234375 ])
p_set1.append([ 1872.821044921875,	1158.728515625,	270.08404541015625 ])
p_set1.append([ 1872.818115234375,	1158.6734619140625,	269.7025146484375 ])
p_set1.append([ 1873.6119384765625,	1158.6453857421875,	269.78643798828125 ])
p_set1.append([ 1873.216796875,	1158.6873779296875,	269.935302734375 ])

midpoint(4, p_set1, f_mid)

print f_mid
