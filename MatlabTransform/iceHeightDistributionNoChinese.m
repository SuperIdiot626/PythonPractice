clc,clear;
format long
iceheight = load('iceHeight(n=15).dat');
averageHeight = mean(iceheight)
variance = var(iceheight)

[f,xi]=ksdensity(iceheight);
plot(xi,f);
title('n=15')