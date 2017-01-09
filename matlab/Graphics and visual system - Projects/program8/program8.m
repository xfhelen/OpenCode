%program8
% Morpholigical Processing
% a). Implement the morphological operations: erosion, dilation,
% opening and closing, and use the noisy_fingerprint.tif to check
% your implementation.
% b). Implement boundary extraction, hole filling, connected
% component extraction. Using licoln_from_penny.tif,
% region_filling_refletion.tif and chickenfilet_with_bones.tif to verify
% the results, respectively.

clc;
clear all;
close all;
%��ȡͼ�� 
I = imread('noisy_fingerprint.tif');
[h,w] = size(I);
figure;subplot(2,4,1);imshow(I);

%a=======================================================================
%��ʴ
disk=[0 1 0
      1 1 1
      0 1 0];%�����Ǵ���һ���뾶Ϊ5��ƽ̹��Բ�̽ṹԪ��
result1 = I;
for i = 2: h-1
    for j = 2: w-1
        h = I(i-1:i+1,j-1:j+1).* disk;
        k = [h(1,2),h(2,1),h(2,2),h(2,3),h(3,2)];
        result1(i,j) = min(min(k));
    end 
end
subplot(2,4,2);imshow(result1);

%����
result2 = I;
for i = 2: h-1
    for j = 2: w-1
        h = I(i-1:i+1,j-1:j+1).* disk;
        result2(i,j) = max(max(h));
    end 
end
subplot(2,4,3);imshow(result2);

%������
result3 = I;
for i = 2: h-1
    for j = 2: w-1
        h = result1(i-1:i+1,j-1:j+1).* disk;%��result1����
        result3(i,j) = max(max(h));
    end 
end
subplot(2,4,4);imshow(result3);

%�ղ���
result4 = result2;
for i = 2: h-1
    for j = 2: w-1
        h = result2(i-1:i+1,j-1:j+1).* disk;
        k = [h(1,2),h(2,1),h(2,2),h(2,3),h(3,2)];%��result1��ʴ
        result4(i,j) = min(min(k));
    end 
end
subplot(2,4,5);imshow(result4);

%b=======================================================================
%��ȡͼ�� 
I1 = imread('licoln_from_penny.tif');
figure;subplot(2,3,1);imshow(I1);
I2 = imread('region_filling_reflections.tif');
subplot(2,3,2);imshow(I2);
I3 = imread('chickenfilet_with_bones.tif');
subplot(2,3,3);imshow(I3);

%�߽���ȡ
result1 = I1 - imerode(I1,disk);
subplot(2,3,4);imshow(result1);

%�׶����
result2 = imfill(I2,'holes');
subplot(2,3,5);imshow(result2);

%��ͨ�����ȡ
[h,w] = size(I3);
I4 = zeros(h,w);
for i = 1:h
    for j = 1:w
        if(I3(i,j) > 200)
            I4(i,j) = 1;
        end
    end
end      
disk=[0 0 1 0 0
      0 1 1 1 0
      1 1 1 1 1
      0 1 1 1 0
      0 0 1 0 0];%�����Ǵ���һ���뾶Ϊ5��ƽ̹��Բ�̽ṹԪ��
I4_fs=imerode(I4,disk);
subplot(2,3,6);imshow(I4_fs);
result3 = max(max(bwlabel(I4_fs)))

