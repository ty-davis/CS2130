% Ty Davis
% Homework 2
% logic gates in Prolog
% 7/10/2025

% My XOR definition
myxor(0,0,0).
myxor(0,1,1).
myxor(1,0,1).
myxor(1,1,0).

% My NAND definition
mynand(0,0,1).
mynand(0,1,1).
mynand(1,0,1).
mynand(1,1,0).

mycircuit(X,Y,Z,F) :- myxor(X,Y,T1), myxor(T1,Z,T2), mynand(T1,T2,F),
	writeln('X | Y | Z || F'),
	write(X),write(' | '),
	write(Y),write(' | '),
	write(Z),write(' || '),
	writeln(F).
