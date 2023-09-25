    for m in arange(1,(n0 - 1)).reshape(-1):
        ####################һ׶########## ##########
        for p in arange(1,(n1 - 1)).reshape(-1):
            T1_up      [2*(n1-1)* m   +p  ]=B1[2*(n1-1)*(m+1)+p+1] - B1[2*(n1-1)* m   +p  ]
            T2_up      [2*(n1-1)* m   +p  ]=B1[2*(n1-1)* m   +p+1] - B1[2*(n1-1)*(m+1)+p  ]

            N_B1       [2*(n1-1)* m   +p  ]=cross(T2_up[2*(n1-1)* m   +p  ],T1_up[2*(n1-1)* m   +p  ])
            N_B1_fanshu[2*(n1-1)* m   +p  ]=norm(N_B1[2*(n1-1)* m   +p  ])
            N_B1_danwei[2*(n1-1)* m   +p  ]=(N_B1[2*(n1-1)* m   +p  ]) / (N_B1_fanshu[2*(n1-1)* m   +p  ])


            Average_B1 [2*(n1-1)* m   +p  ]=multiply(0.25,(B1[2*(n1-1)* m   +p  ] + B1(multiply(dot(2,n1),m) + p,arange()) + B1(multiply(dot(2,n1),m) + p + 1,arange()) + B1[2*(n1-1)* m   +p+1]))
            
            #���ĸ��ǵ�ͶӰ����Ԫƽ����
            B1_tou[multiply(dot(2,n1),(m - 1)) + p,arange()]=B1[2*(n1-1)* m   +p  ] + multiply((N_B1_danwei[2*(n1-1)* m   +p  ]),(Average_B1[2*(n1-1)* m   +p  ] - B1[2*(n1-1)* m   +p  ]))
            B1_tou[multiply(dot(2,n1),m) + p,arange()]=B1(multiply(dot(2,n1),m) + p,arange()) + multiply(N_B1_danwei[2*(n1-1)* m   +p  ],(Average_B1[2*(n1-1)* m   +p  ] - B1(multiply(dot(2,n1),m) + p,arange())))
            B1_tou[multiply(dot(2,n1),m) + p + 1,arange()]=B1(multiply(dot(2,n1),m) + p + 1,arange()) + multiply(N_B1_danwei[2*(n1-1)* m   +p  ],(Average_B1[2*(n1-1)* m   +p  ] - B1(multiply(dot(2,n1),m) + p + 1,arange())))
            B1_tou[multiply(dot(2,n1),(m - 1)) + p + 1,arange()]=B1[2*(n1-1)* m   +p+1] + multiply(N_B1_danwei[2*(n1-1)* m   +p  ],(Average_B1[2*(n1-1)* m   +p  ] - B1[2*(n1-1)* m   +p+1]))

            #������Ԫ����ϵ:ԭ��λ��X_bar��Y_bar��Z_bar��x��ƽ����t1,y��ƽ����m��z��ƽ����n
            T1_up_fanshu[2*(n1-1)* m   +p  ]=norm(T1_up[2*(n1-1)* m   +p  ])
            T1_up_danwei[2*(n1-1)* m   +p  ]=T1_up[2*(n1-1)* m   +p  ] / T1_up_fanshu[2*(n1-1)* m   +p  ]
            m_danwei_up[2*(n1-1)* m   +p  ]=cross(N_B1_danwei[2*(n1-1)* m   +p  ],T1_up_danwei[2*(n1-1)* m   +p  ])

            #��ͶӰ��ӷ���������ϵת������Ԫ�����?
       #x
            B1_myx[multiply(dot(2,n1),(m - 1)) + p,1]=multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))

            B1_myx[multiply(dot(2,n1),m) + p,1]=multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),m) + p,1) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),m) + p,2) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),m) + p,3) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))

            B1_myx[multiply(dot(2,n1),m) + p + 1,1]=multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),m) + p + 1,1) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),m) + p + 1,2) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),m) + p + 1,3) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))

            B1_myx[multiply(dot(2,n1),(m - 1)) + p + 1,1]=multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,1) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,2) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,3) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            #y
            B1_myx[multiply(dot(2,n1),(m - 1)) + p,2]=multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))

            B1_myx[multiply(dot(2,n1),m) + p,2]=multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),m) + p,1) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),m) + p,2) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),m) + p,3) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))

            B1_myx[multiply(dot(2,n1),m) + p + 1,2]=multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),m) + p + 1,1) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),m) + p + 1,2) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),m) + p + 1,3) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B1_myx[multiply(dot(2,n1),(m - 1)) + p + 1,2]=multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,1) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,2) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,3) - Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            #z
            B1_myx[multiply(dot(2,n1),(m - 1)) + p,3]=0
            B1_myx[multiply(dot(2,n1),m) + p,3]=0
            B1_myx[multiply(dot(2,n1),m) + p + 1,3]=0
            B1_myx[multiply(dot(2,n1),(m - 1)) + p + 1,3]=0
            #����Ԫ�������A
            A_up[2*(n1-1)* m   +p  ]=multiply(multiply(0.5,(B1_myx(multiply(dot(2,n1),m) + p + 1,1) - B1_myx(multiply(dot(2,n1),(m - 1)) + p,1))),(B1_myx(multiply(dot(2,n1),m) + p,1) - B1_myx(multiply(dot(2,n1),(m - 1)) + p + 1,1)))
            ZhiXin_up[(p + multiply(dot(2,(m - 1)),(n1 - 1))),1]=multiply(multiply((1 / 3),(1.0 / (B1_myx(multiply(dot(2,n1),m) + p,2) - B1_myx(multiply(dot(2,n1),(m - 1)) + p + 1,2)))),(multiply(B1_myx(multiply(dot(2,n1),(m - 1)) + p + 1,1),(B1_myx(multiply(dot(2,n1),(m - 1)) + p,2) - B1_myx(multiply(dot(2,n1),m) + p,2))) + multiply(B1_myx(multiply(dot(2,n1),m) + p,1),(B1_myx(multiply(dot(2,n1),(m - 1)) + p + 1,2) - B1_myx(multiply(dot(2,n1),(m - 1)) + p,2)))))
            ZhiXin_up[(p + multiply(dot(2,(m - 1)),(n1 - 1))),2]=multiply((- 1 / 3),B1_myx(multiply(dot(2,n1),(m - 1)) + p,2))
            ZhiXin_up[(p + multiply(dot(2,(m - 1)),(n1 - 1))),3]=0
            Zhixin_up_fxqzbx[(p + multiply(dot(2,(m - 1)),(n1 - 1))),1]=Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),1) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),ZhiXin_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),ZhiXin_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            Zhixin_up_fxqzbx[(p + multiply(dot(2,(m - 1)),(n1 - 1))),2]=Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),2) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),ZhiXin_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),ZhiXin_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            Zhixin_up_fxqzbx[(p + multiply(dot(2,(m - 1)),(n1 - 1))),3]=Average_B1((p + multiply(dot(2,(m - 1)),(n1 - 1))),3) + multiply(T1_up_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),ZhiXin_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),ZhiXin_up((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            zhuangjijiao_up[2*(n1-1)* m   +p  ]=pi / 2 - acos((- (dot(N_B1_danwei[2*(n1-1)* m   +p  ],V(1,arange())))) / (norm(V(1,arange()))))
            if zhuangjijiao_up[2*(n1-1)* m   +p  ] >= 0:
                Cp_up[2*(n1-1)* m   +p  ]=Newton1(zhuangjijiao_up[2*(n1-1)* m   +p  ],V(1,1),V(1,2),V(1,3),Ma)
            if zhuangjijiao_up[2*(n1-1)* m   +p  ] < 0:
                Cp_up[2*(n1-1)* m   +p  ]=Newton1(zhuangjijiao_up[2*(n1-1)* m   +p  ],V(1,1),V(1,2),V(1,3),Ma)
            #��������
            F_up[2*(n1-1)* m   +p  ]=multiply(A_up[2*(n1-1)* m   +p  ],(multiply(multiply(multiply(Cp_up[2*(n1-1)* m   +p  ],0.5),midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)) + p_lailiu))
            CA_up[2*(n1-1)* m   +p  ]=multiply(F_up[2*(n1-1)* m   +p  ],N_B1_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            CN_up[2*(n1-1)* m   +p  ]=multiply(F_up[2*(n1-1)* m   +p  ],N_B1_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            CZ_up[2*(n1-1)* m   +p  ]=multiply(F_up[2*(n1-1)* m   +p  ],N_B1_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            Cl_up[2*(n1-1)* m   +p  ]=multiply(CN_up[2*(n1-1)* m   +p  ],cos(AttackAngle)) - multiply(CA_up[2*(n1-1)* m   +p  ],sin(AttackAngle))
            Cd_up[2*(n1-1)* m   +p  ]=multiply(CN_up[2*(n1-1)* m   +p  ],sin(AttackAngle)) + multiply(CA_up[2*(n1-1)* m   +p  ],cos(AttackAngle))
        ####################һ׶����####################
        ####################��׶####################
        for p in arange((n1 + 1),(dot(2,n1) - 1)).reshape(-1):
            T1_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=B1(multiply(dot(2,n1),m) + p + 1,arange()) - B1[2*(n1-1)* m   +p  ]
            T2_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=B1[2*(n1-1)* m   +p+1] - B1(multiply(dot(2,n1),m) + p,arange())
            N_B1[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=cross(T2_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),T1_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            N_B1_fanshu[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=norm(N_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            N_B1_danwei[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=(N_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange())) / (N_B1_fanshu((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            Average_B1[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(0.25,(B1[2*(n1-1)* m   +p  ] + B1(multiply(dot(2,n1),m) + p,arange()) + B1(multiply(dot(2,n1),m) + p + 1,arange()) + B1[2*(n1-1)* m   +p+1]))
            #���ĸ��ǵ�ͶӰ����Ԫƽ����
            B1_tou[multiply(dot(2,n1),(m - 1)) + p,arange()]=B1[2*(n1-1)* m   +p  ] + multiply(N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) - B1[2*(n1-1)* m   +p  ]))
            B1_tou[multiply(dot(2,n1),m) + p,arange()]=B1(multiply(dot(2,n1),m) + p,arange()) + multiply(N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) - B1(multiply(dot(2,n1),m) + p,arange())))
            B1_tou[multiply(dot(2,n1),m) + p + 1,arange()]=B1(multiply(dot(2,n1),m) + p + 1,arange()) + multiply(N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) - B1(multiply(dot(2,n1),m) + p + 1,arange())))
            B1_tou[multiply(dot(2,n1),(m - 1)) + p + 1,arange()]=B1[2*(n1-1)* m   +p+1] + multiply(N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) - B1[2*(n1-1)* m   +p+1]))
            #������Ԫ����ϵ:ԭ��λ��X_bar��Y_bar��Z_bar��x��ƽ����t1_up,y��ƽ����m��z��ƽ����n
            T1_up_fanshu[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=norm(T1_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            T1_up_danwei[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=T1_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) / T1_up_fanshu((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange())
            m_danwei_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=cross(N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            #��ͶӰ��ӷ���������ϵת������Ԫ�����?
       #x
            B1_myx[multiply(dot(2,n1),(m - 1)) + p,1]=multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B1_myx[multiply(dot(2,n1),m) + p,1]=multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B1_myx[multiply(dot(2,n1),m) + p + 1,1]=multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),m) + p + 1,1) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),m) + p + 1,2) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),m) + p + 1,3) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B1_myx[multiply(dot(2,n1),(m - 1)) + p + 1,1]=multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,1) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,2) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,3) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            #y
            B1_myx[multiply(dot(2,n1),(m - 1)) + p,2]=multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B1_myx[multiply(dot(2,n1),m) + p,2]=multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B1_myx[multiply(dot(2,n1),m) + p + 1,2]=multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),m) + p + 1,1) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),m) + p + 1,2) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),m) + p + 1,3) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B1_myx[multiply(dot(2,n1),(m - 1)) + p + 1,2]=multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,1) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,2) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B1_tou(multiply(dot(2,n1),(m - 1)) + p + 1,3) - Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            #z
            B1_myx[multiply(dot(2,n1),(m - 1)) + p,3]=0
            B1_myx[multiply(dot(2,n1),m) + p,3]=0
            B1_myx[multiply(dot(2,n1),m) + p + 1,3]=0
            B1_myx[multiply(dot(2,n1),(m - 1)) + p + 1,3]=0
            #����Ԫ�������A
            A_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(multiply(0.5,(B1_myx(multiply(dot(2,n1),m) + p + 1,1) - B1_myx(multiply(dot(2,n1),(m - 1)) + p,1))),(B1_myx(multiply(dot(2,n1),m) + p,1) - B1_myx(multiply(dot(2,n1),(m - 1)) + p + 1,1)))
            ZhiXin_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1]=multiply(multiply((1 / 3),(1.0 / (B1_myx(multiply(dot(2,n1),m) + p,2) - B1_myx(multiply(dot(2,n1),(m - 1)) + p + 1,2)))),(multiply(B1_myx(multiply(dot(2,n1),(m - 1)) + p + 1,1),(B1_myx(multiply(dot(2,n1),(m - 1)) + p,2) - B1_myx(multiply(dot(2,n1),m) + p,2))) + multiply(B1_myx(multiply(dot(2,n1),m) + p,1),(B1_myx(multiply(dot(2,n1),(m - 1)) + p + 1,2) - B1_myx(multiply(dot(2,n1),(m - 1)) + p,2)))))
            ZhiXin_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2]=multiply(- (1 / 3),B1_myx(multiply(dot(2,n1),(m - 1)) + p,2))
            ZhiXin_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2]=0
            Zhixin_up_fxqzbx[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1]=Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),ZhiXin_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),ZhiXin_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            Zhixin_up_fxqzbx[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2]=Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),ZhiXin_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),ZhiXin_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            Zhixin_up_fxqzbx[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3]=Average_B1((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3) + multiply(T1_up_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),ZhiXin_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),ZhiXin_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            zhuangjijiao_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=pi / 2 - acos((- (dot(N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),V(1,arange())))) / (norm(V(1,arange()))))
            if zhuangjijiao_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) >= 0:
                Cp_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=Newton1(zhuangjijiao_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),V(1,1),V(1,2),V(1,3),Ma)
            if zhuangjijiao_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) < 0:
                Cp_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=Newton1(zhuangjijiao_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),V(1,1),V(1,2),V(1,3),Ma)
            #��������
            F_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(A_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(multiply(multiply(multiply(Cp_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),0.5),midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)) + p_lailiu))
            CA_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(F_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            CN_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(F_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            CZ_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(F_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            Cl_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(CN_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),cos(AttackAngle)) - multiply(CA_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),sin(AttackAngle))
            Cd_up[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(CN_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),sin(AttackAngle)) + multiply(CA_up((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),cos(AttackAngle))
        ####################��׶����####################
    
    ###############################################################End---�ϱ���###############################################################
    
    ###############################################################�±���###############################################################
    for m in arange(1,(n0 - 1)).reshape(-1):
        ####################һ׶########## ##########
        for p in arange(1,(n1 - 1)).reshape(-1):
            T1_down[2*(n1-1)* m   +p  ]=B2(multiply(dot(2,n1),m) + p + 1,arange()) - B2[2*(n1-1)* m   +p  ]
            T2_down[2*(n1-1)* m   +p  ]=B2[2*(n1-1)* m   +p+1] - B2(multiply(dot(2,n1),m) + p,arange())
            N_B2[2*(n1-1)* m   +p  ]=cross(T2_down[2*(n1-1)* m   +p  ],T1_down[2*(n1-1)* m   +p  ])
            N_B2_fanshu[2*(n1-1)* m   +p  ]=norm(N_B2[2*(n1-1)* m   +p  ])
            N_B2_danwei[2*(n1-1)* m   +p  ]=- (N_B2[2*(n1-1)* m   +p  ]) / (N_B2_fanshu[2*(n1-1)* m   +p  ])
            Average_B2[2*(n1-1)* m   +p  ]=multiply(0.25,(B2[2*(n1-1)* m   +p  ] + B2(multiply(dot(2,n1),m) + p,arange()) + B2(multiply(dot(2,n1),m) + p + 1,arange()) + B2[2*(n1-1)* m   +p+1]))
            #���ĸ��ǵ�ͶӰ����Ԫƽ����
            B2_tou[multiply(dot(2,n1),(m - 1)) + p,arange()]=B2[2*(n1-1)* m   +p  ] + multiply((N_B2_danwei[2*(n1-1)* m   +p  ]),(Average_B2[2*(n1-1)* m   +p  ] - B2[2*(n1-1)* m   +p  ]))
            B2_tou[multiply(dot(2,n1),m) + p,arange()]=B2(multiply(dot(2,n1),m) + p,arange()) + multiply(N_B2_danwei[2*(n1-1)* m   +p  ],(Average_B2[2*(n1-1)* m   +p  ] - B2(multiply(dot(2,n1),m) + p,arange())))
            B2_tou[multiply(dot(2,n1),m) + p + 1,arange()]=B2(multiply(dot(2,n1),m) + p + 1,arange()) + multiply(N_B2_danwei[2*(n1-1)* m   +p  ],(Average_B2[2*(n1-1)* m   +p  ] - B2(multiply(dot(2,n1),m) + p + 1,arange())))
            B2_tou[multiply(dot(2,n1),(m - 1)) + p + 1,arange()]=B2[2*(n1-1)* m   +p+1] + multiply(N_B2_danwei[2*(n1-1)* m   +p  ],(Average_B2[2*(n1-1)* m   +p  ] - B2[2*(n1-1)* m   +p+1]))
            #������Ԫ����ϵ:ԭ��λ��X_bar��Y_bar��Z_bar��x��ƽ����t1,y��ƽ����m��z��ƽ����n
            T1_down_fanshu[2*(n1-1)* m   +p  ]=norm(T1_down[2*(n1-1)* m   +p  ])
            T1_down_danwei[2*(n1-1)* m   +p  ]=T1_down[2*(n1-1)* m   +p  ] / T1_down_fanshu[2*(n1-1)* m   +p  ]
            m_danwei_down[2*(n1-1)* m   +p  ]=cross(N_B2_danwei[2*(n1-1)* m   +p  ],T1_down_danwei[2*(n1-1)* m   +p  ])
            #��ͶӰ��ӷ���������ϵת������Ԫ�����?
       #x
            B2_myx[multiply(dot(2,n1),(m - 1)) + p,1]=multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),m) + p,1]=multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),m) + p,1) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),m) + p,2) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),m) + p,3) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),m) + p + 1,1]=multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),m) + p + 1,1) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),m) + p + 1,2) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),m) + p + 1,3) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),(m - 1)) + p + 1,1]=multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,1) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,2) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,3) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            #y
            B2_myx[multiply(dot(2,n1),(m - 1)) + p,2]=multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),m) + p,2]=multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),m) + p,1) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),m) + p,2) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),m) + p,3) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),m) + p + 1,2]=multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),m) + p + 1,1) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),m) + p + 1,2) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),m) + p + 1,3) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),(m - 1)) + p + 1,2]=multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,1) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,2) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,3) - Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            #z
            B2_myx[multiply(dot(2,n1),(m - 1)) + p,3]=0
            B2_myx[multiply(dot(2,n1),m) + p,3]=0
            B2_myx[multiply(dot(2,n1),m) + p + 1,3]=0
            B2_myx[multiply(dot(2,n1),(m - 1)) + p + 1,3]=0
            #����Ԫ�������A
            A_down[2*(n1-1)* m   +p  ]=multiply(multiply(0.5,(B2_myx(multiply(dot(2,n1),m) + p + 1,1) - B2_myx(multiply(dot(2,n1),(m - 1)) + p,1))),(B2_myx(multiply(dot(2,n1),m) + p,1) - B2_myx(multiply(dot(2,n1),(m - 1)) + p + 1,1)))
            ZhiXin_down[(p + multiply(dot(2,(m - 1)),(n1 - 1))),1]=multiply(multiply((1 / 3),(1.0 / (B2_myx(multiply(dot(2,n1),m) + p,2) - B2_myx(multiply(dot(2,n1),(m - 1)) + p + 1,2)))),(multiply(B2_myx(multiply(dot(2,n1),(m - 1)) + p + 1,1),(B2_myx(multiply(dot(2,n1),(m - 1)) + p,2) - B2_myx(multiply(dot(2,n1),m) + p,2))) + multiply(B2_myx(multiply(dot(2,n1),m) + p,1),(B2_myx(multiply(dot(2,n1),(m - 1)) + p + 1,2) - B2_myx(multiply(dot(2,n1),(m - 1)) + p,2)))))
            ZhiXin_down[(p + multiply(dot(2,(m - 1)),(n1 - 1))),2]=multiply((- 1 / 3),B2_myx(multiply(dot(2,n1),(m - 1)) + p,2))
            ZhiXin_down[(p + multiply(dot(2,(m - 1)),(n1 - 1))),3]=0
            Zhixin_down_fxqzbx[(p + multiply(dot(2,(m - 1)),(n1 - 1))),1]=Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),1) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),ZhiXin_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),1),ZhiXin_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            Zhixin_down_fxqzbx[(p + multiply(dot(2,(m - 1)),(n1 - 1))),2]=Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),2) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),ZhiXin_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),2),ZhiXin_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            Zhixin_down_fxqzbx[(p + multiply(dot(2,(m - 1)),(n1 - 1))),3]=Average_B2((p + multiply(dot(2,(m - 1)),(n1 - 1))),3) + multiply(T1_down_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),ZhiXin_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),3),ZhiXin_down((p + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            zhuangjijiao_down[2*(n1-1)* m   +p  ]=pi / 2 - acos((- (dot(N_B2_danwei[2*(n1-1)* m   +p  ],V(1,arange())))) / (norm(V(1,arange()))))
            if zhuangjijiao_down[2*(n1-1)* m   +p  ] >= 0:
                Cp_down[2*(n1-1)* m   +p  ]=Newton1(zhuangjijiao_down[2*(n1-1)* m   +p  ],V(1,1),V(1,2),V(1,3),Ma)
            if zhuangjijiao_down[2*(n1-1)* m   +p  ] < 0:
                Cp_down[2*(n1-1)* m   +p  ]=Qie2(zhuangjijiao_down[2*(n1-1)* m   +p  ],V(1,1),V(1,2),V(1,3),Ma)
            #��������
            F_down[2*(n1-1)* m   +p  ]=multiply(A_down[2*(n1-1)* m   +p  ],(multiply(multiply(multiply(Cp_down[2*(n1-1)* m   +p  ],0.5),midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)) + p_lailiu))
            CA_down[2*(n1-1)* m   +p  ]=multiply(F_down[2*(n1-1)* m   +p  ],N_B1_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),1)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            CN_down[2*(n1-1)* m   +p  ]=multiply(F_down[2*(n1-1)* m   +p  ],N_B1_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),3)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            CZ_down[2*(n1-1)* m   +p  ]=multiply(F_down[2*(n1-1)* m   +p  ],N_B1_danwei((p + multiply(dot(2,(m - 1)),(n1 - 1))),2)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            Cl_down[2*(n1-1)* m   +p  ]=multiply(CN_down[2*(n1-1)* m   +p  ],cos(AttackAngle)) - multiply(CA_down[2*(n1-1)* m   +p  ],sin(AttackAngle))
            Cd_down[2*(n1-1)* m   +p  ]=multiply(CN_down[2*(n1-1)* m   +p  ],sin(AttackAngle)) + multiply(CA_down[2*(n1-1)* m   +p  ],cos(AttackAngle))
        ####################һ׶����####################
        ####################��׶####################
        for p in arange((n1 + 1),(dot(2,n1) - 1)).reshape(-1):
            T1_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=B2(multiply(dot(2,n1),m) + p + 1,arange()) - B2[2*(n1-1)* m   +p  ]
            T2_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=B2[2*(n1-1)* m   +p+1] - B2(multiply(dot(2,n1),m) + p,arange())
            N_B2[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=cross(T2_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),T1_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            N_B2_fanshu[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=norm(N_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            N_B2_danwei[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=- (N_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange())) / (N_B2_fanshu((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            Average_B2[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(0.25,(B2[2*(n1-1)* m   +p  ] + B2(multiply(dot(2,n1),m) + p,arange()) + B2(multiply(dot(2,n1),m) + p + 1,arange()) + B2[2*(n1-1)* m   +p+1]))
            #���ĸ��ǵ�ͶӰ����Ԫƽ����
            B2_tou[multiply(dot(2,n1),(m - 1)) + p,arange()]=B2[2*(n1-1)* m   +p  ] + multiply(N_B2_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) - B2[2*(n1-1)* m   +p  ]))
            B2_tou[multiply(dot(2,n1),m) + p,arange()]=B2(multiply(dot(2,n1),m) + p,arange()) + multiply(N_B2_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) - B2(multiply(dot(2,n1),m) + p,arange())))
            B2_tou[multiply(dot(2,n1),m) + p + 1,arange()]=B2(multiply(dot(2,n1),m) + p + 1,arange()) + multiply(N_B2_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) - B2(multiply(dot(2,n1),m) + p + 1,arange())))
            B2_tou[multiply(dot(2,n1),(m - 1)) + p + 1,arange()]=B2[2*(n1-1)* m   +p+1] + multiply(N_B2_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) - B2[2*(n1-1)* m   +p+1]))
            #������Ԫ����ϵ:ԭ��λ��X_bar��Y_bar��Z_bar��x��ƽ����t1_down,y��ƽ����m��z��ƽ����n
            T1_down_fanshu[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=norm(T1_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            T1_down_danwei[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=T1_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) / T1_down_fanshu((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange())
            m_danwei_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=cross(N_B2_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()))
            #��ͶӰ��ӷ���������ϵת������Ԫ�����?
       #x
            B2_myx[multiply(dot(2,n1),(m - 1)) + p,1]=multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),m) + p,1]=multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),m) + p + 1,1]=multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),m) + p + 1,1) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),m) + p + 1,2) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),m) + p + 1,3) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),(m - 1)) + p + 1,1]=multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,1) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,2) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,3) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            #y
            B2_myx[multiply(dot(2,n1),(m - 1)) + p,2]=multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),m) + p,2]=multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,1) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,2) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p,3) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),m) + p + 1,2]=multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),m) + p + 1,1) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),m) + p + 1,2) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),m) + p + 1,3) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            B2_myx[multiply(dot(2,n1),(m - 1)) + p + 1,2]=multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,1) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1))) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,2) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),(B2_tou(multiply(dot(2,n1),(m - 1)) + p + 1,3) - Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)))
            #z
            B2_myx[multiply(dot(2,n1),(m - 1)) + p,3]=0
            B2_myx[multiply(dot(2,n1),m) + p,3]=0
            B2_myx[multiply(dot(2,n1),m) + p + 1,3]=0
            B2_myx[multiply(dot(2,n1),(m - 1)) + p + 1,3]=0
            #����Ԫ�������A
            A_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(multiply(0.5,(B2_myx(multiply(dot(2,n1),m) + p + 1,1) - B2_myx(multiply(dot(2,n1),(m - 1)) + p,1))),(B2_myx(multiply(dot(2,n1),m) + p,1) - B2_myx(multiply(dot(2,n1),(m - 1)) + p + 1,1)))
            ZhiXin_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1]=multiply(multiply((1 / 3),(1.0 / (B2_myx(multiply(dot(2,n1),m) + p,2) - B2_myx(multiply(dot(2,n1),(m - 1)) + p + 1,2)))),(multiply(B2_myx(multiply(dot(2,n1),(m - 1)) + p + 1,1),(B2_myx(multiply(dot(2,n1),(m - 1)) + p,2) - B2_myx(multiply(dot(2,n1),m) + p,2))) + multiply(B2_myx(multiply(dot(2,n1),m) + p,1),(B2_myx(multiply(dot(2,n1),(m - 1)) + p + 1,2) - B2_myx(multiply(dot(2,n1),(m - 1)) + p,2)))))
            ZhiXin_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2]=multiply(- (1 / 3),B2_myx(multiply(dot(2,n1),(m - 1)) + p,2))
            ZhiXin_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2]=0
            Zhixin_down_fxqzbx[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1]=Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),ZhiXin_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1),ZhiXin_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            Zhixin_down_fxqzbx[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2]=Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),ZhiXin_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2),ZhiXin_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            Zhixin_down_fxqzbx[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3]=Average_B2((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3) + multiply(T1_down_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),ZhiXin_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1)) + multiply(m_danwei_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3),ZhiXin_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2))
            zhuangjijiao_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=pi / 2 - acos((- (dot(N_B2_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),V(1,arange())))) / (norm(V(1,arange()))))
            if zhuangjijiao_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) >= 0:
                Cp_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=Newton1(zhuangjijiao_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),V(1,1),V(1,2),V(1,3),Ma)
            if zhuangjijiao_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()) < 0:
                Cp_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=Newton1(zhuangjijiao_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),V(1,1),V(1,2),V(1,3),Ma)
            #��������
            F_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(A_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),(multiply(multiply(multiply(Cp_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),0.5),midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)) + p_lailiu))
            CA_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(F_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),1)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            CN_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(F_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),3)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            CZ_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(F_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),N_B1_danwei((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),2)) / (dot(multiply(multiply(0.5,midu),(V(1,1) ** 2 + V(1,2) ** 2 + V(1,3) ** 2)),S_can))
            Cl_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(CN_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),cos(AttackAngle)) - multiply(CA_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),sin(AttackAngle))
            Cd_down[(p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()]=multiply(CN_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),sin(AttackAngle)) + multiply(CA_down((p - 1 + multiply(dot(2,(m - 1)),(n1 - 1))),arange()),cos(AttackAngle))
        ####################��׶����####################
    
    ###############################################################End-�±���###############################################################
    
    ###############################################################������ϵ��###############################################################
    
    #������ϵ��
    CA=sum(ravel(CA_up)) + sum(ravel(CA_down))
    #������ϵ��
    CN=sum(ravel(CN_up)) + sum(ravel(CN_down))
    #������ϵ��
    CZ=sum(ravel(CZ_up)) + sum(ravel(CZ_down))
    #����ϵ��
    Cl=sum(ravel(Cl_up)) + sum(ravel(Cl_down))
    #����ϵ��
    Cd=sum(ravel(Cd_up)) + sum(ravel(Cd_down))
    #�����?
    K=Cl / Cd
    #��������ϵ��
    Gusuan[1]=CA
    Gusuan[2]=CN
    Gusuan[3]=CZ
    Gusuan[4]=Cl
    Gusuan[5]=Cd
    Gusuan[6]=K
    ###############################################################End-����ϵ��###############################################################
    return zhuangjijiao_up
    