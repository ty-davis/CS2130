% Ty Davis
% Homework 1
% File: hw1.pl
% This is a practice Prolog program that creates a family tree

female(ann).
female(beth).
female(liz).
female(sue).
female(jill).
female(mary).
female(carol).

male(bob).
male(ted).
male(bill).
male(sam).
male(harry).
male(john).
male(matt).

parentof(beth,bill).
parentof(bill,jill).
parentof(bill,liz).
parentof(ann,jill).
parentof(ann,liz).
parentof(ann,ted).
parentof(liz,matt).
parentof(matt,john).
parentof(bob,carol).
parentof(harry,sue).
parentof(harry,sam).
parentof(carol,sue).
parentof(carol,sam).
parentof(sue,mary).
parentof(mary,john).

childof(Child, Parent) :- parentof(Parent,Child).

siblings(Sib1, Sib2) :- parentof(Parent, Sib1), parentof(Parent, Sib2), Sib1 \== Sib2.

sisterof(Sis, Sib) :- siblings(Sis, Sib), female(Sis).

ancestor_of(A,B) :- parentof(A,B).
ancestor_of(A,B) :- parentof(A,C), ancestor_of(C,B).

ancestor_gen(A,B,G) :- parentof(A,B), G is 1.
ancestor_gen(A,B,G) :- parentof(A,C), ancestor_gen(C,B,F), G is F + 1.
