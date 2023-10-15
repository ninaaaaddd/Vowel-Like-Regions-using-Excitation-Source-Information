clc;
clear all;
close all;

[d,fs]=audioread('merged/10115.wav');%%115
d=d(:,1);
d=resample(d,8000,fs);
fs=8000;
d=d-mean(d);
d=d./max(abs(d));


t1=(1:1:length(d))./fs;

% figure(1);
% plot(t1,d)

fs=8000;
Speech_Rate = 1;


% For vowel onset point
[G,Gd]= gausswin((800/Speech_Rate)+1,(133/Speech_Rate)+1);

res1= LPres(d,fs,20,10,10,1);
hensp1=HilbertEnv(res1,fs,0);
he2=abs(hensp1);
he1=he2/max(abs(he2));

winlength=6;
THexivlrop=.06; % original

%%%%---------------------------------- %%From HE of LP residual
[EVIvlrop_he1]= vlropHEoflpresidual_v1(he1,fs,Gd,Speech_Rate);

%%%%------------------------------ %%From zerofrequency filtered output
[ EVIvlrop_zf1,zffo, gclocssp1]= vlropZerofrequency_v1(d,winlength,fs,Gd,Speech_Rate);

%%%%------------------------%% From Excitation source information
[EVIvlrop1,vlrop1,total_vlrop1,PP1]=...
    vlropExcitationsource_v1(d,EVIvlrop_he1,EVIvlrop_zf1,0, 0, 0, 0, THexivlrop,0);



% For Vowel offset point
flipped_Gd = fliplr(Gd);

res1= LPres(d,fs,20,10,10,1);
hensp1=HilbertEnv(res1,fs,0);
he2=abs(hensp1);
he1=he2/max(abs(he2));

winlength=6;
THexivlrop=.06; % original

%%%%---------------------------------- %%From HE of LP residual
[EVIvlrop_he2]= vlropHEoflpresidual_v1(he1,fs,flipped_Gd,Speech_Rate);

%%%%------------------------------ %%From zerofrequency filtered output
[ EVIvlrop_zf2,zffo2, gclocssp2]= vlropZerofrequency_v1(d,winlength,fs,flipped_Gd,Speech_Rate);

%%%%------------------------%% From Excitation source information
[EVIvlrop2,vlrop2,total_vlrop2,PP2]=...
    vlropExcitationsource_v1(d,EVIvlrop_he2,EVIvlrop_zf2,0, 0, 0, 0, THexivlrop,0);

time_n1 = 1/fs;
time_n2 = length(d)/fs;

t1= t1(time_n1*fs:time_n2*fs);
t1 = (1:length(t1))./fs;

d1 = d(time_n1*fs:time_n2*fs);

EVIvlrop1 = EVIvlrop1(time_n1*fs:time_n2*fs);
PP1 = PP1(time_n1*fs:time_n2*fs);
EVIvlrop2 = EVIvlrop2(time_n1*fs:time_n2*fs);
PP2 = PP2(time_n1*fs:time_n2*fs);

figure(1);
b(1) = subplot(221);
plot(t1,d1,'k');
hold on;
% plot(t1,-stgrlabel1,'k');
% hold on;
plot(t1,PP1);
b(2) = subplot(222);
plot(t1,EVIvlrop1);
hold on;
plot(t1,PP1);

b(3) = subplot(223);
plot(t1,d1,'k');
hold on;
% plot(t1,-stgrlabel1,'k');
% hold on;
plot(t1,PP2);
b(4) = subplot(224);
plot(t1,EVIvlrop2);
hold on;
plot(t1,PP2);







