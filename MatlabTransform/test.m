clc;
clear;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%来流条件%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% V(1,1)=input('Vx:'); 
% V(1,2)=input('Vy:'); 
% V(1,3)=input('Vz:');  
% Ma=input('Ma:'); 
% midu=input('来流密度：');
% p_lailiu=input('来流压力：');
% S_can=input('参考面积：');
% L_can=input('参考长度：');
% AttackAngle=input('攻角：');
V(1,1)=4871.833604; 
V(1,2)=0; 
V(1,3)=859.0098528;
Ma=15; 
midu=0.00102688;
p_lailiu=79.7791;
AttackAngle=10;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%来流条件输入结束%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

top_folder='E:\CST\Part2\';
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%输入设计变量%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%定义设计变量因素
L=5;
number=1;
% L=input('飞行器总长:');
% number=input('请输入设计变量的水平数:');
L_can=L;
for i=1:number
   Wmax(i)=1.8;
   L1(i)=1;
   theta_u_1_deg(i)=3;
   theta_l_1_deg(i)=1;
   theta_u_2_deg(i)=6.5;
   theta_l_2_deg(i)=3.5;
   %转化为弧度制
   theta_u_1(i)= theta_u_1_deg(i)./180.*pi;
   theta_l_1(i)= theta_l_1_deg(i)./180.*pi;
   theta_u_2(i)= theta_u_2_deg(i)./180.*pi;
   theta_l_2(i)= theta_l_2_deg(i)./180.*pi;
  
   Nc_u_1(i)=3;
   Nc_l_1(i)=0.5;
   Nc_u_2(i)=0.5;
   Nc_l_2(i)=2;
   n(i)=0.55;
end
% for i=1:number
%    Wmax(i)= input('飞行器宽度:');
%    L1(i)= input('第一锥长度:');
%    theta_u_1_deg(i)= input('第一锥上半锥角(deg):');
%    theta_l_1_deg(i)= input('第一锥下半锥角(deg):');
%    theta_u_2_deg(i)= input('第二锥上半锥角(deg):');
%    theta_l_2_deg(i)= input('第二锥下半锥角(deg):');
%    %转化为弧度制
%    theta_u_1(i)= theta_u_1_deg(i)./180.*pi;
%    theta_l_1(i)= theta_l_1_deg(i)./180.*pi;
%    theta_u_2(i)= theta_u_2_deg(i)./180.*pi;
%    theta_l_2(i)= theta_l_2_deg(i)./180.*pi;
%   
%    Nc_u_1(i)= input('第一锥上表面型线控制参数:');
%    Nc_l_1(i)= input('第一锥下表面型线控制参数:');
%    Nc_u_2(i)= input('第二锥上表面型线控制参数:');
%    Nc_l_2(i)= input('第二锥下表面型线控制参数:');
%    n(i)=input('轮廓曲线控制参数:');
% end
Duozhui_N=number^11;%%%给定的样本量是多少
YangBen=zeros(Duozhui_N,11);
Duozhui_N_k=1;
for i1=1:number
    for i2=1:number
        for i3=1:number
            for i4=1:number
                for i5=1:number
                    for i6=1:number
                        for i7=1:number
                            for i8=1:number
                                for i9=1:number
                                    for i10=1:number
                                        for i11=1:number
                                            YangBen(Duozhui_N_k,:) =[Wmax(i1),L1(i2),theta_u_1(i3),theta_l_1(i4),theta_u_2(i5),theta_l_2(i6),Nc_u_1(i7),Nc_l_1(i8),Nc_u_2(i9),Nc_l_2(i10),n(i11)];
                                            Duozhui_N_k=Duozhui_N_k+1;
                                        end
                                   end
                               end
                           end
                       end
                   end
               end
           end
       end
    end
end

print(YangBen)

%%%%%%%%%%%x、y方向分别分成多少份%%%%%%%%%%%
n0=100;%每一个截面沿y方向分成多少份
n1=50;%每一锥沿长度x方向分成多少个截面
qidongxishu=zeros(Duozhui_N,6);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%滑翔升力体参数化%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for i0=1:Duozhui_N
    %%%%%%%%%%其他参数计算%%%%%%%%%%
    %%%锥体剩余参数计算
    L2(i0)=L-YangBen(i0,2);%第二锥长度
    Wmax1=YangBen(i0,1)./(L.^YangBen(i0,11)).*YangBen(i0,2).^YangBen(i0,11);%计算第一锥的最大宽度
    %%%划分截面所需的参数计算
    l=linspace(0,L,2*n1);%沿长度方向底面截面分为n1份
    l1=linspace(0,YangBen(i0,2),n1);
    l2=linspace(YangBen(i0,2),L,n1);
    x=zeros(2*n1,n0);
    %%%%%%%%%%其他参数计算完成%%%%%%%%%%

    %%%%%%%%%%飞行器参数化开始%%%%%%%%%%
    %第一锥飞行器参数化
    for i=1:n1
        W1(i,:)=YangBen(i0,1)./(L.^YangBen(i0,11)).*l1(i).^(YangBen(i0,11));%计算各截面的宽度
        Hu1(i)=tan(YangBen(i0,3)).*l1(i);%计算各截面上曲线的高度
        Hl1(i)=tan(YangBen(i0,4)).*l1(i);%计算各截面下曲线的高度
        y1(i,:)=linspace(-W1(i)/2,W1(i)/2,n0);%宽度沿y方向变化
        x1(i,:)=l1(i);%某一长度位置的飞行器截面
        
        zu1(i,:)= +Hu1(i)
                    .*(+y1(i,:)/W1(i)+0.5).^(YangBen(i0,7))       
                    .*(-y1(i,:)/W1(i)+0.5).^(YangBen(i0,7))   
                    .*2.^(2.*YangBen(i0,7));
        zl1(i,:)=(-Hl1(i)
                    .*(+y1(i,:)/W1(i)+0.5).^(YangBen(i0,8))
                    .*(-y1(i,:)/W1(i)+0.5).^(YangBen(i0,8))
                    .*2.^(2.*YangBen(i0,8)));
        
        if isnan(zu1(i,:))
          zu1(i,:)=0;
        end
        if isnan(zl1(i,:))
          zl1(i,:)=0;
        end
    end
    %第二锥飞行器参数化
    for i=1:n1
        W2(i,:)=Wmax./(L.^YangBen(i0,11)).*l2(i).^(YangBen(i0,11));%计算各截面的宽度
        Hu2(i)=tan(YangBen(i0,5)).*(l2(i)-YangBen(i0,2));%计算各截面上曲线的高度
        Hl2(i)=tan(YangBen(i0,6)).*(l2(i)-YangBen(i0,2));%计算各截面下曲线的高度
        y2(i,:)=linspace(-W2(i)/2,W2(i)/2,n0);%宽度沿y方向变化
        x2(i,:)=l2(i);%某一长度位置的飞行器截面
        
        zu2(i,:)=+Hu2(i)
                    .*(y2(i,:)/W2(i)+0.5).^(YangBen(i0,9))
                    .*(0.5-y2(i,:)/W2(i)).^(YangBen(i0,9))
                    .*2.^(2.*YangBen(i0,9))
                    +zu1(n1,:);
        zl2(i,:)=-Hl2(i)
                    .*(y2(i,:)/W2(i)+0.5).^(YangBen(i0,10))
                    .*(0.5-y2(i,:)/W2(i)).^(YangBen(i0,10))
                    .*2.^(2.*YangBen(i0,10))
                    +zl1(n1,:);

        if isnan(zu2(i,:))
          zu2(i,:)=0;
        end
        if isnan(zl2(i,:))
          zl2(i,:)=0;
        end
    end
    
    %把第一锥和第二锥的数组粘合到一起
    x=[x1;x2];
    y=[y1;y2];
    zu=[zu1;zu2];
    zl=[zl1;zl2];
    
    %UG格式输出
    %生成上表面
    B1=zeros(2*n1*n0,3);
    for j1=1:n0
        for k1=1:2*n1
            B1(2*n1*(j1-1)+k1,1)=x(k1);
            B1(2*n1*(j1-1)+k1,2)=y(k1,j1);
            B1(2*n1*(j1-1)+k1,3)=zu(k1,j1);
        end
    end
    %生成下表面
    B2=zeros(2*n1*n0,3);
    for j1=1:n0
        for k1=1:2*n1
            B2(2*n1*(j1-1)+k1,1)=x(k1);
            B2(2*n1*(j1-1)+k1,2)=y(k1,j1);
            B2(2*n1*(j1-1)+k1,3)=zl(k1,j1);
        end
    end
%     %插值，生成底面
%     zc1=ones(2*n1,n0);
%     zc2=ones(2*n1,n0);
%     zc3=ones(2*n1,n0);
%     zc1=(zu+zl)/2;
%     zc2=(zu+zc1)/2;
%     zc3=(zl+zc1)/2;
%     B3=zeros(5*(n0-2),3);
%     for j1=1:n0
%         for k1=1:5
%             B3(5*(j1-1)+k1,1)=x(2*n1);
%             B3(5*(j1-1)+k1,2)=y(2*n1,j1);
%             if mod(k1,5)==1
%                B3(5*(j1-1)+k1,3)=zu(2*n1,j1);
%             elseif mod(k1,5)==2
%                B3(5*(j1-1)+k1,3)=zc2(2*n1,j1);
%             elseif mod(k1,5)==3
%                B3(5*(j1-1)+k1,3)=zc1(2*n1,j1);
%             elseif mod(k1,5)==4
%                B3(5*(j1-1)+k1,3)=zc3(2*n1,j1);
%             elseif mod(k1,5)==0
%                B3(5*(j1-1)+k1,3)=zl(2*n1,j1);
%             end
%         end
%     end
% 
%     %%%%%%将数组输出到文件中%%%%%%    
%     
%     %新建文件夹
%     second_folder=sprintf('%s%s',top_folder,int2str(i0));
%     mkdir(second_folder);
%   
%     %上表面
%     UP=sprintf('%s%s',second_folder,'\up.dat');
%     fid = fopen(UP,'wt');
%     for m=1:n0
%         fprintf(fid,'%s\n','ROW');
%         fprintf(fid,'%f %f %f \n',B1(1+2*n1*(m-1):m*2*n1,:)');
%     end   
%     fclose(fid);
%     %下表面   
%     DOWN=sprintf('%s%s',second_folder,'\down.dat');
%     fid = fopen(DOWN,'wt');
%     for m=1:n0
%         fprintf(fid,'%s\n','ROW');
%         fprintf(fid,'%f %f %f \n',B2(1+2*n1*(m-1):m*2*n1,:)');
%     end
%     fclose(fid);
%      %底面
%     under=sprintf('%s%s',second_folder,'\udersurface.dat');
%     fid=fopen(under,'wt')
%     for m=2:(n0-1)
%         fprintf(fid,'%s\n','ROW');
%         fprintf(fid,'%f %f %f \n',B3(5*m-4:5*m,:)');
%     end
%     fclose(fid);
    %求参考面积
    for k=1:(n0-1)
       a_left(k)=zu(2*n1,k)-zl(2*n1,k);
       b_right(k)=zu(2*n1,k+1)-zl(2*n1,k+1);
       h(k)=y(2*n1,k+1)-y(2*n1,k);
       S_each(k)=(a_left(k)+b_right(k)).*h(k)*0.5;
    end
    S_can=sum(S_each(:));
    
    yucezhi=GCGS(n0,n1,B1,B2,V,p_lailiu,S_can,L_can,AttackAngle,Ma,midu);
%     qidongxishu(i0,1)=yucezhi(1);
%     qidongxishu(i0,2)=yucezhi(2);
%     qidongxishu(i0,3)=yucezhi(3);
%     qidongxishu(i0,4)=yucezhi(4);
%     qidongxishu(i0,5)=yucezhi(5);
%     qidongxishu(i0,6)=yucezhi(6);
    
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%滑翔升力体参数化结束%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%工程估算%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
function [zhuangjijiao_up]=GCGS(n0,n1,B1,B2,V,p_lailiu,S_can,L_can,AttackAngle,Ma,midu)
%%%%%%%%%%%面元法%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%上表面%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for m=1:(n0-1)
   %%%%%%%%%%%%%%%%%%%%一锥%%%%%%%%%% %%%%%%%%%%
   for p=1:(n1-1)
       T1_up((p+2*(m-1).*(n1-1)),:)=        +B1(2*n1.* m   +p+1,:)
                                            -B1(2*n1.*(m-1)+p  ,:);
       T2_up((p+2*(m-1).*(n1-1)),:)=        +B1(2*n1.*(m-1)+p+1,:)
                                            -B1(2*n1.* m   +p  ,:);

       N_B1((p+2*(m-1).*(n1-1)),:)=cross( T2_up((p+2*(m-1).*(n1-1)),:),
                                          T1_up((p+2*(m-1).*(n1-1)),:));
       N_B1_fanshu((p+2*(m-1).*(n1-1)),:)=norm(N_B1((p+2*(m-1).*(n1-1)),:));%求范数
       
       N_B1_danwei((p+2*(m-1).*(n1-1)),:)=(N_B1((p+2*(m-1).*(n1-1)),:))./(N_B1_fanshu((p+2*(m-1).*(n1-1)),:));%求单位向量n
       
       Average_B1((p+2*(m-1).*(n1-1)),:)=0.25.*(B1(2*n1.*(m-1)+p,:)+B1(2*n1.*m+p,:)+B1(2*n1.*m+p+1,:)+B1(2*n1.*(m-1)+p+1,:));%求每一个面元X、Y、Z的平均值
       
       %将四个角点投影到面元平面上
       B1_tou(2*n1.*(m-1)+p  ,:)=B1(2*n1.*(m-1)+p  ,:) + N_B1_danwei((p+2*(m-1).*(n1-1)),:).*(Average_B1((p+2*(m-1).*(n1-1)),:)-B1(2*n1.*(m-1)+p  ,:));%位置1
       
       B1_tou(2*n1.* m   +p  ,:)=B1(2*n1.* m   +p  ,:) + N_B1_danwei((p+2*(m-1).*(n1-1)),:).*(Average_B1((p+2*(m-1).*(n1-1)),:)-B1(2*n1.* m   +p  ,:));%位置2
       
       B1_tou(2*n1.* m   +p+1,:)=B1(2*n1.* m   +p+1,:) + N_B1_danwei((p+2*(m-1).*(n1-1)),:).*(Average_B1((p+2*(m-1).*(n1-1)),:)-B1(2*n1.* m   +p+1,:));%位置3
       B1_tou(2*n1.*(m-1)+p+1,:)=B1(2*n1.*(m-1)+p+1,:) + N_B1_danwei((p+2*(m-1).*(n1-1)),:).*(Average_B1((p+2*(m-1).*(n1-1)),:)-B1(2*n1.*(m-1)+p+1,:));%位置4
       
       %建立面元坐标系:原点位于X_bar、Y_bar、Z_bar，x轴平行于t1,y轴平行于m，z轴平行于n
       T1_up_fanshu((p+2*(m-1).*(n1-1)),:)=norm(T1_up((p+2*(m-1).*(n1-1)),:));%求T1_up的范数
       T1_up_danwei((p+2*(m-1).*(n1-1)),:)=T1_up((p+2*(m-1).*(n1-1)),:)./T1_up_fanshu((p+2*(m-1).*(n1-1)),:);%求T1_up的单位向量t1
       m_danwei_up((p+2*(m-1).*(n1-1)),:)=cross(N_B1_danwei((p+2*(m-1).*(n1-1)),:),T1_up_danwei((p+2*(m-1).*(n1-1)),:));%求第三个单位向量m
       
       %把投影点从飞行器坐标系转换到面元坐标系
       %x
       B1_myx(2*n1.*(m-1)+p,1)  =T1_up_danwei((p+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p,1)  -Average_B1((p+2*(m-1).*(n1-1)),1))
                                +T1_up_danwei((p+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p,2)  -Average_B1((p+2*(m-1).*(n1-1)),2))
                                +T1_up_danwei((p+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p,3)  -Average_B1((p+2*(m-1).*(n1-1)),3));%位置1
       B1_myx(2*n1.*m+p,1)      =T1_up_danwei((p+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*m+p,1)      -Average_B1((p+2*(m-1).*(n1-1)),1))
                                +T1_up_danwei((p+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*m+p,2)      -Average_B1((p+2*(m-1).*(n1-1)),2))
                                +T1_up_danwei((p+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*m+p,3)      -Average_B1((p+2*(m-1).*(n1-1)),3));%位置2
       B1_myx(2*n1.*m+p+1,1)    =T1_up_danwei((p+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*m+p+1,1)    -Average_B1((p+2*(m-1).*(n1-1)),1))
                                +T1_up_danwei((p+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*m+p+1,2)    -Average_B1((p+2*(m-1).*(n1-1)),2))
                                +T1_up_danwei((p+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*m+p+1,3)    -Average_B1((p+2*(m-1).*(n1-1)),3));%位置3
       B1_myx(2*n1.*(m-1)+p+1,1)=T1_up_danwei((p+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p+1,1)-Average_B1((p+2*(m-1).*(n1-1)),1))
                                +T1_up_danwei((p+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p+1,2)-Average_B1((p+2*(m-1).*(n1-1)),2))
                                +T1_up_danwei((p+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p+1,3)-Average_B1((p+2*(m-1).*(n1-1)),3));%位置4
       %y
       B1_myx(2*n1.*(m-1)+p,2)  =m_danwei_up((p+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p,1)   -Average_B1((p+2*(m-1).*(n1-1)),1))
                                +m_danwei_up((p+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p,2)   -Average_B1((p+2*(m-1).*(n1-1)),2))
                                +m_danwei_up((p+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p,3)   -Average_B1((p+2*(m-1).*(n1-1)),3));%位置1
       B1_myx(2*n1.*m+p,2)      =m_danwei_up((p+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*m+p,1)       -Average_B1((p+2*(m-1).*(n1-1)),1))
                                +m_danwei_up((p+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*m+p,2)       -Average_B1((p+2*(m-1).*(n1-1)),2))
                                +m_danwei_up((p+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*m+p,3)       -Average_B1((p+2*(m-1).*(n1-1)),3));%位置2
       B1_myx(2*n1.*m+p+1,2)    =m_danwei_up((p+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*m+p+1,1)     -Average_B1((p+2*(m-1).*(n1-1)),1))
                                +m_danwei_up((p+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*m+p+1,2)     -Average_B1((p+2*(m-1).*(n1-1)),2))
                                +m_danwei_up((p+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*m+p+1,3)     -Average_B1((p+2*(m-1).*(n1-1)),3));%位置3
       B1_myx(2*n1.*(m-1)+p+1,2)=m_danwei_up((p+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p+1,1) -Average_B1((p+2*(m-1).*(n1-1)),1))
                                +m_danwei_up((p+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p+1,2) -Average_B1((p+2*(m-1).*(n1-1)),2))
                                +m_danwei_up((p+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p+1,3) -Average_B1((p+2*(m-1).*(n1-1)),3));%位置4
       %z
       B1_myx(2*n1.*(m-1)+p  ,3)=0;%位置1
       B1_myx(2*n1.* m   +p  ,3)=0;%位置2
       B1_myx(2*n1.* m   +p+1,3)=0;%位置3
       B1_myx(2*n1.*(m-1)+p+1,3)=0;%位置4
       
       %求面元的面积△A
       A_up((p-0+2*(m-1).*(n1-1)),:)=0.5
                                        .*(B1_myx(2*n1.*m+p+1,1)-B1_myx(2*n1.*(m-1)+p  ,1))
                                        .*(B1_myx(2*n1.*m+p  ,1)-B1_myx(2*n1.*(m-1)+p+1,1));
       %求面元质心的坐标
       ZhiXin_up((p+2*(m-1).*(n1-1)),1)=(1/3)   .*(1./(B1_myx(2*n1.*m+p,2)   -B1_myx(2*n1.*(m-1)+p+1,2)))
                                                .*(    
                                                +   B1_myx(2*n1.*(m-1)+p+1,1)
                                                .*( B1_myx(2*n1.*(m-1)+p,2)  -B1_myx(2*n1.*m+p,2))
                                                
                                                +   B1_myx(2*n1.*m+p,1)
                                                .*( B1_myx(2*n1.*(m-1)+p+1,2)-B1_myx(2*n1.*(m-1)+p,2))
                                                );
       ZhiXin_up((p+2*(m-1).*(n1-1)),2)=(-1/3).*B1_myx(2*n1.*(m-1)+p,2);
       ZhiXin_up((p+2*(m-1).*(n1-1)),3)=0;
       %质心在飞行器坐标系中的质心坐标
       Zhixin_up_fxqzbx((p+2*(m-1).*(n1-1)),1)=Average_B1((p+2*(m-1).*(n1-1)),1)+T1_up_danwei((p+2*(m-1).*(n1-1)),1).*ZhiXin_up((p+2*(m-1).*(n1-1)),1)+m_danwei_up((p+2*(m-1).*(n1-1)),1).*ZhiXin_up((p+2*(m-1).*(n1-1)),2);
       Zhixin_up_fxqzbx((p+2*(m-1).*(n1-1)),2)=Average_B1((p+2*(m-1).*(n1-1)),2)+T1_up_danwei((p+2*(m-1).*(n1-1)),2).*ZhiXin_up((p+2*(m-1).*(n1-1)),1)+m_danwei_up((p+2*(m-1).*(n1-1)),2).*ZhiXin_up((p+2*(m-1).*(n1-1)),2);
       Zhixin_up_fxqzbx((p+2*(m-1).*(n1-1)),3)=Average_B1((p+2*(m-1).*(n1-1)),3)+T1_up_danwei((p+2*(m-1).*(n1-1)),3).*ZhiXin_up((p+2*(m-1).*(n1-1)),1)+m_danwei_up((p+2*(m-1).*(n1-1)),3).*ZhiXin_up((p+2*(m-1).*(n1-1)),2);
       %撞击角
       zhuangjijiao_up((p+2*(m-1).*(n1-1)),:)=pi/2-acos((-(dot(N_B1_danwei((p+2*(m-1).*(n1-1)),:),V(1,:))))./(norm(V(1,:))));
       %代入工程估算
       if zhuangjijiao_up((p+2*(m-1).*(n1-1)),:)>=0
           Cp_up((p+2*(m-1).*(n1-1)),:)=Newton1(zhuangjijiao_up((p+2*(m-1).*(n1-1)),:),V(1,1),V(1,2),V(1,3),Ma);
       end
       if zhuangjijiao_up((p+2*(m-1).*(n1-1)),:)<0
           Cp_up((p+2*(m-1).*(n1-1)),:)=Newton1(zhuangjijiao_up((p+2*(m-1).*(n1-1)),:),V(1,1),V(1,2),V(1,3),Ma);
       end
       %求作用力
       F_up((p+2*(m-1).*(n1-1)),:)=A_up((p+2*(m-1).*(n1-1)),:).*(Cp_up((p+2*(m-1).*(n1-1)),:).*0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)+p_lailiu);
       %轴向力系数
       CA_up((p+2*(m-1).*(n1-1)),:)=F_up((p+2*(m-1).*(n1-1)),:).*N_B1_danwei((p+2*(m-1).*(n1-1)),1)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %法向力系数
       CN_up((p+2*(m-1).*(n1-1)),:)=F_up((p+2*(m-1).*(n1-1)),:).*N_B1_danwei((p+2*(m-1).*(n1-1)),3)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %横向力系数
       CZ_up((p+2*(m-1).*(n1-1)),:)=F_up((p+2*(m-1).*(n1-1)),:).*N_B1_danwei((p+2*(m-1).*(n1-1)),2)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %升力系数
       Cl_up((p+2*(m-1).*(n1-1)),:)=CN_up((p+2*(m-1).*(n1-1)),:).*cos(AttackAngle)-CA_up((p+2*(m-1).*(n1-1)),:).*sin(AttackAngle);
       %阻力系数
       Cd_up((p+2*(m-1).*(n1-1)),:)=CN_up((p+2*(m-1).*(n1-1)),:).*sin(AttackAngle)+CA_up((p+2*(m-1).*(n1-1)),:).*cos(AttackAngle);
       
       
   end
   %%%%%%%%%%%%%%%%%%%%一锥结束%%%%%%%%%%%%%%%%%%%% 
   
   %%%%%%%%%%%%%%%%%%%%二锥%%%%%%%%%%%%%%%%%%%%
   for p=(n1+1):(2*n1-1)
       T1_up((p-1+2*(m-1).*(n1-1)),:)=  +B1(2*n1.* m   +p+1,:)
                                        -B1(2*n1.*(m-1)+p  ,:);
       T2_up((p-1+2*(m-1).*(n1-1)),:)=  +B1(2*n1.*(m-1)+p+1,:)
                                        -B1(2*n1.* m   +p  ,:);
       N_B1 ((p-1+2*(m-1).*(n1-1)),:)=cross(T2_up((p-1+2*(m-1).*(n1-1)),:),
                                            T1_up((p-1+2*(m-1).*(n1-1)),:));
       
       N_B1_fanshu((p-1+2*(m-1).*(n1-1)),:)=norm(N_B1((p-1+2*(m-1).*(n1-1)),:));%求范数
       N_B1_danwei((p-1+2*(m-1).*(n1-1)),:)=(N_B1((p-1+2*(m-1).*(n1-1)),:))./(N_B1_fanshu((p-1+2*(m-1).*(n1-1)),:));%求单位向量n
       
       Average_B1((p-1+2*(m-1).*(n1-1)),:)=0.25.*(
           +B1(2*n1.*(m-1)+p  ,:)
           +B1(2*n1.* m   +p  ,:)
           +B1(2*n1.* m   +p+1,:)
           +B1(2*n1.*(m-1)+p+1,:));%求每一个面元X、Y、Z的平均值
       
       %将四个角点投影到面元平面上
       B1_tou(2*n1.*(m-1)+p  ,:)=B1(2*n1.*(m-1)+p  ,:)+N_B1_danwei((p-1+2*(m-1).*(n1-1)),:).*(Average_B1((p-1+2*(m-1).*(n1-1)),:)-B1(2*n1.*(m-1)+p  ,:));%位置1
       B1_tou(2*n1.* m   +p  ,:)=B1(2*n1.* m   +p  ,:)+N_B1_danwei((p-1+2*(m-1).*(n1-1)),:).*(Average_B1((p-1+2*(m-1).*(n1-1)),:)-B1(2*n1.* m   +p  ,:));%位置2
       B1_tou(2*n1.* m   +p+1,:)=B1(2*n1.* m   +p+1,:)+N_B1_danwei((p-1+2*(m-1).*(n1-1)),:).*(Average_B1((p-1+2*(m-1).*(n1-1)),:)-B1(2*n1.* m   +p+1,:));%位置3
       B1_tou(2*n1.*(m-1)+p+1,:)=B1(2*n1.*(m-1)+p+1,:)+N_B1_danwei((p-1+2*(m-1).*(n1-1)),:).*(Average_B1((p-1+2*(m-1).*(n1-1)),:)-B1(2*n1.*(m-1)+p+1,:));%位置4
       
       %建立面元坐标系:原点位于X_bar、Y_bar、Z_bar，x轴平行于t1_up,y轴平行于m，z轴平行于n
       T1_up_fanshu((p-1+2*(m-1).*(n1-1)),:)=       norm(T1_up((p-1+2*(m-1).*(n1-1)),:));%求T1_up的范数
       T1_up_danwei((p-1+2*(m-1).*(n1-1)),:)=            T1_up((p-1+2*(m-1).*(n1-1)),:)./
                                                  T1_up_fanshu((p-1+2*(m-1).*(n1-1)),:);%求T1_up的单位向量t1_up
       m_danwei_up ((p-1+2*(m-1).*(n1-1)),:)=cross(N_B1_danwei((p-1+2*(m-1).*(n1-1)),:),
                                                  T1_up_danwei((p-1+2*(m-1).*(n1-1)),:));%求第三个单位向量m
       
       %把投影点从飞行器坐标系转换到面元坐标系
       %x
       B1_myx(2*n1.*(m-1)+p  ,1)=T1_up_danwei((p-1+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p,1)    -Average_B1((p-1+2*(m-1).*(n1-1)),1))
                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p,2)    -Average_B1((p-1+2*(m-1).*(n1-1)),2))
                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p,3)    -Average_B1((p-1+2*(m-1).*(n1-1)),3));%位置1
       B1_myx(2*n1.* m   +p  ,1)=T1_up_danwei((p-1+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p,1)    -Average_B1((p-1+2*(m-1).*(n1-1)),1))
                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p,2)    -Average_B1((p-1+2*(m-1).*(n1-1)),2))
                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p,3)    -Average_B1((p-1+2*(m-1).*(n1-1)),3));%位置2
       B1_myx(2*n1.* m   +p+1,1)=T1_up_danwei((p-1+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*m+p+1,1)      -Average_B1((p-1+2*(m-1).*(n1-1)),1))
                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*m+p+1,2)      -Average_B1((p-1+2*(m-1).*(n1-1)),2))
                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*m+p+1,3)      -Average_B1((p-1+2*(m-1).*(n1-1)),3));%位置3
       B1_myx(2*n1.*(m-1)+p+1,1)=T1_up_danwei((p-1+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p+1,1)  -Average_B1((p-1+2*(m-1).*(n1-1)),1))
                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p+1,2)  -Average_B1((p-1+2*(m-1).*(n1-1)),2))
                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p+1,3)  -Average_B1((p-1+2*(m-1).*(n1-1)),3));%位置4
       %y
       B1_myx(2*n1.*(m-1)+p  ,2)=m_danwei_up((p-1+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p,1)     -Average_B1((p-1+2*(m-1).*(n1-1)),1))
                                +m_danwei_up((p-1+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p,2)     -Average_B1((p-1+2*(m-1).*(n1-1)),2))
                                +m_danwei_up((p-1+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p,3)     -Average_B1((p-1+2*(m-1).*(n1-1)),3));%位置1
       B1_myx(2*n1.* m   +p  ,2)=m_danwei_up((p-1+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p,1)     -Average_B1((p-1+2*(m-1).*(n1-1)),1))
                                +m_danwei_up((p-1+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p,2)     -Average_B1((p-1+2*(m-1).*(n1-1)),2))
                                +m_danwei_up((p-1+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p,3)     -Average_B1((p-1+2*(m-1).*(n1-1)),3));%位置2
       B1_myx(2*n1.* m   +p+1,2)=m_danwei_up((p-1+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*m+p+1,1)       -Average_B1((p-1+2*(m-1).*(n1-1)),1))
                                +m_danwei_up((p-1+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*m+p+1,2)       -Average_B1((p-1+2*(m-1).*(n1-1)),2))
                                +m_danwei_up((p-1+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*m+p+1,3)       -Average_B1((p-1+2*(m-1).*(n1-1)),3));%位置3
       B1_myx(2*n1.*(m-1)+p+1,2)=m_danwei_up((p-1+2*(m-1).*(n1-1)),1).*(B1_tou(2*n1.*(m-1)+p+1,1)   -Average_B1((p-1+2*(m-1).*(n1-1)),1))
                                +m_danwei_up((p-1+2*(m-1).*(n1-1)),2).*(B1_tou(2*n1.*(m-1)+p+1,2)   -Average_B1((p-1+2*(m-1).*(n1-1)),2))
                                +m_danwei_up((p-1+2*(m-1).*(n1-1)),3).*(B1_tou(2*n1.*(m-1)+p+1,3)   -Average_B1((p-1+2*(m-1).*(n1-1)),3));%位置4
       %z
       B1_myx(2*n1.*(m-1)+p  ,3)=0;%位置1
       B1_myx(2*n1.* m   +p  ,3)=0;%位置2
       B1_myx(2*n1.* m   +p+1,3)=0;%位置3
       B1_myx(2*n1.*(m-1)+p+1,3)=0;%位置4

       %求面元的面积△A
       A_up((p-1+2*(m-1).*(n1-1)),:)=0.5
                                        .*(B1_myx(2*n1.*m+p+1,1)-B1_myx(2*n1.*(m-1)+p  ,1))
                                        .*(B1_myx(2*n1.*m+p  ,1)-B1_myx(2*n1.*(m-1)+p+1,1));
    
       %求面元质心的坐标
       ZhiXin_up((p-1+2*(m-1).*(n1-1)),1)= (1/3).*(1./(B1_myx(2*n1.* m   +p  ,2)-B1_myx(2*n1.*(m-1)+p+1,2))).*(
                                                      +B1_myx(2*n1.*(m-1)+p+1,1)
                                                    .*(B1_myx(2*n1.*(m-1)+p  ,2)-B1_myx(2*n1.* m   +p  ,2))
                                                      +B1_myx(2*n1.* m   +p  ,1)
                                                    .*(B1_myx(2*n1.*(m-1)+p+1,2)-B1_myx(2*n1.*(m-1)+p  ,2))); 
       ZhiXin_up((p-1+2*(m-1).*(n1-1)),2)=-(1/3).*B1_myx(2*n1.*(m-1)+p,2);
       ZhiXin_up((p-1+2*(m-1).*(n1-1)),2)=0;
       %质心在飞行器坐标系中的质心坐标
       Zhixin_up_fxqzbx((p-1+2*(m-1).*(n1-1)),1)=  Average_B1((p-1+2*(m-1).*(n1-1)),1)
                                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),1).*ZhiXin_up((p-1+2*(m-1).*(n1-1)),1)
                                                + m_danwei_up((p-1+2*(m-1).*(n1-1)),1).*ZhiXin_up((p-1+2*(m-1).*(n1-1)),2);
       Zhixin_up_fxqzbx((p-1+2*(m-1).*(n1-1)),2)=  Average_B1((p-1+2*(m-1).*(n1-1)),2)
                                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),2).*ZhiXin_up((p-1+2*(m-1).*(n1-1)),1)
                                                + m_danwei_up((p-1+2*(m-1).*(n1-1)),2).*ZhiXin_up((p-1+2*(m-1).*(n1-1)),2);
       Zhixin_up_fxqzbx((p-1+2*(m-1).*(n1-1)),3)=  Average_B1((p-1+2*(m-1).*(n1-1)),3)
                                                +T1_up_danwei((p-1+2*(m-1).*(n1-1)),3).*ZhiXin_up((p-1+2*(m-1).*(n1-1)),1)
                                                + m_danwei_up((p-1+2*(m-1).*(n1-1)),3).*ZhiXin_up((p-1+2*(m-1).*(n1-1)),2);
       %撞击角
       zhuangjijiao_up((p-1+2*(m-1).*(n1-1)),:)=pi/2-acos((-(dot(N_B1_danwei((p-1+2*(m-1).*(n1-1)),:),V(1,:))))./(norm(V(1,:))));
       %代入工程估算
       if zhuangjijiao_up((p-1+2*(m-1).*(n1-1)),:)>=0
           Cp_up((p-1+2*(m-1).*(n1-1)),:)=Newton1(zhuangjijiao_up((p-1+2*(m-1).*(n1-1)),:),V(1,1),V(1,2),V(1,3),Ma);
       end
       if zhuangjijiao_up((p-1+2*(m-1).*(n1-1)),:)<0
           Cp_up((p-1+2*(m-1).*(n1-1)),:)=Newton1(zhuangjijiao_up((p-1+2*(m-1).*(n1-1)),:),V(1,1),V(1,2),V(1,3),Ma);
       end
       %求作用力
       F_up((p-1+2*(m-1).*(n1-1)),:)=A_up((p-1+2*(m-1).*(n1-1)),:).*(Cp_up((p-1+2*(m-1).*(n1-1)),:).*0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)+p_lailiu);
       
       %轴向力系数
       CA_up((p-1+2*(m-1).*(n1-1)),:)=F_up((p-1+2*(m-1).*(n1-1)),:).*N_B1_danwei((p-1+2*(m-1).*(n1-1)),1)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %法向力系数
       CN_up((p-1+2*(m-1).*(n1-1)),:)=F_up((p-1+2*(m-1).*(n1-1)),:).*N_B1_danwei((p-1+2*(m-1).*(n1-1)),3)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %横向力系数
       CZ_up((p-1+2*(m-1).*(n1-1)),:)=F_up((p-1+2*(m-1).*(n1-1)),:).*N_B1_danwei((p-1+2*(m-1).*(n1-1)),2)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       
       %升力系数
       Cl_up((p-1+2*(m-1).*(n1-1)),:)=CN_up((p-1+2*(m-1).*(n1-1)),:).*cos(AttackAngle)-CA_up((p-1+2*(m-1).*(n1-1)),:).*sin(AttackAngle);
       %阻力系数
       Cd_up((p-1+2*(m-1).*(n1-1)),:)=CN_up((p-1+2*(m-1).*(n1-1)),:).*sin(AttackAngle)+CA_up((p-1+2*(m-1).*(n1-1)),:).*cos(AttackAngle);
       
       
   end
   %%%%%%%%%%%%%%%%%%%%二锥结束%%%%%%%%%%%%%%%%%%%%
   
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%End---上表面%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%下表面%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for m=1:(n0-1)
   %%%%%%%%%%%%%%%%%%%%一锥%%%%%%%%%% %%%%%%%%%%
   for p=1:(n1-1)
       T1_down((p+2*(m-1).*(n1-1)),:)=
            +B2(2*n1.* m   +p+1,:)
            -B2(2*n1.*(m-1)+p  ,:);
       T2_down((p+2*(m-1).*(n1-1)),:)=
            +B2(2*n1.*(m-1)+p+1,:)
            -B2(2*n1.* m   +p  ,:);
       N_B2((p+2*(m-1).*(n1-1)),:)=cross(
        T2_down((p+2*(m-1).*(n1-1)),:),
        T1_down((p+2*(m-1).*(n1-1)),:));
       
       N_B2_fanshu((p+2*(m-1).*(n1-1)),:)=norm(N_B2((p+2*(m-1).*(n1-1)),:));%求范数
       N_B2_danwei((p+2*(m-1).*(n1-1)),:)=-(N_B2((p+2*(m-1).*(n1-1)),:))
                                  ./(N_B2_fanshu((p+2*(m-1).*(n1-1)),:));%求单位向量n
       
       Average_B2((p+2*(m-1).*(n1-1)),:)=0.25.*(
              +B2(2*n1.*(m-1)+p  ,:)
              +B2(2*n1.* m   +p  ,:)
              +B2(2*n1.* m   +p+1,:)
              +B2(2*n1.*(m-1)+p+1,:));%求每一个面元X、Y、Z的平均值
       
       %将四个角点投影到面元平面上
       B2_tou(2*n1.*(m-1)+p  ,:)=B2(2*n1.*(m-1)+p  ,:)+N_B2_danwei((p+2*(m-1).*(n1-1)),:).*(Average_B2((p+2*(m-1).*(n1-1)),:)-B2(2*n1.*(m-1)+p  ,:));%位置1
       B2_tou(2*n1.* m   +p  ,:)=B2(2*n1.* m   +p  ,:)+N_B2_danwei((p+2*(m-1).*(n1-1)),:).*(Average_B2((p+2*(m-1).*(n1-1)),:)-B2(2*n1.* m   +p  ,:));%位置2
       B2_tou(2*n1.* m   +p+1,:)=B2(2*n1.* m   +p+1,:)+N_B2_danwei((p+2*(m-1).*(n1-1)),:).*(Average_B2((p+2*(m-1).*(n1-1)),:)-B2(2*n1.* m   +p+1,:));%位置3
       B2_tou(2*n1.*(m-1)+p+1,:)=B2(2*n1.*(m-1)+p+1,:)+N_B2_danwei((p+2*(m-1).*(n1-1)),:).*(Average_B2((p+2*(m-1).*(n1-1)),:)-B2(2*n1.*(m-1)+p+1,:));%位置4
       
       %建立面元坐标系:原点位于X_bar、Y_bar、Z_bar，x轴平行于t1,y轴平行于m，z轴平行于n
       T1_down_fanshu((p+2*(m-1).*(n1-1)),:)=norm(T1_down((p+2*(m-1).*(n1-1)),:));%求T1_down的范数
       T1_down_danwei((p+2*(m-1).*(n1-1)),:)=T1_down((p+2*(m-1).*(n1-1)),:)./T1_down_fanshu((p+2*(m-1).*(n1-1)),:);%求T1_down的单位向量t1
       m_danwei_down((p+2*(m-1).*(n1-1)),:)=cross(N_B2_danwei((p+2*(m-1).*(n1-1)),:),T1_down_danwei((p+2*(m-1).*(n1-1)),:));%求第三个单位向量m
       
       %把投影点从飞行器坐标系转换到面元坐标系
       %x
       B2_myx(2*n1.*(m-1)+p  ,1)=T1_down_danwei((p+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p  ,1)-Average_B2((p+2*(m-1).*(n1-1)),1))
                                +T1_down_danwei((p+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p  ,2)-Average_B2((p+2*(m-1).*(n1-1)),2))
                                +T1_down_danwei((p+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p  ,3)-Average_B2((p+2*(m-1).*(n1-1)),3));%位置1
       B2_myx(2*n1.* m   +p  ,1)=T1_down_danwei((p+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.* m   +p  ,1)-Average_B2((p+2*(m-1).*(n1-1)),1))
                                +T1_down_danwei((p+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.* m   +p  ,2)-Average_B2((p+2*(m-1).*(n1-1)),2))
                                +T1_down_danwei((p+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.* m   +p  ,3)-Average_B2((p+2*(m-1).*(n1-1)),3));%位置2
       B2_myx(2*n1.* m   +p+1,1)=T1_down_danwei((p+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.* m   +p+1,1)-Average_B2((p+2*(m-1).*(n1-1)),1))
                                +T1_down_danwei((p+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.* m   +p+1,2)-Average_B2((p+2*(m-1).*(n1-1)),2))
                                +T1_down_danwei((p+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.* m   +p+1,3)-Average_B2((p+2*(m-1).*(n1-1)),3));%位置3
       B2_myx(2*n1.*(m-1)+p+1,1)=T1_down_danwei((p+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p+1,1)-Average_B2((p+2*(m-1).*(n1-1)),1))
                                +T1_down_danwei((p+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p+1,2)-Average_B2((p+2*(m-1).*(n1-1)),2))
                                +T1_down_danwei((p+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p+1,3)-Average_B2((p+2*(m-1).*(n1-1)),3));%位置4
       %y
       B2_myx(2*n1.*(m-1)+p  ,2)= m_danwei_down((p+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p  ,1)-Average_B2((p+2*(m-1).*(n1-1)),1))
                                + m_danwei_down((p+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p  ,2)-Average_B2((p+2*(m-1).*(n1-1)),2))
                                + m_danwei_down((p+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p  ,3)-Average_B2((p+2*(m-1).*(n1-1)),3));%位置1
       B2_myx(2*n1.* m   +p  ,2)= m_danwei_down((p+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.* m   +p  ,1)-Average_B2((p+2*(m-1).*(n1-1)),1))
                                + m_danwei_down((p+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.* m   +p  ,2)-Average_B2((p+2*(m-1).*(n1-1)),2))
                                + m_danwei_down((p+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.* m   +p  ,3)-Average_B2((p+2*(m-1).*(n1-1)),3));%位置2
       B2_myx(2*n1.* m   +p+1,2)= m_danwei_down((p+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.* m   +p+1,1)-Average_B2((p+2*(m-1).*(n1-1)),1))
                                + m_danwei_down((p+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.* m   +p+1,2)-Average_B2((p+2*(m-1).*(n1-1)),2))
                                + m_danwei_down((p+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.* m   +p+1,3)-Average_B2((p+2*(m-1).*(n1-1)),3));%位置3
       B2_myx(2*n1.*(m-1)+p+1,2)= m_danwei_down((p+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p+1,1)-Average_B2((p+2*(m-1).*(n1-1)),1))
                                + m_danwei_down((p+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p+1,2)-Average_B2((p+2*(m-1).*(n1-1)),2))
                                + m_danwei_down((p+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p+1,3)-Average_B2((p+2*(m-1).*(n1-1)),3));%位置4
       %z
       B2_myx(2*n1.*(m-1)+p  ,3)=0;%位置1
       B2_myx(2*n1.* m   +p  ,3)=0;%位置2
       B2_myx(2*n1.* m   +p+1,3)=0;%位置3
       B2_myx(2*n1.*(m-1)+p+1,3)=0;%位置4
       
       %求面元的面积△A
       A_down((p+2*(m-1).*(n1-1)),:)=0.5.*(B2_myx(2*n1.*m+p+1,1)-B2_myx(2*n1.*(m-1)+p  ,1))
                                        .*(B2_myx(2*n1.*m+p  ,1)-B2_myx(2*n1.*(m-1)+p+1,1));
       %求面元质心的坐标
       ZhiXin_down((p+2*(m-1).*(n1-1)),1)=(1/3).*(1./( B2_myx(2*n1.* m   +p  ,2)-B2_myx(2*n1.*(m-1)+p+1,2)))
                                                .*(
                                                    +  B2_myx(2*n1.*(m-1)+p+1,1)
                                                    .*(B2_myx(2*n1.*(m-1)+p  ,2)-B2_myx(2*n1.* m   +p  ,2))
                                                    +  B2_myx(2*n1.* m   +p  ,1)
                                                    .*(B2_myx(2*n1.*(m-1)+p+1,2)-B2_myx(2*n1.*(m-1)+p  ,2))
                                                    );
       ZhiXin_down((p+2*(m-1).*(n1-1)),2)=(-1/3).*     B2_myx(2*n1.*(m-1)+p  ,2);
       ZhiXin_down((p+2*(m-1).*(n1-1)),3)=0;
       %质心在飞行器坐标系中的质心坐标
       Zhixin_down_fxqzbx((p+2*(m-1).*(n1-1)),1)=Average_B2((p+2*(m-1).*(n1-1)),1)
                                            +T1_down_danwei((p+2*(m-1).*(n1-1)),1).*ZhiXin_down((p+2*(m-1).*(n1-1)),1)
                                            + m_danwei_down((p+2*(m-1).*(n1-1)),1).*ZhiXin_down((p+2*(m-1).*(n1-1)),2);
       Zhixin_down_fxqzbx((p+2*(m-1).*(n1-1)),2)=Average_B2((p+2*(m-1).*(n1-1)),2)
                                            +T1_down_danwei((p+2*(m-1).*(n1-1)),2).*ZhiXin_down((p+2*(m-1).*(n1-1)),1)
                                            + m_danwei_down((p+2*(m-1).*(n1-1)),2).*ZhiXin_down((p+2*(m-1).*(n1-1)),2);
       Zhixin_down_fxqzbx((p+2*(m-1).*(n1-1)),3)=Average_B2((p+2*(m-1).*(n1-1)),3)
                                            +T1_down_danwei((p+2*(m-1).*(n1-1)),3).*ZhiXin_down((p+2*(m-1).*(n1-1)),1)
                                            + m_danwei_down((p+2*(m-1).*(n1-1)),3).*ZhiXin_down((p+2*(m-1).*(n1-1)),2);
       %撞击角
       zhuangjijiao_down((p+2*(m-1).*(n1-1)),:)=pi/2-acos((-(dot(N_B2_danwei((p+2*(m-1).*(n1-1)),:),V(1,:))))./(norm(V(1,:))));
       %代入工程估算
       if zhuangjijiao_down((p+2*(m-1).*(n1-1)),:)>=0
           Cp_down((p+2*(m-1).*(n1-1)),:)=Newton1(zhuangjijiao_down((p+2*(m-1).*(n1-1)),:),V(1,1),V(1,2),V(1,3),Ma);
       end
       if zhuangjijiao_down((p+2*(m-1).*(n1-1)),:)<0
           Cp_down((p+2*(m-1).*(n1-1)),:)=Qie2(zhuangjijiao_down((p+2*(m-1).*(n1-1)),:),V(1,1),V(1,2),V(1,3),Ma);
       end
       %求作用力
       F_down((p+2*(m-1).*(n1-1)),:)=A_down((p+2*(m-1).*(n1-1)),:).*(Cp_down((p+2*(m-1).*(n1-1)),:).*0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)+p_lailiu);
       %轴向力系数
       CA_down((p+2*(m-1).*(n1-1)),:)=F_down((p+2*(m-1).*(n1-1)),:).*N_B1_danwei((p+2*(m-1).*(n1-1)),1)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %法向力系数
       CN_down((p+2*(m-1).*(n1-1)),:)=F_down((p+2*(m-1).*(n1-1)),:).*N_B1_danwei((p+2*(m-1).*(n1-1)),3)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %横向力系数
       CZ_down((p+2*(m-1).*(n1-1)),:)=F_down((p+2*(m-1).*(n1-1)),:).*N_B1_danwei((p+2*(m-1).*(n1-1)),2)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %升力系数
       Cl_down((p+2*(m-1).*(n1-1)),:)=CN_down((p+2*(m-1).*(n1-1)),:).*cos(AttackAngle)-CA_down((p+2*(m-1).*(n1-1)),:).*sin(AttackAngle);
       %阻力系数
       Cd_down((p+2*(m-1).*(n1-1)),:)=CN_down((p+2*(m-1).*(n1-1)),:).*sin(AttackAngle)+CA_down((p+2*(m-1).*(n1-1)),:).*cos(AttackAngle);
       
   end
   %%%%%%%%%%%%%%%%%%%%一锥结束%%%%%%%%%%%%%%%%%%%% 
   
   %%%%%%%%%%%%%%%%%%%%二锥%%%%%%%%%%%%%%%%%%%%
 for p=(n1+1):(2*n1-1)
       T1_down((p-1+2*(m-1).*(n1-1)),:)=
            +B2(2*n1.* m   +p+1,:)
            -B2(2*n1.*(m-1)+p  ,:);
       T2_down((p-1+2*(m-1).*(n1-1)),:)=
            +B2(2*n1.*(m-1)+p+1,:)
            -B2(2*n1.* m   +p  ,:);
       N_B2((p-1+2*(m-1).*(n1-1)),:)=cross(
           T2_down((p-1+2*(m-1).*(n1-1)),:),
           T1_down((p-1+2*(m-1).*(n1-1)),:));
       
       N_B2_fanshu((p-1+2*(m-1).*(n1-1)),:)=norm(N_B2((p-1+2*(m-1).*(n1-1)),:));%求范数
       N_B2_danwei((p-1+2*(m-1).*(n1-1)),:)=-(N_B2((p-1+2*(m-1).*(n1-1)),:))./(N_B2_fanshu((p-1+2*(m-1).*(n1-1)),:));%求单位向量n
       
       Average_B2((p-1+2*(m-1).*(n1-1)),:)=0.25.*(
           +B2(2*n1.*(m-1)+p  ,:)
           +B2(2*n1.* m   +p  ,:)
           +B2(2*n1.* m   +p+1,:)
           +B2(2*n1.*(m-1)+p+1,:));%求每一个面元X、Y、Z的平均值
       
       %将四个角点投影到面元平面上
       B2_tou(2*n1.*(m-1)+p  ,:)=B2(2*n1.*(m-1)+p  ,:)+N_B2_danwei((p-1+2*(m-1).*(n1-1)),:).*(Average_B2((p-1+2*(m-1).*(n1-1)),:)-B2(2*n1.*(m-1)+p  ,:));%位置1
       B2_tou(2*n1.* m   +p  ,:)=B2(2*n1.* m   +p  ,:)+N_B2_danwei((p-1+2*(m-1).*(n1-1)),:).*(Average_B2((p-1+2*(m-1).*(n1-1)),:)-B2(2*n1.* m   +p  ,:));%位置2
       B2_tou(2*n1.* m   +p+1,:)=B2(2*n1.* m   +p+1,:)+N_B2_danwei((p-1+2*(m-1).*(n1-1)),:).*(Average_B2((p-1+2*(m-1).*(n1-1)),:)-B2(2*n1.* m   +p+1,:));%位置3
       B2_tou(2*n1.*(m-1)+p+1,:)=B2(2*n1.*(m-1)+p+1,:)+N_B2_danwei((p-1+2*(m-1).*(n1-1)),:).*(Average_B2((p-1+2*(m-1).*(n1-1)),:)-B2(2*n1.*(m-1)+p+1,:));%位置4
       
       %建立面元坐标系:原点位于X_bar、Y_bar、Z_bar，x轴平行于t1_down,y轴平行于m，z轴平行于n
       T1_down_fanshu((p-1+2*(m-1).*(n1-1)),:)=norm(     T1_down((p-1+2*(m-1).*(n1-1)),:));%求T1_down的范数
       T1_down_danwei((p-1+2*(m-1).*(n1-1)),:)=          T1_down((p-1+2*(m-1).*(n1-1)),:)
                                                ./T1_down_fanshu((p-1+2*(m-1).*(n1-1)),:);%求T1_down的单位向量t1_down
       m_danwei_down ((p-1+2*(m-1).*(n1-1)),:)=cross(N_B2_danwei((p-1+2*(m-1).*(n1-1)),:),
                                                  T1_down_danwei((p-1+2*(m-1).*(n1-1)),:));%求第三个单位向量m
       
       %把投影点从飞行器坐标系转换到面元坐标系
       %x
       B2_myx(2*n1.*(m-1)+p  ,1)=T1_down_danwei((p-1+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p  ,1)-Average_B2((p-1+2*(m-1).*(n1-1)),1))
                                +T1_down_danwei((p-1+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p  ,2)-Average_B2((p-1+2*(m-1).*(n1-1)),2))
                                +T1_down_danwei((p-1+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p  ,3)-Average_B2((p-1+2*(m-1).*(n1-1)),3));%位置1
       B2_myx(2*n1.* m   +p  ,1)=T1_down_danwei((p-1+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p  ,1)-Average_B2((p-1+2*(m-1).*(n1-1)),1))
                                +T1_down_danwei((p-1+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p  ,2)-Average_B2((p-1+2*(m-1).*(n1-1)),2))
                                +T1_down_danwei((p-1+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p  ,3)-Average_B2((p-1+2*(m-1).*(n1-1)),3));%位置2
       B2_myx(2*n1.* m   +p+1,1)=T1_down_danwei((p-1+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.* m   +p+1,1)-Average_B2((p-1+2*(m-1).*(n1-1)),1))
                                +T1_down_danwei((p-1+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.* m   +p+1,2)-Average_B2((p-1+2*(m-1).*(n1-1)),2))
                                +T1_down_danwei((p-1+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.* m   +p+1,3)-Average_B2((p-1+2*(m-1).*(n1-1)),3));%位置3
       B2_myx(2*n1.*(m-1)+p+1,1)=T1_down_danwei((p-1+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p+1,1)-Average_B2((p-1+2*(m-1).*(n1-1)),1))
                                +T1_down_danwei((p-1+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p+1,2)-Average_B2((p-1+2*(m-1).*(n1-1)),2))
                                +T1_down_danwei((p-1+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p+1,3)-Average_B2((p-1+2*(m-1).*(n1-1)),3));%位置4
       %y
       B2_myx(2*n1.*(m-1)+p  ,2)= m_danwei_down((p-1+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p  ,1)-Average_B2((p-1+2*(m-1).*(n1-1)),1))
                                 +m_danwei_down((p-1+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p  ,2)-Average_B2((p-1+2*(m-1).*(n1-1)),2))
                                 +m_danwei_down((p-1+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p  ,3)-Average_B2((p-1+2*(m-1).*(n1-1)),3));%位置1
       B2_myx(2*n1.* m   +p  ,2)= m_danwei_down((p-1+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p  ,1)-Average_B2((p-1+2*(m-1).*(n1-1)),1))
                                 +m_danwei_down((p-1+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p  ,2)-Average_B2((p-1+2*(m-1).*(n1-1)),2))
                                 +m_danwei_down((p-1+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p  ,3)-Average_B2((p-1+2*(m-1).*(n1-1)),3));%位置2
       B2_myx(2*n1.* m   +p+1,2)= m_danwei_down((p-1+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.* m   +p+1,1)-Average_B2((p-1+2*(m-1).*(n1-1)),1))
                                 +m_danwei_down((p-1+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.* m   +p+1,2)-Average_B2((p-1+2*(m-1).*(n1-1)),2))
                                 +m_danwei_down((p-1+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.* m   +p+1,3)-Average_B2((p-1+2*(m-1).*(n1-1)),3));%位置3
       B2_myx(2*n1.*(m-1)+p+1,2)= m_danwei_down((p-1+2*(m-1).*(n1-1)),1).*(B2_tou(2*n1.*(m-1)+p+1,1)-Average_B2((p-1+2*(m-1).*(n1-1)),1))
                                 +m_danwei_down((p-1+2*(m-1).*(n1-1)),2).*(B2_tou(2*n1.*(m-1)+p+1,2)-Average_B2((p-1+2*(m-1).*(n1-1)),2))
                                 +m_danwei_down((p-1+2*(m-1).*(n1-1)),3).*(B2_tou(2*n1.*(m-1)+p+1,3)-Average_B2((p-1+2*(m-1).*(n1-1)),3));%位置4
       %z
       B2_myx(2*n1.*(m-1)+p,3)=0;%位置1
       B2_myx(2*n1.*m+p,3)=0;%位置2
       B2_myx(2*n1.*m+p+1,3)=0;%位置3
       B2_myx(2*n1.*(m-1)+p+1,3)=0;%位置4
       %求面元的面积△A
       A_down((p-1+2*(m-1).*(n1-1)),:)=0.5.*(B2_myx(2*n1.* m   +p+1,1)-B2_myx(2*n1.*(m-1)+p  ,1))
                                          .*(B2_myx(2*n1.* m   +p  ,1)-B2_myx(2*n1.*(m-1)+p+1,1));
       %求面元质心的坐标
       ZhiXin_down((p-1+2*(m-1).*(n1-1)),1)=(1/3).*(1./(B2_myx(2*n1.* m   +p  ,2)-B2_myx(2*n1.*(m-1)+p+1,2))).*(

                                                     +  B2_myx(2*n1.*(m-1)+p+1,1)
                                                     .*(B2_myx(2*n1.*(m-1)+p  ,2)-B2_myx(2*n1.* m   +p  ,2))
                                                     +  B2_myx(2*n1.* m   +p  ,1)
                                                     .*(B2_myx(2*n1.*(m-1)+p+1,2)-B2_myx(2*n1.*(m-1)+p  ,2))); 
       ZhiXin_down((p-1+2*(m-1).*(n1-1)),2)=-(1/3).*B2_myx(2*n1.*(m-1)+p,2);
       ZhiXin_down((p-1+2*(m-1).*(n1-1)),2)=0;
       %质心在飞行器坐标系中的质心坐标
       Zhixin_down_fxqzbx((p-1+2*(m-1).*(n1-1)),1)=Average_B2((p-1+2*(m-1).*(n1-1)),1)
                                              +T1_down_danwei((p-1+2*(m-1).*(n1-1)),1).*ZhiXin_down((p-1+2*(m-1).*(n1-1)),1)
                                              + m_danwei_down((p-1+2*(m-1).*(n1-1)),1).*ZhiXin_down((p-1+2*(m-1).*(n1-1)),2);
       Zhixin_down_fxqzbx((p-1+2*(m-1).*(n1-1)),2)=Average_B2((p-1+2*(m-1).*(n1-1)),2)
                                              +T1_down_danwei((p-1+2*(m-1).*(n1-1)),2).*ZhiXin_down((p-1+2*(m-1).*(n1-1)),1)
                                              + m_danwei_down((p-1+2*(m-1).*(n1-1)),2).*ZhiXin_down((p-1+2*(m-1).*(n1-1)),2);
       Zhixin_down_fxqzbx((p-1+2*(m-1).*(n1-1)),3)=Average_B2((p-1+2*(m-1).*(n1-1)),3)
                                              +T1_down_danwei((p-1+2*(m-1).*(n1-1)),3).*ZhiXin_down((p-1+2*(m-1).*(n1-1)),1)
                                              + m_danwei_down((p-1+2*(m-1).*(n1-1)),3).*ZhiXin_down((p-1+2*(m-1).*(n1-1)),2);
       %撞击角
       zhuangjijiao_down((p-1+2*(m-1).*(n1-1)),:)=pi/2-acos((-(dot(N_B2_danwei((p-1+2*(m-1).*(n1-1)),:),V(1,:))))./(norm(V(1,:))));
       %代入工程估算
       if zhuangjijiao_down((p-1+2*(m-1).*(n1-1)),:)>=0
           Cp_down((p-1+2*(m-1).*(n1-1)),:)=Newton1(zhuangjijiao_down((p-1+2*(m-1).*(n1-1)),:),V(1,1),V(1,2),V(1,3),Ma);
       end
       if zhuangjijiao_down((p-1+2*(m-1).*(n1-1)),:)<0
           Cp_down((p-1+2*(m-1).*(n1-1)),:)=Newton1(zhuangjijiao_down((p-1+2*(m-1).*(n1-1)),:),V(1,1),V(1,2),V(1,3),Ma);
       end
       %求作用力
       F_down((p-1+2*(m-1).*(n1-1)),:)=A_down((p-1+2*(m-1).*(n1-1)),:).*(Cp_down((p-1+2*(m-1).*(n1-1)),:).*0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)+p_lailiu);
       %轴向力系数
       CA_down((p-1+2*(m-1).*(n1-1)),:)=F_down((p-1+2*(m-1).*(n1-1)),:).*N_B1_danwei((p-1+2*(m-1).*(n1-1)),1)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %法向力系数
       CN_down((p-1+2*(m-1).*(n1-1)),:)=F_down((p-1+2*(m-1).*(n1-1)),:).*N_B1_danwei((p-1+2*(m-1).*(n1-1)),3)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %横向力系数
       CZ_down((p-1+2*(m-1).*(n1-1)),:)=F_down((p-1+2*(m-1).*(n1-1)),:).*N_B1_danwei((p-1+2*(m-1).*(n1-1)),2)./(0.5.*midu.*(V(1,1)^2+V(1,2)^2+V(1,3)^2)*S_can);
       %升力系数
       Cl_down((p-1+2*(m-1).*(n1-1)),:)=CN_down((p-1+2*(m-1).*(n1-1)),:).*cos(AttackAngle)-CA_down((p-1+2*(m-1).*(n1-1)),:).*sin(AttackAngle);
       %阻力系数
       Cd_down((p-1+2*(m-1).*(n1-1)),:)=CN_down((p-1+2*(m-1).*(n1-1)),:).*sin(AttackAngle)+CA_down((p-1+2*(m-1).*(n1-1)),:).*cos(AttackAngle);
       
       
   end
   %%%%%%%%%%%%%%%%%%%%二锥结束%%%%%%%%%%%%%%%%%%%%
   
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%End-下表面%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%求力矩系数%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%轴向力系数
CA=sum(CA_up(:))+sum(CA_down(:));
%法向力系数
CN=sum(CN_up(:))+sum(CN_down(:));
%横向力系数
CZ=sum(CZ_up(:))+sum(CZ_down(:));
%升力系数
Cl=sum(Cl_up(:))+sum(Cl_down(:));
%阻力系数
Cd=sum(Cd_up(:))+sum(Cd_down(:));
%升阻比
K=Cl/Cd;
%俯仰力矩系数
Gusuan(1)=CA;
Gusuan(2)=CN;
Gusuan(3)=CZ;
Gusuan(4)=Cl;
Gusuan(5)=Cd;
Gusuan(6)=K;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%End-力矩系数%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%气动力工程估算方法%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 修正牛顿法-ACM-1-文献19
function [Cp]=Newton1(zhuangjijiao,Vx,Vy,Vz,Ma)
if zhuangjijiao>=0
    r=1.4;
    K=2./(r.*Ma.*Ma).*(
                        ((r+1)^2.*Ma^2./(4.*r.*Ma^2-2.*(r-1)))
                            .^(r./(r-1))
                        
                        .*((1-r+2.*r.*Ma^2)./(r+1))
                        
                    
                        -1
                        
                        );
    Cp=K.*(sin(zhuangjijiao)^2);
end
if zhuangjijiao<0
   Cp=0;     
end
end
% 修正牛顿法-ACM-2-文献19
function [Cp]=Newton2(zhuangjijiao,Vx,Vy,Vz,Ma)
if zhuangjijiao>=0
    r=1.4;
    K=(2*(r+1)*(r+7))/((r+3)^2);
    Cp=K.*(sin(zhuangjijiao)^2);
end
if zhuangjijiao<0
   Cp=0;     
end
end
%切楔/切锥法1-文献4
function [Cp]=Qie1(zhuangjijiao,Vx,Vy,Vz,Ma)
yita=sin(zhuangjijiao).*log(sqrt(Ma^2-1));
e=0.18145
    -0.20923. *yita
    +0.09092. *(yita^2)
    +0.006876.*(yita^3)
    -0.006225.*(yita^4)
    -0.000971.*(yita^5);
Cp=2.*exp(e).*(sin(zhuangjijiao))^2;
end
%切楔/切锥法1-文献5
function [Cp]=Qie2(zhuangjijiao,Vx,Vy,Vz,Ma)
Cp=(4.*(sin(zhuangjijiao)^2)
    .*(2.5+8*sin(zhuangjijiao).*(sqrt(Ma^2-1))))
        ./(1+16.*sin(zhuangjijiao).*(sqrt(Ma^2-1)));
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%End---气动力工程估算方法%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%









    