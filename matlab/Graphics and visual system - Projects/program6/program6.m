%program6
%Geometric transform (test image: ray_trace_bottle.tif)
%Develop a geometric transform program that will rotate, translate,
%and scale an image by specified amounts, using the nearest neighbor
%and bilinear interpolation methods, respectively.

clc;
clear all;
close all;
%��ȡͼ�� 
I = imread('ray_trace_bottle.tif');
[ h , w] = size(I);  
figure;subplot(2,4,1);imshow(I);

%��תͼ�� - �����
alpha1 = 30;
alpha = - 3.14 * alpha1/180;
result1 = I;
centerH = h/2;
centerW = w/2;
d = h * abs(cos(alpha)) + w * abs(sin(alpha));
k = abs( d / h);
for i = 1 : h
    for j = 1 : w
        p = k *(( i - centerH) * cos(alpha) - ( j - centerW) * sin(alpha)) + centerH;
        q = k *(( i - centerH) * sin(alpha) + ( j - centerW) * cos(alpha)) + centerW;
        p = round(p);
        q = round(q);
        if(p>0 && p<h && q>0 && q<w)
            result1(i,j) = I(p,q);
        else
            result1(i,j) = 0;
        end        
    end
end
subplot(2,4,2);imshow(result1);

%��תͼ�� - ˫���Բ�ֵ
alpha1 = 30;
alpha = - 3.14 * alpha1/180;
result2 = I;
centerH = h/2;
centerW = w/2;
d = h * abs(cos(alpha)) + w * abs(sin(alpha));
k = abs( d / h);
for i = 1 : h
    for j = 1 : w
        p = k *(( i - centerH) * cos(alpha) - ( j - centerW) * sin(alpha)) + centerH;
        q = k *(( i - centerH) * sin(alpha) + ( j - centerW) * cos(alpha)) + centerW;
        p_min = floor(p);
        p_max = ceil(p);
        q_min = floor(q);
        q_max = ceil(q);
                if(p_min>0 && p_max<h && q_min>0 && q_max<w)
            if(q == q_min)
                up = I(p_min,q_min);
                down = I(p_max,q_min);
            else                
                up = (q - q_min) * I(p_min,q_min) + (q_max - q) * I(p_min,q_max); 
                down = (q - q_min) * I(p_max,q_min) + (q_max - q) * I(p_max,q_max); 
            end
            if(p == p_min)
                result2(i,j) = up;
            else
                result2(i,j) = (p - p_min) * up + (p_max - p) * down ;
            end
        else
            result2(i,j) = 0;
        end          
    end
end
subplot(2,4,3);imshow(result2);

%ƽ��ͼ��
trans_x = 50;
trans_y = 100;
result3 = I;
for i = 1 : h
    for j = 1 : w
        p = i - trans_x;
        q = j - trans_y;
        if(p>0 && p<h && q>0 && q<w)
            result3(i,j) = I(p,q);
        else
            result3(i,j) = 0;
        end        
    end
end
subplot(2,4,4);imshow(result3);

%����ͼ�񡪡������
k_h = 0.5;
k_w = 0.5;
result4 = I;
for i = 1 : h
    for j = 1 : w
        p = i/k_h;
        q = j/k_w;
        p = round(p);
        q = round(q);
        if(p>0 && p<h && q>0 && q<w)
            result4(i,j) = I(p,q);
        else
            result4(i,j) = 0;
        end        
    end
end
subplot(2,4,5);imshow(result4);

%����ͼ�񡪡�˫���Բ�ֵ
k_h = 0.5;
k_w = 0.5;
result5 = I;
for i = 1 : h
    for j = 1 : w
        p = i/k_h;
        q = j/k_w;
        p_min = floor(p);
        p_max = ceil(p);
        q_min = floor(q);
        q_max = ceil(q);
        if(p_min>0 && p_max<h && q_min>0 && q_max<w)
            if(q == q_min)
                up = I(p_min,q_min);
                down = I(p_max,q_min);
            else                
                up = (q - q_min) * I(p_min,q_min) + (q_max - q) * I(p_min,q_max); 
                down = (q - q_min) * I(p_max,q_min) + (q_max - q) * I(p_max,q_max); 
            end
            if(p == p_min)
                result5(i,j) = up;
            else
                result5(i,j) = (p - p_min) * up + (p_max - p) * down ;
            end
        else
            result5(i,j) = 0;
        end        
    end
end
subplot(2,4,6);imshow(result5);


