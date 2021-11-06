clear all;clc;

% Loadind data
x = load('x.dat'); 
y = load('y.dat');

% Plotting data
clf;
subplot(211);
scatter(x(:,1),x(:,2),'filled')
xlabel('X_1');
ylabel('X_2');
title('Data');

% data size
m = length(x);
% Add X_0
x = [ones(m, 1), x];

% Normalization 
mu = mean(x);
sigma = std(x);
x(:,2) = (x(:,2) - mu(2))./ sigma(2);
x(:,3) = (x(:,3) - mu(3))./ sigma(3);


% plotting Normalized Data
subplot(212);
scatter(x(:,2),x(:,3),'filled')
xlabel('X_1');
ylabel('X_2');
title('Normalized Data');


% initialization 
alpha = 0.01;
iter = 50;
theta = [0 0 0];

% Gradient Descent 
for i = 1:iter
  theta = theta - alpha * sum((x*theta' - y).*x);
end

% Estimation for [400 , 3]  house
#price = [1, 400, 3]*theta'
price = [1, (400 - mu(2))/sigma(2),(3 - mu(3))/sigma(3)]*theta'








