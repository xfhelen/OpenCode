%program1
% Histogram Equalization
%(a) Write a computer program for computing the histogram of an image.
%(b) Implement the histogram equalization technique.
%(c) Your program must be general to allow any gray-level image as its input.

clc;
clear all;
close all;
%读取图像  
I = imread('Fig2.jpg');  
[ h , w ] = size(I);  
%显示原始图像
figure;subplot(2,2,1);imshow(I);
  
%原始图像各个灰度值对应的像素的数量的多少  
gray256 = zeros(256,1);
for i = 1:h  
    for j = 1: w  
        gray256(I(i,j) + 1) = gray256(I(i,j) + 1) + 1;
    end  
end  

%原始图像各个灰度值对应像素数量占总体像素的比例  
gray256_Prop = zeros(1,256);  
x = zeros(256,1);
pixel = h * w * 1.0;
for i = 1:256  
    gray256_Prop(i) = gray256(i) / pixel;  
    x(i) = i;%直方图横坐标
end  

%画原始图像直方图
subplot(2,2,2); bar(gray256,0.01);

%计算灰度映射函数
for i = 2:256  
    gray256_Prop(i) = gray256_Prop(i-1) + gray256_Prop(i);  
end  
gray256_Prop = 256 * gray256_Prop;
 
%对灰度值进行映射（均衡化）  
result = I;
for i = 1:h  
    for j = 1: w  
        result(i,j) = gray256_Prop(I(i,j) + 1);  
    end  
end  
 
%画结果图像
subplot(2,2,3);imshow(result);

%结果图像各个灰度值对应的像素的数量的多少  
gray256_result = zeros(256,1);
for i = 1:h  
    for j = 1: w  
        gray256_result(floor(result(i,j)) + 1) = gray256_result(floor(result(i,j)) + 1) + 1;
    end  
end  

%结果图像各个灰度值对应像素数量占总体像素的比例  
gray256_Prop_result = zeros(1,256);  
for i = 1:256  
    gray256_Prop_result(i) = gray256_result(i) / pixel;  
end  

%画结果图像直方图
subplot(2,2,4); bar(gray256_result,0.01);



