clc,clear;
format long
iceheight = load('iceHeight(n=15).dat');
averageHeight = mean(iceheight)%均值
variance = var(iceheight)%方差

[f,xi]=ksdensity(iceheight);
plot(xi,f);
title('n=15')