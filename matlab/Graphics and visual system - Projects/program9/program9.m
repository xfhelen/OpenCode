%program9
% Image segmentation
% (a). Develop a program to implement the Roberts, Prewitt,
% Sobel, the Marr-Hildreth and the Canny edge detectors. Use the
% image ¡®building.tif¡¯ to test your detectors. (For technique details
% of Marr-Hildreth and Canny, please refer to pp.736-747 (3rd
% edition, Gonzalez DIP) or MH-Canny.pdf at the same address of
% the slides.)
% (b). Develop a program to implement the Otsu¡¯s method of
% thresholding segmentation, and compare the results with the
% global thresholding method using test image ¡®polymersomes.tif.
% (For technique details, please refer to pp.763-770 (3rd edition,
% Gonzalez DIP), or Otsu.pdf at the same ftp address of slides.)

clc;
clear all;
close all;
%¶ÁÈ¡Í¼Ïñ 
I = imread('building.tif');
figure;subplot(2,3,1);imshow(I);

%Ç°ÆÚ´¦ÀíÍ¼Ïñ
pre1=im2double(I);
[a,b,c]=ddencmp('den','wv',pre1);
pre2=wdencmp('gbl',pre1,'sym4',2,a,b,c);
pre3=medfilt2(pre2,[7 7]);
pre4=imresize(pre3,0.25,'bicubic');
[h,w] = size(pre4);
 
%robertËã×Ó¡ª¡ª±ßÔµ¼ì²â
result1 = pre4;
for i = 1:h-1
    for j =1:w-1
        result1(i,j) = sqrt((pre4(i+1,j) - pre4(i,j))^2+ (pre4(i,j+1) - pre4(i,j))^2);
    end
end
subplot(2,3,2);imshow(result1);

%sobelËã×Ó¡ª¡ª±ßÔµ¼ì²â
result2 = pre4;
for i = 2:h-1
    for j =2:w-1
        result2(i,j) = sqrt((pre4(i+1,j-1)+2*pre4(i+1,j)+pre4(i+1,j+1) - pre4(i-1,j-1)-2*pre4(i-1,j)-pre4(i-1,j+1))^2+ (pre4(i-1,j+1)+2*pre4(i,j+1)+pre4(i+1,j+1) - pre4(i-1,j-1)-2*pre4(i,j-1)-pre4(i+1,j-1))^2);
    end
end
subplot(2,3,3);imshow(result2);

%prewittËã×Ó¡ª¡ª±ßÔµ¼ì²â
result3 = pre4;
for i = 2:h-1
    for j =2:w-1
        result3(i,j) = sqrt((pre4(i+1,j-1)+pre4(i+1,j)+pre4(i+1,j+1) - pre4(i-1,j-1)-pre4(i-1,j)-pre4(i-1,j+1))^2+ (pre4(i-1,j+1)+pre4(i,j+1)+pre4(i+1,j+1) - pre4(i-1,j-1)-pre4(i,j-1)-pre4(i+1,j-1))^2);
    end
end
subplot(2,3,4);imshow(result3);

%logËã×Ó¡ª¡ª±ßÔµ¼ì²â
result4 = pre4;
log=[ 0  0 -1  0  0;
      0 -1 -2 -1  0;
     -1 -2 16 -2 -1;
      0 -1 -2 -1  0;
      0  0 -1  0  0 ];
for i=3:h-2
    for j=3:w-2
        temp=pre4(i-2:i+2,j-2:j+2);
        result4(i,j)=abs(sum(sum(temp.*log)));
    end
end
subplot(2,3,5);imshow(result4);

%cannyËã×Ó¡ª¡ª±ßÔµ¼ì²â
result5=edge(pre4,'canny');
subplot(2,3,6);imshow(result5);

%¶ÁÈ¡Í¼Ïñ 
I = imread('polymersomes.tif');
[h,w] = size(I);
figure;subplot(2,2,1);imshow(I);

%È«¾ÖãÐÖµ
I=double(I);
T=(min(I(:))+max(I(:)))/2;
done=false;
i=0;
result1 = I; 
while ~done
    r1=find(I<=T);
    r2=find(I>=T);
    Tnew=(mean(I(r1))+mean(I(r2)))/2;
    done=abs(Tnew-T)<1;
    T=Tnew;
    i=i+1;
end
result1(r1)=0;
result1(r2)=1;
subplot(2,2,2);imshow(result1);

%OstuãÐÖµ
I =  imread('polymersomes.tif');
level = graythresh(I);
result2 = im2bw(I,level);
subplot(2,2,3); imshow(result2)

