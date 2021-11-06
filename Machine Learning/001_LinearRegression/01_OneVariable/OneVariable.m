 clear all;
 clc;
 
 % loading data
 x = load('x.dat');
 y = load('y.dat');
 
 % plotting data
 plot(x,y, 'o');
 xlabel('Experience (Year)');
 ylabel('Salary ($)');
 
 % data size
 m = length(x);
 
 % adding X_0
 x = [ones(m,1) x];
 
## % initialization
## iter = 1000;
## alpha = 0.001;
## theta = [0 0];
## 
## % gradient descent
## for i=1:iter
##   theta = theta - alpha * sum((x*theta' - y) .* x);
## endfor
 
 theta = pinv(x'*x)*x'*y
 
 hold on;
 plot(x(:,2), x*theta, 'r')
 hold off;
 
 % prediction
 [1 10]*theta
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 