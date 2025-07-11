% Ty Davis
% CS 2130 - Online
% Boolean Algebra Program
% 7/10/2025
% filename: boolean_alg.pl
%
% -----------
% Demonstrate boolean algebra by creating a full-adder circuit with prolog


% My OR gate definitions
myor(0,0,0).
myor(0,1,1).
myor(1,0,1).
myor(1,1,1).

% My AND definitions
myand(0,0,0).
myand(0,1,0).
myand(1,0,0).
myand(1,1,1).

% My NOT definitions
mynot(0,1).
mynot(1,0).

% The definition of the function
pmath(A1, A0, B1, B0, S1, S0, Cout) :-
	% solve to S0
	myor(A0, B0, T1),
	myand(A0, B0, T2),
	mynot(T2, T3),
	myand(T1, T3, S0),

	% solve to S1
	myor(A1, B1, T4),
	myand(A1, B1, T5),
	mynot(T5, T6),
	myand(T4, T6, T7),
	myor(T2, T7, T8),
	myand(T2, T7, T9),
	mynot(T9, T10),
	myand(T8, T10, S1),
	
	% finish the carry
	myor(T9, T5, Cout),

	write(A1),
	write(A0),write(' + '),
	write(B1),
	write(B0),write(' = '),
	write(Cout),
	write(S1),
	writeln(S0).

