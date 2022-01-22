clear; close all; clc;

I0 = imread('brain_0.png');
I1 = imread('brain_1.png');
I2 = imread('brain_2.png');
I3 = imread('brain_3.png');
I4 = imread('brain_4.png');
I5 = imread('brain_5.png');

I0_slice = imcrop(rgb2gray(I0), [50 235 271 120]);
I1_slice = imcrop(rgb2gray(I1), [49 235 271 120]);
I2_slice = imcrop(rgb2gray(I2), [48 235 271 120]);
I3_slice = imcrop(rgb2gray(I3), [48 240 271 120]);
I4_slice = imcrop(rgb2gray(I4), [48 240 271 120]);
I5_slice = imcrop(rgb2gray(I5), [50 240 271 120]);

filtered_I0 = imadjust(I0_slice,[],[], 0.7);
filtered_I1 = imadjust(I1_slice,[],[], 0.7);
filtered_I2 = imadjust(I2_slice,[],[], 0.7);
filtered_I3 = imadjust(I3_slice,[],[], 0.7);
filtered_I4 = imadjust(I4_slice,[],[], 0.7);
filtered_I5 = imadjust(I5_slice,[],[], 0.7);

figure(1)
subplot(2,3,1), imshow(filtered_I0), title('brain0 slice');
subplot(2,3,2), imshow(filtered_I1), title('brain1 slice');
subplot(2,3,3), imshow(filtered_I2), title('brain2 slice');
subplot(2,3,4), imshow(filtered_I3), title('brain3 slice');
subplot(2,3,5), imshow(filtered_I4), title('brain4 slice');
subplot(2,3,6), imshow(filtered_I5), title('brain5 slice');

[i0, j0] = size(I0_slice);
[i1, j1] = size(I1_slice);
[i2, j2] = size(I2_slice);
[i3, j3] = size(I3_slice);
[i4, j4] = size(I4_slice);
[i5, j5] = size(I5_slice);

b0=0;, b1=0;, b2=0;, b3=0;, b4=0;, b5=0;
w=0;
bw = 0;

for bw = 0 : 32 : 255
    for i = 1 : i0
        for j = 1 : j0
            if bw <= 255
                if filtered_I0(i,j) >= bw & filtered_I0(i,j) <= bw+31
                    b0 = b0+1;
                end
            end
        end
    end
disp(b0);
b0=0;
end

for bw = 0 : 32 : 255
    for i = 1 : i1
        for j = 1 : j1
            if bw <= 255
                if filtered_I1(i,j) >= bw & filtered_I1(i,j) <= bw+31
                    b1 = b1+1;
                end
            end
        end
    end
disp(b1);
b1=0;
end

for bw = 0 : 32 : 255
    for i = 1 : i2
        for j = 1 : j2
            if bw <= 255
                if filtered_I2(i,j) >= bw & filtered_I2(i,j) <= bw+31
                    b2 = b2+1;
                end
            end
        end
    end
disp(b2);
b2=0;
end

for bw = 0 : 32 : 255
    for i = 1 : i3
        for j = 1 : j3
            if bw <= 255
                if filtered_I3(i,j) >= bw & filtered_I3(i,j) <= bw+31
                    b3 = b3+1;
                end
            end
        end
    end
disp(b3);
b3=0;
end

for bw = 0 : 32 : 255
    for i = 1 : i4
        for j = 1 : j4
            if bw <= 255
                if filtered_I4(i,j) >= bw & filtered_I4(i,j) <= bw+31
                    b4 = b4+1;
                end
            end
        end
    end
disp(b4);
b4=0;
end

for bw = 0 : 32 : 255
    for i = 1 : i5
        for j = 1 : j5
            if bw <= 255
                if filtered_I5(i,j) >= bw & filtered_I5(i,j) <= bw+31
                    b5 = b5+1;
                end
            end
        end
    end
disp(b5);
b5=0;
end