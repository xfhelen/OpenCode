%program2
%Combining spatial enhancement methods
%Implement the image enhancement task of Section 3.7 (Fig
%3.43) (Section 3.8, Fig. 3.46 in our slides). The image to be
%enhanced is skeleton_orig.tif. You should implement all steps in
%Figure 3.43. (You are encouraged to implement all functions by
%yourself, attempting not to directly use Matlab functions such as
%imfilter or fspecial.)

clc;
clear all;
close all;
%��ȡͼ��  
I = imread('skeleton_orig.tif');  
[ h , w] = size(I);  

%��ʾԭʼͼ��
figure;subplot(2,4,1);imshow(I);

%������˹�˲���
filter = [-1.0, -1.0, -1.0 ; -1.0, 8.0, -1.0; -1.0, -1.0, -1.0 ];

% w=fspecial('laplacian',0)
% g1=imfilter(I,w,'replicate');
% subplot(2,2,2);imshow(g1);

%��������˹�˲�����ͼ������
% result1  = conv2 (I, filter, 'same');
result1 = zeros(h,w);
for i = 2: h - 1
    for j = 2 : w - 1
        mask = I(i-1:i+1, j-1:j+1);
        temp = double(mask).*double(filter);
        result1(i,j) = sum(sum(temp))/256;
%          result(i,j) = 8*I(i,j)-(I(i-1,j)+I(i+1,j)+   I(i-1,j-1)+I(i,j-1)+I(i+1,j-1)+   I(i-1,j+1)+I(i,j+1)+I(i+1,j+1));
    end
end
subplot(2,4,2);imshow(result1);imwrite(result1, '2.tif')
%===============================================================================

%������˹ͼ����ǿ
result2 = double(result1) + double(I)/256;
subplot(2,4,3);imshow(result2);imwrite(result2, '3.tif')
%===============================================================================
%sober����
filter_S = [-1.0, -2.0, -1.0 ; 0.0, 0.0, 0.0; 1.0, 2.0, 1.0 ];

%��sober������ͼ������
result3  = zeros(h,w);
for i = 2: 1 : h - 5
    for j = 2 : 1 : w - 1
        mask = I(i-1:i+1, j-1:j+1);
        temp = double(mask).*double(filter_S);
        result3(i+5,j) = sum(sum(temp))/256;
%          result(i,j) = 8*I(i,j)-(I(i-1,j)+I(i+1,j)+   I(i-1,j-1)+I(i,j-1)+I(i+1,j-1)+   I(i-1,j+1)+I(i,j+1)+I(i+1,j+1));
    end
end
result4 = double(result3) + double(I)/256;
subplot(2,4,4);imshow(result4);imwrite(result4, '4.tif')
%==========================================================================
%5��5��ֵ�˲�ƽ��soberͼ��
filter_Junzhi = ones(5,5);

%�þ�ֵ�˲�����ͼ������
result5  = zeros(h,w);
for i = 3: 1 : h - 3
    for j = 3 : 1 : w - 3
        mask = result4(i-2:i+2, j-2:j+2);
        temp = double(mask).*double(filter_Junzhi)/25;
        result5(i,j) = sum(sum(temp));
%          result(i,j) = 8*I(i,j)-(I(i-1,j)+I(i+1,j)+   I(i-1,j-1)+I(i,j-1)+I(i+1,j-1)+   I(i-1,j+1)+I(i,j+1)+I(i+1,j+1));
    end
end

subplot(2,4,5);imshow(result5);imwrite(result5, '5.tif')
%==========================================================================
%�ڱ�ͼ��
result6 = result3.*result5;
subplot(2,4,6);imshow(result6);imwrite(result6, '6.tif')
%==========================================================================
%I�����ڱ�ͼ��
result7 = double(I)/256 + result6;
subplot(2,4,7);imshow(result7);imwrite(result7, '7.tif')
%==========================================================================
%�Ե�����ͼӦ�����ɣ�٤���任
C = 1;
Gamma = 0.4;
result8  = C*(result7.^Gamma);
subplot(2,4,8);imshow(result8);imwrite(result8, '8.tif')
