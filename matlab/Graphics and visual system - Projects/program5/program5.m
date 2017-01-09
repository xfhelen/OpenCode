%program5
% Image restoration (Test image: book_cover.jpg)
% Suppose a blurring degradation function as
% 
% (a) Implement a blurring filter using Eq. (1).
% (b) Blur the test image book_cover.jpg using parameters
% a=b=0.1 and T = 1.
% (c) Add Gaussian noise of 0 mean and variance of 650 to the
% blurred image.
% (d) Restore the blurred image and the blurred noisy image using
% the inverse filter, Wiener deconvolution filter, respectively.
% (e) Add Gaussian noise of 0 and different variances to the blurred
% image and repeat (d), investigate the performance of the Wiener
% deconvolution filter

clc;
clear all;
close all;
%读取图像 
I = imread('book_cover.jpg');
figure;subplot(2,4,1);imshow(I);

%转换到频域
f1=fft2(I);
f2=fftshift(f1);
[h , w] = size(f2);

%根据模糊方程模糊图像
T = 1;
a = 0.1;
b = 0.1;
result_blur = f2;
H =zeros(h,w);
H1=zeros(h,w);
for i=1:h;
    for j=1:w
        s=pi*((i-h/2-1)*a+(j-w/2-1)*b);
        if s==0
            H(i,j)=1;
        else
            H(i,j)=(T*sin(s)*exp(-sqrt(-1)*s))/s;
        end
        if (abs(sin(s))<0.01)
            H1(i,j)=1;
        else
            H1(i,j)=1/H(i,j);
        end
    end
end
result_blur = result_blur.* H;
result_blur2=ifftshift(result_blur);%转回空域
result1=ifft2(result_blur2);
result1=abs(result1);  
result1 = result1/256;
subplot(2,4,2);imshow(result1);

%增加高斯噪声 mean = 0  变异数650
a = 0;
b = 10;
y=randn(1,h*w); 
y=y/std(y); 
y=y-mean(y); 
y2 = reshape(y,h,w);
n_gaussian = 0.0004*(a + b .* y2-0.5);
result2 = double(result1) +double(n_gaussian);
subplot(2,4,3);imshow(result2);

%逆滤波器
temp_ydgs=fft2(result2);%转换到频域
temp_ydgs=fftshift(temp_ydgs);
[h , w] = size(temp_ydgs);
T = 1;
a = 0.1;
b = 0.1;
H1=zeros(h,w);
for i=1:h;
    for j=1:w
        s=pi*((i-h/2-1)*a+(j-w/2-1)*b);
        if (abs(sin(s))<0.01)
            H1(i,j)=1;
        else
            H1(i,j)=s/(T*sin(s)*exp(-sqrt(-1)*s));
        end
    end
end
result_ni = temp_ydgs.* H1;
result_ni2=ifftshift(result_ni);%转回空域
result3=ifft2(result_ni2);
result3=abs(result3);  
result3 = result3/256;
subplot(2,4,4);imshow(result3);

%维纳滤波器
temp_gs=fft2(result2-result1);%转换到频域
temp_gs=fftshift(temp_gs);
[h , w] = size(temp_gs);
W = conj(H)./abs(H.*conj(H)+(temp_gs.*conj(temp_gs))./((f2/256).*conj(f2/256)));
result_wn = W.*temp_ydgs;
result_wn2=ifftshift(result_wn);%转回空域
result4=ifft2(result_wn2);
result4=abs(result4);  
subplot(2,4,5);imshow(result4);


%增加高斯噪声 mean = 0 变异数改变，重复上述过程。




