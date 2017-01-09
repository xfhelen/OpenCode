% program10
% Image representation and description
% (a). Develop a program to implement the boundary following
% algorithm, the resampling grid and calculate the chain code and
% the first difference chain code. Use the image ‘noisy_stroke.tif’ for
% test. (For technique details, please refer to pp.818-822 (3rd
% edition, Gonzalez DIP) or boundaryfollowing.pdf at the same
% address of the slides.)
% (b). Develop a program to implement the image description
% by the principal components (PC). Calculate and display the PC
% images and the reconstructed images from 2 PCs. Use the six
% images in ‘washingtonDC.rar’ as the test images.

clc;
clear all;
close all;
%读取图像 
I = imread('noisy_stroke.tif');
[ h , w] = size(I);  
figure;subplot(2,4,1);imshow(I);

%均值滤波器
Junzhi = ones(5,5)/25;
I = double(I)/256;
result1 = I;
for i = 1: h-4
    for j = 1: w-4
        result1(i,j) = sum(sum(I(i:i+4,j:j+4).* Junzhi));   
    end 
end
subplot(2,4,2);imshow(result1);

%全局ostu
YuZhi = zeros(200,1);
YuZhi(1) = 0.5;
chazhi = 0.5;
for k = 1 : 200
    if chazhi >= 0.001
        result2 = zeros(h,w);
        for i = 1 : h
           for j = 1 : w
               if result1(i,j)>YuZhi(k)
                   result2(i,j)=1;
               else
                   result2(i,j)=0;
               end
           end
        end
        white = result1.*result2;
        [h1,w1] = find(white~=0);
        white_ave = sum(sum(white))/length(h1);
        
        black = result1.*(1-result2);
        [h2,w2] = find(black~=0);
        black_ave = sum(sum(black))/length(h2);
        
        YuZhi(k+1)=(white_ave + black_ave)/2;
        chazhi = abs(YuZhi(k+1) - YuZhi(k));
     else
        break;
     end
end
subplot(2,4,3);imshow(result2);

%边界追踪
result3 = zeros(h,w);
Tidu = zeros(h*w,2);
Tidu(1,:) = [0,-1];
pixel = 1;
for i=1:h
      for j=1:w
            if result2(i,j)==1 && result2(i+10,j)==1
                start_i=i;
                start_j=j;
                break;
            end            
      end
      if j~=w
            break;
      end
end
boundary_i = start_i; 
boundary_j = start_j;
while(1)
    temp=result2(boundary_i-1:boundary_i+1,boundary_j-1:boundary_j+1);
    if Tidu(pixel,:)==[0, -1]
        H=[2 3 4;
               1 0 5;
               8 7 6];
    end
    if  Tidu(pixel,:)==[-1,-1]
        H=[1 2 3;
               8 0 4;
               7 6 5];
    end
    if Tidu(pixel,:)==[-1,0]
        H=[8 1 2;
               7 0 3;
               6 5 4];
    end
    if Tidu(pixel,:)==[-1,1]
        H=[7 8 1;
               6 0 2;
               5 4 3];
    end
    if Tidu(pixel,:)==[0,1]
        H=[6 7 8;
               5 0 1;
               4 3 2];
    end
    if Tidu(pixel,:)==[1,1]
        H=[5 6 7;
               4 0 8;
               3 2 1];
    end
    if Tidu(pixel,:)==[1,0]
        H=[4 5 6;
               3 0 7;
               2 1 8];
    end
    if Tidu(pixel,:)==[1,-1]
        H=[3 4 5;
               2 0 6;
               1 8 7];
    end
    pixel=pixel+1;
    result3(boundary_i,boundary_j)=1;
    for i=1:9
        [v,c]=find(H==i);
        if temp(v,c)==1
            boundary_i=boundary_i+v-2;       
            boundary_j=boundary_j+c-2;
            [v1,c1]=find(H==(i-1));
        break; 
        end
    end
    if  boundary_i== start_i&& boundary_j==start_j
        break;
    end
    Tidu(pixel,:)=[v1-v,c1-c];
end
subplot(2,4,4);imshow(result3);


%重采样
result4=zeros(h,w); 
H2 = ones(20,20);
for i = 1:20: h-20
    for j = 1:20: w-20
        k = sum(sum(result3(i:i+19,j:j+19).* H2));  
        if(k>0)
            result4(i,j) = 1;
        end
    end 
end
subplot(2,4,5);imshow(result4);%imwrite(result4,'result4.jpg');

%链码result5
temp1=result4;
H3=[3 2 1;
    4 8 0;
    5 6 7];
countc=1;
for i=1:20:h
      for j=1:20:w
            if result4(i,j)==1
                start_i=i;
                start_j=j;
                break;
            end            
      end
end
bd_i=start_i;
bd_j=start_j;
while(1)
    for i=0:2:6
        [v2,c2]=find(H3==i);
        if temp1(bd_i+51*(v2-2),bd_j+51*(c2-2))==1
            temp1(bd_i+51*(v2-2),bd_j+51*(c2-2))=0;
            bd_i=bd_i+51*(v2-2);       bd_j=bd_j+51*(c2-2);
            break; 
        end
	end
    result5(countc)=i;
    countc=countc+1;
    if  bd_i==ci&&bd_j==cj
        break;
    end
end
l=length(result5);
result5(1,l+1)=result5(1);
result5

%一阶差分链码result6
result6=zeros(1,l);
for i=1:l
    ll=result5(i+1)-result5(i);
    if ll<0
        ll=ll+8;
    end
    result6(i)=ll;
end
result6
%b==================================================================

I1 = double(imread('WashingtonDC_Band1.tif'));
[h,w] = size(I1);
X = imstack2vectors(I1);
P = princomp(X,6);
result1 = P.Y;
result1 = reshape(result1,h,w);
figure;subplot(2,6,1);imshow(result1);title('band1');

d = diag(P.Cy);
P = princomp(X,2);
result21 = P.X;
result21 = reshape(result21,h,w);
subplot(2,6,7);imshow(result21);title('band1-R');


I2 = double(imread('WashingtonDC_Band2.tif'));
X = imstack2vectors(I2);
P = princomp(X,6);
result2 = P.Y;
result2 = reshape(result2,h,w);
subplot(2,6,2);imshow(result2);title('band2');

d = diag(P.Cy);
P = princomp(X,2);
result22 = P.X;
result22 = reshape(result22,h,w);
subplot(2,6,8);imshow(result22);title('band2-R');

I3 = double(imread('WashingtonDC_Band3.tif'));
X = imstack2vectors(I3);
P = princomp(X,6);
result3 = P.Y;
result3 = reshape(result3,h,w);
subplot(2,6,3);imshow(result3);title('band3');

d = diag(P.Cy);
P = princomp(X,2);
result23 = P.X;
result23 = reshape(result23,h,w);
subplot(2,6,9);imshow(result23);title('band3-R');

I4 = double(imread('WashingtonDC_Band4.tif'));
X = imstack2vectors(I4);
P = princomp(X,6);
result4 = P.Y;
result4=reshape(result4,h,w);
subplot(2,6,4);imshow(result4);title('band4');

d = diag(P.Cy);
P = princomp(X,2);
result24 = P.X;
result24 = reshape(result24,h,w);
subplot(2,6,10);imshow(result24);title('band4-R');

I5 = double(imread('WashingtonDC_Band5.tif'));
X = imstack2vectors(I5);
P = princomp(X,6);
result5 = P.Y;
result5 = reshape(result5,h,w);
subplot(2,6,5);imshow(result5);title('band5');

d = diag(P.Cy);
P = princomp(X,2);
result25 = P.X;
result25 = reshape(result25,h,w);
subplot(2,6,11);imshow(result25);title('band5-R');

I6 = double(imread('WashingtonDC_Band6.tif'));
X = imstack2vectors(I6);
P = princomp(X,6);
result6 = P.Y;
result6 = reshape(result6,h,w);
subplot(2,6,6);imshow(result6);title('band6');

d = diag(P.Cy);
P = princomp(X,2);
result26 = P.X;
result26 = reshape(result26,h,w);
subplot(2,6,12);imshow(result26);title('band6-R');


