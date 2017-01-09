%program3
%Filtering in frequency domain
%Implement the ideal, Butterworth and Gaussian lowpass and
%highpass filters and test them under different parameters using
%characters_test_pattern.tif.

clc;
clear all;
close all;
%读取图像 
I = imread('characters_test_pattern.tif');

figure;subplot(2,4,1);imshow(I);
%转换到频域
f1=fft2(I);
f2=fftshift(f1);
[h , w] = size(f2);

%理想滤波器(低通)
result_lxdt = f2;
for i = 1:h
    for j = 1:w
        if( (h/2-i) * (h/2-i) + (w/2-j) * (w/2-j) >= 40)
            result_lxdt(i,j) = 0;
        end
    end
end
result_lxdt2=ifftshift(result_lxdt);%转回空域
result1=ifft2(result_lxdt2);
result1=abs(result1);  
result1=result1/256;  
subplot(2,4,2);imshow(result1);

%理想滤波器(高通)
result_lxgt = f2;
for i = 1:h
    for j = 1:w
        if( (h/2-i) * (h/2-i) + (w/2-j) * (w/2-j) <= 40)
            result_lxgt(i,j) = 0;
        end
    end
end
result_lxgt2=ifftshift(result_lxgt);%转回空域
result2=ifft2(result_lxgt2);
result2=abs(result2);  
result2=result2/256;  
subplot(2,4,3);imshow(result2);
%================================================================
%butterworth滤波器(低通)
n = 2;
result_bwdt = f2;
for i = 1:h
    for j = 1:w
        d = sqrt((h/2-i) * (h/2-i) + (w/2-j) * (w/2-j));
        h1 = 1/(1+(d/40)^(2*n));
        result_bwdt(i,j) = f2(i,j) * h1;
    end
end
result_bwdt2=ifftshift(result_bwdt);%转回空域
result3=ifft2(result_bwdt2);
result3=abs(result3);  
result3=result3/256;  
subplot(2,4,5);imshow(result3);

%butterworth滤波器(高通)
n=2;
result_bwgt = f2;
for i = 1:h
    for j = 1:w
       d = sqrt((h/2-i) * (h/2-i) + (w/2-j) * (w/2-j));
       h2 = 1/(1+(d/40)^(2*n));
       result_bwgt(i,j) = f2(i,j) * ( 1 - h2);
    end
end
result_bwgt2=ifftshift(result_bwgt);%转回空域
result4=ifft2(result_bwgt2);
result4=abs(result4);  
result4=result4/256;  
subplot(2,4,6);imshow(result4);
%================================================================
%高斯滤波器(低通)
n = 2;
result_gsdt = f2;
for i = 1:h
    for j = 1:w
        d2 = (h/2-i) * (h/2-i) + (w/2-j) * (w/2-j);
        h3 = exp(-d2/(2*40));
        result_gsdt(i,j) = f2(i,j) * h3;
    end
end
result_gsdt2=ifftshift(result_gsdt);%转回空域
result5=ifft2(result_gsdt2);
result5=abs(result5);  
result5=result5/256;  
subplot(2,4,7);imshow(result5);

%高斯滤波器(高通)
n=2;
result_gsgt = f2;
for i = 1:h
    for j = 1:w
       d2 = (h/2-i) * (h/2-i) + (w/2-j) * (w/2-j);
       h4 = exp(-d2/(2*40));
       result_gsgt(i,j) = f2(i,j) * ( 1 - h4);
    end
end
result_gsgt2=ifftshift(result_gsgt);%转回空域
result6=ifft2(result_gsgt2);
result6=abs(result6);  
result6=result6/256;  
subplot(2,4,8);imshow(result6);