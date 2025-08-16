% Ty Davis
% CS 2130 - Dr. Huson
% Airline paths
% 8/16/2025
% filename: propositional_logic.pl
%
% -----------
% Find if there is a path between two cities in a list of flights

% city definitions
city(dgz).
city(qyy).
city(azi).
city(csi).
city(tva).
city(ppg).
city(brw).

% relations between vertices on the graph
from_to(dgz, qyy).
from_to(dgz, azi).
from_to(qyy, csi).
from_to(azi, tva).
from_to(csi, ppg).
from_to(tva, brw).
from_to(brw, csi).

% recursive route definition to find paths, while writing out the stops
route(A, B, S) :- from_to(A, B), S is 0.
route(A, B, S) :- from_to(A, C), route(C, B, X), S is X + 1, write(' '),write(C),write(' ').

