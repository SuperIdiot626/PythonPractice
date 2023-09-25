clc,clear;
format long
%导入翼型和冰型数据
airfoil = load('Tail.dat'); %翼型数据
ice = load('3.dat');          %冰形数据

airfoilx=airfoil(:,1);
airfoily=airfoil(:,2);
icex=ice(:,1);
icey=ice(:,2);

plot(airfoilx,airfoily,'k');
axis equal;
hold on;

k = find(airfoilx==min(min(airfoilx)));%确定驻点位置
StagnationPoint=[min(airfoilx),airfoily(k)];%确定驻点坐标
plot(ice(:,1),ice(:,2),'r');

%%绘制内切圆
%绘制圆心

r=0.01;
plot(r,0,'ro');
CircleCenter=[r,0]; %确定圆心
r_vector=StagnationPoint-[r,0];
r=norm(r_vector);

alpha=0:pi/40:2*pi;
x=r*cos(alpha)+r;
y=r*sin(alpha);
plot(x,y,'-');
n=length(icex);
sUp=zeros(1,length(icex));
sDown=zeros(1,length(icex));
for i=1:n
    if icey(i)>0&&icex(i)<1*r
        sUp(i)= (icex(i)-r)^2+icey(i)^2;
    end
    if icey(i)<=-0&&icex(i)<1.2*r
        sDown(i)= (icex(i)-r)^2+icey(i)^2;
    end
end
[pksUp,idUp]=max(sUp);
[pksDown,idDown]=max(sDown);
% fprintf("idUp=%d",idUp);
% fprintf("idDown=%d",idDown);

IceStagnationPointUp=[icex(idUp),icey(idUp)];%上冰形峰值点坐标
IceStagnationPointDown=[icex(idDown),icey(idDown)];%下冰形峰值点坐标
plot(icex(idUp),icey(idUp),'ro');
plot(icex(idDown),icey(idDown),'ro');
    
IceLineUp=CircleCenter-[icex(idUp),icey(idUp)];%峰值点与圆心连线
IceLineDown=CircleCenter-[icex(idDown),icey(idDown)];%峰值点与圆心连线
[iceAngleUp,IceHeightUp]=cart2pol(IceLineUp(1),IceLineUp(2));%计算冰高冰角
[iceAngleDown,IceHeightDown]=cart2pol(IceLineDown(1),IceLineDown(2));%计算冰高冰角
IceAngleUp=abs(iceAngleUp*180/pi);
IceAngleDown=abs(iceAngleDown*180/pi);
plot([CircleCenter(1),IceStagnationPointUp(1)],[CircleCenter(2),IceStagnationPointUp(2)]);
plot([CircleCenter(1),IceStagnationPointDown(1)],[CircleCenter(2),IceStagnationPointDown(2)]);
IceAngle = IceAngleUp + IceAngleDown;
fprintf("IceAngle=%d",IceAngle);
fprintf("IceAngleUp=%d",IceAngleUp);
fprintf("IceAngleDown=%d",IceAngleDown);
% %判断冰型
% CircleCenter=[0.01,0]; %确定圆心
% [pks,id]=findpeaks(-icex);%确定冰形峰值和位置
% if length(pks)==1 %霜冰
%     IceStagnationPoint=[-pks,icey(id)];%冰形峰值点坐标
%     plot(-pks,icey(id),'ro');
%     
%     IceLine=CircleCenter-[-pks,icey(id)];%峰值点与圆心连线
%     [iceAngle,IceHeight]=cart2pol(IceLine(1),IceLine(2));%计算冰高冰角
%     IceAngle=abs(iceAngle*180/pi);
%     plot([CircleCenter(1),IceStagnationPoint(1)],[CircleCenter(2),IceStagnationPoint(2)]);
% %     IceHeight=norm([-pks,icey(id)]-CircleCenter);
% %     IceAngle=
% 
% else  %明冰
%     n=length(pks);%确定冰角个数
%     for i=1:n
%         IceStagnationPoint=[-pks(i),icey(id(i))];%冰形峰值点坐标
%         plot(-pks(i),icey(id(i)),'ro');
%         IceLine=CircleCenter-[-pks(i),icey(id(i))];%峰值点与圆心连线
%         [iceAngle,iceHeight]=cart2pol(IceLine(1),IceLine(2));%计算冰高冰角
%         IceHeight(i)=iceHeight;
%         IceAngle(i)=abs(iceAngle*180/pi);
%         plot([CircleCenter(1),IceStagnationPoint(1)],[CircleCenter(2),IceStagnationPoint(2)]);
%     end
% end
  
        
    
    
    
    