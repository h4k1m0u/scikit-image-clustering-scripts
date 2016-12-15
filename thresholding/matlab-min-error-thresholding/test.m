% https://github.com/carandraug/histthresh
I = rgb2gray(imread('C:\Github\scikit-image-clustering-scripts\img\Lenna.png'));

% A, B, C
y = hist(I(:),0:255);
fprintf('A: %f\n', A(y, 124.0));
fprintf('B: %f\n', B(y, 124.0));
fprintf('C: %f\n', C(y, 124.0));


% Minimum error threshold
% T =  th_minerror_iter(I);

% Display original and thresholded images
%subplot(1, 2, 1);
%imshow(I);
%subplot(1, 2, 2);
%imshow(I > T);