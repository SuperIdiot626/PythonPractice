clc;clear;
format long;
LWCrange=xlsread('LWCrange.xlsx');
[CaseNum,StepNum]=size(LWCrange);

% % single case LWC range
for i=1:CaseNum
    Case = LWCrange(i,:);
    plot([1:StepNum],Case);
    hold on;
end
LWCmax = 1.1e-3;
LWCmin = 0.9e-3;
plot([1,StepNum],[LWCmax,LWCmax],'--')
plot([1,StepNum],[LWCmin,LWCmin],'--')

% % all case LWC range
% num = 1:CaseNum*StepNum;
% for i=1:CaseNum
%     for j=1:StepNum
%         id = (i-1)*j+j;
%        plot(num(id),LWCrange(i,j),'ro');
%        fprintf('LWC=%f',LWCrange(i,j));
%        hold on;
%     end
% end
% 
% LWCmax = 1.1e-3;
% LWCmin = 0.9e-3;
% plot([1,CaseNum*StepNum],[LWCmax,LWCmax],'--')
% plot([1,CaseNum*StepNum],[LWCmin,LWCmin],'--')