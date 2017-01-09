%program7
%Transform image compression (test image lenna.tif)

clc;
clear all;
close all;
%读取图像 
I = imread('lenna.tif');
[ h , w] = size(I);  
figure;subplot(2,4,1);imshow(I);

%DCT变换后的频域图像
I=im2double(I);
T=dctmtx(8)
a1=[16 11 10 16 24  40  51  61;
    12 12 14 19 26  58  60  55;
    14 13 16 24 40  57  69  56;
    14 17 22 29 51  87  80  62;
    18 22 37 56 68  109 103 77;
    24 35 55 64 81  104 113 92;
    49 64 78 87 103 121 120 101;
    72 92 95 98 112 100 103 99 ];
result1 = I;
result2 = I;
for i=1:8:h
    for j=1:8:w
        P=I(i:i+7,j:j+7);
        K=T*P*T';
        result1(i:i+7,j:j+7)=K;
        K=K./a1;%量化
        K(abs(K)<0.03)=0;
        result2(i:i+7,j:j+7)=K;
    end
end
temp=dct2(I);
result1=log(abs(temp));
subplot(2,4,2);imshow(result1);

%zonal mask重建图像
mask=[1 1 1 1 0 0 0 0 
      1 1 1 0 0 0 0 0
      1 1 0 0 0 0 0 0
      1 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0
      0 0 0 0 0 0 0 0 ];
for i=1:8:h
    for j=1:8:w
        P=result2(i:i+7,j:j+7).*mask.*a1;
        K=T'*P*T;
        result4(i:i+7,j:j+7)=K;
    end
end
subplot(2,4,4);imshow(result4);

%zonal mask图像差值
result5 = abs(result4 - I);
subplot(2,4,5);imshow(result5);

%threshold mask重建图像
mask=zeros(8,8);
for i=1:8:h
    for j=1:8:w
        for p = 0:7
            for q = 0:7
                if(result2(i+p,j+q)>0.1)
                    mask(1+p,1+q)=1;
                end
            end
        end
        P=result2(i:i+7,j:j+7).*mask.*a1;
        K=T'*P*T;
        result6(i:i+7,j:j+7)=K;
    end
end
subplot(2,4,6);imshow(result6);

%threshold mask图像差值
result7 = abs(result6 - I);
subplot(2,4,7);imshow(result7);

%==========================================================================
%http://wenku.baidu.com/link?url=b73OeErxLk5XVkq6RLVnEEeLfbD2YUtYvNUSm9bi77
%7L8LbdnOjAHbeMSIuI-t9UZt--bxhxlFYqMI6PQnVF_GKyTVB9jcBHipErM2U49tu





