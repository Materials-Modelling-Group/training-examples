% Plotting and Visualization in Octave
% Creating various types of plots

fprintf('Plotting in Octave\n');
fprintf('==================\n\n');

%% Simple Line Plot
fprintf('Creating line plot...\n');

x = linspace(0, 2*pi, 100);
y = sin(x);

figure(1);
plot(x, y, 'b-', 'LineWidth', 2);
title('Sine Wave');
xlabel('x');
ylabel('sin(x)');
grid on;

% Add legend
hold on;
y2 = cos(x);
plot(x, y2, 'r--', 'LineWidth', 2);
legend('sin(x)', 'cos(x)');
hold off;

%% Multiple Subplots
fprintf('Creating subplot figure...\n');

figure(2);

subplot(2, 2, 1);
plot(x, sin(x));
title('sin(x)');
grid on;

subplot(2, 2, 2);
plot(x, cos(x));
title('cos(x)');
grid on;

subplot(2, 2, 3);
plot(x, tan(x));
title('tan(x)');
ylim([-5, 5]);
grid on;

subplot(2, 2, 4);
plot(x, exp(-x));
title('exp(-x)');
grid on;

%% Scatter Plot
fprintf('Creating scatter plot...\n');

figure(3);
x_scatter = randn(100, 1);
y_scatter = randn(100, 1);

scatter(x_scatter, y_scatter, 50, 'filled');
title('Random Scatter Plot');
xlabel('X');
ylabel('Y');
grid on;

%% Histogram
fprintf('Creating histogram...\n');

figure(4);
data = randn(1000, 1);

hist(data, 30);
title('Histogram of Normal Distribution');
xlabel('Value');
ylabel('Frequency');
grid on;

%% 3D Surface Plot
fprintf('Creating 3D surface plot...\n');

figure(5);
[X, Y] = meshgrid(-3:0.1:3, -3:0.1:3);
Z = sin(sqrt(X.^2 + Y.^2)) ./ sqrt(X.^2 + Y.^2 + 0.1);

surf(X, Y, Z);
title('3D Surface Plot');
xlabel('X');
ylabel('Y');
zlabel('Z');
colorbar;
shading interp;

%% Contour Plot
fprintf('Creating contour plot...\n');

figure(6);
contour(X, Y, Z, 20);
title('Contour Plot');
xlabel('X');
ylabel('Y');
colorbar;

fprintf('\nPlots created! Check figure windows.\n');
fprintf('Save plots with: print -dpng filename.png\n');
