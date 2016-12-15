% https://github.com/carandraug/histthresh
I = imread('..\..\img\lena.bmp');

% Minimum error threshold
T =  th_minerror_iter(I);

% Display original and thresholded images
%subplot(1, 2, 1);
%imshow(I);
%subplot(1, 2, 2);
%imshow(I > T);