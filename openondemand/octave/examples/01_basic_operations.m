% Basic Octave Operations
% Introduction to fundamental Octave commands

fprintf('GNU Octave Basic Operations\n');
fprintf('===========================\n\n');

%% Arithmetic Operations
fprintf('=== Arithmetic Operations ===\n');
a = 10;
b = 3;

fprintf('a = %d, b = %d\n', a, b);
fprintf('Addition: %d + %d = %d\n', a, b, a + b);
fprintf('Subtraction: %d - %d = %d\n', a, b, a - b);
fprintf('Multiplication: %d * %d = %d\n', a, b, a * b);
fprintf('Division: %d / %d = %.2f\n', a, b, a / b);
fprintf('Power: %d ^ %d = %d\n', a, b, a ^ b);
fprintf('Modulo: %d mod %d = %d\n', a, b, mod(a, b));

%% Vector Operations
fprintf('\n=== Vector Operations ===\n');

% Create vectors
v1 = [1, 2, 3, 4, 5];
v2 = [5, 4, 3, 2, 1];

fprintf('v1 = ['); fprintf('%d ', v1); fprintf(']\n');
fprintf('v2 = ['); fprintf('%d ', v2); fprintf(']\n');

% Element-wise operations
fprintf('v1 + v2 = ['); fprintf('%d ', v1 + v2); fprintf(']\n');
fprintf('v1 .* v2 = ['); fprintf('%d ', v1 .* v2); fprintf(']\n');

% Dot product
dot_prod = dot(v1, v2);
fprintf('Dot product: %d\n', dot_prod);

% Vector length
fprintf('Length of v1: %.2f\n', norm(v1));

%% Common Functions
fprintf('\n=== Common Functions ===\n');

x = pi/4;
fprintf('x = π/4\n');
fprintf('sin(x) = %.4f\n', sin(x));
fprintf('cos(x) = %.4f\n', cos(x));
fprintf('tan(x) = %.4f\n', tan(x));
fprintf('exp(x) = %.4f\n', exp(x));
fprintf('log(x) = %.4f\n', log(x));
fprintf('sqrt(x) = %.4f\n', sqrt(x));

%% Random Numbers
fprintf('\n=== Random Numbers ===\n');

% Set seed for reproducibility
rand('seed', 42);

% Uniform random numbers
uniform = rand(1, 5);
fprintf('Uniform [0,1]: '); fprintf('%.2f ', uniform); fprintf('\n');

% Normal random numbers
normal = randn(1, 5);
fprintf('Normal (0,1): '); fprintf('%.2f ', normal); fprintf('\n');

% Random integers
integers = randi(10, 1, 5);
fprintf('Random integers [1,10]: '); fprintf('%d ', integers); fprintf('\n');

%% Statistical Functions
fprintf('\n=== Statistical Functions ===\n');

data = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11];
fprintf('Data: '); fprintf('%d ', data); fprintf('\n');
fprintf('Mean: %.2f\n', mean(data));
fprintf('Median: %.2f\n', median(data));
fprintf('Std Dev: %.2f\n', std(data));
fprintf('Variance: %.2f\n', var(data));
fprintf('Min: %d\n', min(data));
fprintf('Max: %d\n', max(data));
fprintf('Range: %d\n', max(data) - min(data));

fprintf('\nBasic operations complete!\n');
