clear all;clc;

% Loading data
x = csvread('x.dat');
y = csvread('y.dat');

%plotting Data
zero_y = find(y==0);
one_y  = find(y==1);
clf
scatter3(x(zero_y,1), x(zero_y,2), x(zero_y,3) ,'r');
hold on;
scatter3(x(one_y,1), x(one_y,2), x(one_y,3) ,'g');
hold off;

% Data size
m  = length(x);

% intercept
x = [ones(m,1) x];

% Train Data 
x_train = x(1:1000,:);
y_train = y(1:1000,:);

% Test Data 
x_test = x(1001:m,:);
y_test = y(1001:m,:);

% initialization 
theta = [0 0 0 0 0];
alpha = 0.00001;
iter = 500;

% Gradient Descent 
for i = 1:iter
  theta = theta - alpha * sum((x_train*theta' - y_train).*x_train);
end


% Accuracy
accuracy = sum((x_test*theta' >= 0.5) == y_test)/ length(x_test)*100


















