clear all;
clc;

% loading data
x = load('x.dat');
y = load('y.dat');

% plotting data
clf;
scatter(x,y,'filled');

% data size 
m = length(x);

% adding X_0
x = [ones(m,1) x];

% initialization
tau = m*0.03;

for i=1:m
  w_i  = exp(-(x(i,2) - x(:,2)).^2 / (2*tau^2));
  w = diag(w_i);
  theta = inv(x'*w*x)*x'*w*y;
  y_pred(i) = x(i,:)*theta;
endfor

hold on;
plot(x(:,2), y_pred, 'r-', 'linewidth', 3);








