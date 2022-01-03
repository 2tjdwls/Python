clear; close all; clc;

r = 80; c = 60; r2 = 2; c2 = 900;

m1 = ones(r, c);
m2 = 255*ones(r, c);
m3 = ones(r, 0.5*c);
m4 = 255*ones(r, 0.5*c);
m5 = cat(2, m4, m1, m2, m1, m2, m1, m2, m1, m2, m1, m2, m1, m2, m1, m2, m3);
m6 = cat(2, m1, m2, m1, m2, m1, m2, m1, m2, m1, m2, m1, m2, m1, m2, m1);
m7 = 80*ones(r2, c2);
m = cat(1, m7, m5, m7, m6, m7, m5, m7, m6, m7, m5, m7, m6, m7, m5, m7);

figure, imshow(m, []), title('Is it parallel to you?');
