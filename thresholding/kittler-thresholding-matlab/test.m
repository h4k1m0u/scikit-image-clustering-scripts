% https://github.com/carandraug/histthresh
I = imread('..\..\img\lena.bmp');

% Otsu threshold
t_otsu =  floor(graythresh(I) * 255);
fprintf('t_otsu: %f\n', t_otsu);

% Minimum error threshold
t_kittler =  th_minerror_iter(I);
fprintf('t_kittler: %f\n', t_kittler);
 
% Display original and thresholded images
subplot(1, 3, 1);
imshow(I);
subplot(1, 3, 2);
imshow(I > t_otsu);
subplot(1, 3, 3);
imshow(I > t_kittler);