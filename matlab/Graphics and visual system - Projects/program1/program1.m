%program1
% Histogram Equalization
%(a) Write a computer program for computing the histogram of an image.
%(b) Implement the histogram equalization technique.
%(c) Your program must be general to allow any gray-level image as its input.

clc;
clear all;
close all;
%��ȡͼ��  
I = imread('Fig2.jpg');  
[ h , w ] = size(I);  
%��ʾԭʼͼ��
figure;subplot(2,2,1);imshow(I);
  
%ԭʼͼ������Ҷ�ֵ��Ӧ�����ص������Ķ���  
gray256 = zeros(256,1);
for i = 1:h  
    for j = 1: w  
        gray256(I(i,j) + 1) = gray256(I(i,j) + 1) + 1;
    end  
end  

%ԭʼͼ������Ҷ�ֵ��Ӧ��������ռ�������صı���  
gray256_Prop = zeros(1,256);  
x = zeros(256,1);
pixel = h * w * 1.0;
for i = 1:256  
    gray256_Prop(i) = gray256(i) / pixel;  
    x(i) = i;%ֱ��ͼ������
end  

%��ԭʼͼ��ֱ��ͼ
subplot(2,2,2); bar(gray256,0.01);

%����Ҷ�ӳ�亯��
for i = 2:256  
    gray256_Prop(i) = gray256_Prop(i-1) + gray256_Prop(i);  
end  
gray256_Prop = 256 * gray256_Prop;
 
%�ԻҶ�ֵ����ӳ�䣨���⻯��  
result = I;
for i = 1:h  
    for j = 1: w  
        result(i,j) = gray256_Prop(I(i,j) + 1);  
    end  
end  
 
%�����ͼ��
subplot(2,2,3);imshow(result);

%���ͼ������Ҷ�ֵ��Ӧ�����ص������Ķ���  
gray256_result = zeros(256,1);
for i = 1:h  
    for j = 1: w  
        gray256_result(floor(result(i,j)) + 1) = gray256_result(floor(result(i,j)) + 1) + 1;
    end  
end  

%���ͼ������Ҷ�ֵ��Ӧ��������ռ�������صı���  
gray256_Prop_result = zeros(1,256);  
for i = 1:256  
    gray256_Prop_result(i) = gray256_result(i) / pixel;  
end  

%�����ͼ��ֱ��ͼ
subplot(2,2,4); bar(gray256_result,0.01);



