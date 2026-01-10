% Matrix Operations in Octave
% Fundamental matrix manipulations

fprintf('Matrix Operations in Octave\n');
fprintf('===========================\n\n');

%% Creating Matrices
fprintf('=== Creating Matrices ===\n');

% Explicit matrix
A = [1, 2, 3; 4, 5, 6; 7, 8, 9];
fprintf('Matrix A:\n');
disp(A);

% Special matrices
Z = zeros(3, 3);
fprintf('3x3 Zero matrix:\n');
disp(Z);

I = eye(3);
fprintf('3x3 Identity matrix:\n');
disp(I);

O = ones(3, 3);
fprintf('3x3 Ones matrix:\n');
disp(O);

% Random matrix
R = rand(3, 3);
fprintf('3x3 Random matrix:\n');
disp(R);

%% Matrix Access
fprintf('\n=== Accessing Elements ===\n');

fprintf('Element (2,3): %d\n', A(2,3));
fprintf('Row 2: '); fprintf('%d ', A(2,:)); fprintf('\n');
fprintf('Column 3: '); fprintf('%d ', A(:,3)'); fprintf('\n');
fprintf('Submatrix (1:2, 2:3):\n');
disp(A(1:2, 2:3));

%% Matrix Operations
fprintf('\n=== Matrix Arithmetic ===\n');

B = [9, 8, 7; 6, 5, 4; 3, 2, 1];

% Addition
C = A + B;
fprintf('A + B:\n');
disp(C);

% Element-wise multiplication
D = A .* B;
fprintf('A .* B (element-wise):\n');
disp(D);

% Matrix multiplication
E = A * B;
fprintf('A * B (matrix multiplication):\n');
disp(E);

% Transpose
AT = A';
fprintf('Transpose of A:\n');
disp(AT);

%% Matrix Properties
fprintf('\n=== Matrix Properties ===\n');

[rows, cols] = size(A);
fprintf('Size of A: %dx%d\n', rows, cols);
fprintf('Determinant of A: %.2f\n', det(A));
fprintf('Trace of A: %d\n', trace(A));
fprintf('Rank of A: %d\n', rank(A));

%% Matrix Functions
fprintf('\n=== Matrix Functions ===\n');

% For a non-singular matrix
M = [4, 2; 3, 1];
fprintf('Original matrix M:\n');
disp(M);

% Inverse
M_inv = inv(M);
fprintf('Inverse of M:\n');
disp(M_inv);

% Verify: M * M_inv = I
fprintf('M * inv(M) = I:\n');
disp(M * M_inv);

%% Eigenvalues and Eigenvectors
fprintf('\n=== Eigenanalysis ===\n');

[V, D] = eig(M);
fprintf('Eigenvalues (diagonal of D):\n');
disp(diag(D));
fprintf('Eigenvectors (columns of V):\n');
disp(V);

fprintf('\nMatrix operations complete!\n');
