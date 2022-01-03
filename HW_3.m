%%HW
clear; close all; clc

img = imread('cameraman.tif');
im = im2double(img);
F = fft2(im);
Fshitft = fftshift(F);

[M,N] = size(im);
lp_filter = zeros(size(im), 'double');

for i = 1:M
    for j = 1:N
        
        axis([-256 256 -256 256]);
        Hp = -4*pi^2*((i-M/2)^2+(j-N/2)^2);
    end
end

%high frequency signal
lp_filtered = Hp.*F;
lp_filtered = ifftshift(lp_filtered);
lp_filtered = ifft2(lp_filtered);
lp_filtered = real(lp_filtered);

lp_filtered = (lp_filtered+255)/2;
lp_filtered = lp_filtered-(min(lp_filtered)+max(lp_filtered))/2;
lp_filtered = lp_filtered*2/(max(lp_filtered)-min(lp_filtered));

final_lp_filtered = im - lp_filtered;
figure, imshow(final_lp_filtered)

figure,
subplot(1,3,1), imshow(im), title('original image')
subplot(1,3,2), imshow(lp_filtered), title('high frequency signal')
subplot(1,3,3), imshow(final_lp_filtered), title('laplacian filtered')