#!/usr/bin/env python
# -*- coding: utf-8 -*-

targetfilename='infout1f.inp'  
file=open(targetfilename,'w')

BeginEnd="#------------------------\n"

output=['coefficients',]
ifdim=[0,]
boundaryConditions=[[2],]
nplane=[0,]
ref_cen=[   [0,0,0],
            [10,1,0],
        ]
ref_inflow=[[89876.3,1.1111,11.0],
            [89876.3,2.2222,22.0],
            [89876.3,3.3333,33.0],
            [89876.3,4.4444,44.0],
            ]
ref_leng=[[10,10,10],
        ]
ref_area=[[15,15,15],
        ]
alpha=[0,5,10,15]
plane=['xy',]



total_num=(  len(output)  *len(ifdim)   *len(boundaryConditions)
            *len(nplane)  *len(ref_cen) *len(ref_inflow)
            *len(ref_leng)*len(ref_area)*len(alpha)
            *len(plane))
i=1

file.write('nentries %s\n'%total_num)
for output_item in output:
    for ifdim_item in ifdim:
        for bcs in boundaryConditions:
            for nplane_item in nplane:
                for cen in ref_cen:
                    for inflow in ref_inflow:
                        for leng in ref_leng:
                            for area in ref_area:
                                for alpha_item in alpha:
                                    for plane_item in plane:
                                        file.write(BeginEnd)
                                        file.write('entry%s begin\n'%i)
                                        file.write('output %s\n'%output_item)
                                        file.write('ifdim %s\n' %ifdim_item)
                                        file.write('nbcsel %s\n'%len(bcs))
                                        for bc in bcs:
                                            file.write('%s\n'%bc)
                                        
                                        file.write('nplane %s\n'%nplane_item)
                                        file.write('xcen %s\n'%cen[0])
                                        file.write('ycen %s\n'%cen[1])
                                        file.write('zcen %s\n'%cen[2])

                                        file.write('pref %s\n'%inflow[0])
                                        file.write('rref %s\n'%inflow[1])
                                        file.write('uref %s\n'%inflow[2])

                                        file.write('lxref %s\n'%leng[0])
                                        file.write('lyref %s\n'%leng[1])
                                        file.write('lzref %s\n'%leng[2])

                                        file.write('axref %s\n'%area[0])
                                        file.write('ayref %s\n'%area[1])
                                        file.write('azref %s\n'%area[2])

                                        file.write('alpha %s\n'%alpha_item)
                                        file.write('plane %s\n'%plane_item)

                                        file.write('entry%s end\n'%i)
                                        file.write(BeginEnd)
                                        i=i+1
