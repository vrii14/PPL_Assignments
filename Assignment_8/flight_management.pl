/*Stimulating flight management system*/

/*flight(from, airline, to, price, duration)*/

/*Toronto to London*/
flight(toronto, 'Air Canada', london, '$500', '360m').
flight(toronto, 'United', london, '$650', '420m').

/*London to Toronto*/
flight(london, 'Air Canada', toronto, '$500', '360m').
flight(london, 'United', toronto, '$650', '420m').

/*Toronto to Madrid*/
flight(toronto, 'Iberia', madrid, '$800', '480m').
flight(toronto, 'United', madrid, '$950', '540m').
flight(toronto, 'Air Canada', madrid, '$900', '480m').

/*Madrid to Toronto*/
flight(madrid, 'Iberia', toronto, '$800', '480m').
flight(madrid, 'United', toronto, '$950', '540m').
flight(madrid, 'Air Canada', toronto, '$900', '480m').

/*Madrid to Barcelona*/
flight(madrid, 'Air Canada', barcelona, '$100', '60m').
flight(madrid, 'Iberia', barcelona, '$120', '65m').

/*Barcelona to Madrid*/
flight(barcelona, 'Air Canada', madrid, '$100', '60m').
flight(barcelona, 'Iberia', madrid, '$120', '65m').

/*Barcelona to London*/
flight(barcelona, 'Iberia', london, '$220', '240m').

/* London to Barcelona*/
flight(london, 'Iberia', barcelona, '$220', '240m').

/*Madrid to Valencia*/
flight(madrid, 'Iberia', valencia, '$40', '50m').

/*Valencia to Madrid*/
flight(valencia, 'Iberia', madrid, '$40', '50m').

/*Barcelona to Valencia*/
flight(barcelona, 'Iberia', valencia, '$110', '75m').

/*Valencia to Barcelona*/
flight(valencia, 'Iberia', barcelona, '$110', '75m').

/*Madrid to Malaga*/
flight(madrid, 'Iberia', malaga, '$50', '30m').

/*malaga to Madrid*/
flight(malaga, 'Iberia', madrid, '$50', '30m').

/*Valencia to Malaga*/
flight(valencia, 'Iberia', malaga, '$80', '120m').

/*Malaga to Valencia*/
flight(malaga, 'Iberia', valencia, '$80', '120m').

/*Paris to Toulouse*/
flight(paris, 'United', toulouse, '$35', '120m').

/*Toulouse to Paris*/
flight(toulouse, 'United', paris, '$35', '120m').


/*airport(city, tax, min_securitydelay)*/

airport(toronto, '$50', '60m').
airport(london, '$75', '80m').
airport(paris, '$50', '60m').
airport(toulhouse, '$40', '30m').
airport(barcelona, '$40', '30m').
airport(madrid, '$75', '45m').
airport(valencia, '$40', '20m').
airport(malaga, '$50', '30m').


/*flight query*/
flight_exist(A, B, C, D, E) :- flight(A, B, C, D, E).

/*airport query*/
airport_details(X, Y, Z) :- airport(X, Y, Z).

/* a. Is there a flight from Toronto to Madrid?*/
a(X, Y):- flight(X,_,Y,_,_) ; flight(Y,_,X,_,_). 

/* b. A flight from city A to city B with airline C is cheap is its price is less than $ 400 */
b(A, B, C) :- flight(A, C, B, D, _) , D<400.

/* c. Is it possible to go from Paris in two flights?*/
c(X, Z) :- flight(X,_,Y,_,_), flight(Y,_,Z,_,_). 

/* d. A flight from city A to city B with airline C is preferred if its cheap or its with Air Canada.*/
d(A, C, B) :- b(A, C, B) ; (C == 'Air Canada').

/* e. If there is a flight from A to B with United then there is a flight from A to B with Air Canada*/
e(A, 'Air Canada', B) :- flight(A, 'United', B, _, _) ; flight(B, 'United', A, _, _).
/*Stimulating flight management system*/

/*flight(from, airline, to, price, duration)*/

/*Toronto to London*/
flight(toronto, 'Air Canada', london, '$500', '360m').
flight(toronto, 'United', london, '$650', '420m').

/*London to Toronto*/
flight(london, 'Air Canada', toronto, '$500', '360m').
flight(london, 'United', toronto, '$650', '420m').

/*Toronto to Madrid*/
flight(toronto, 'Iberia', madrid, '$800', '480m').
flight(toronto, 'United', madrid, '$950', '540m').
flight(toronto, 'Air Canada', madrid, '$900', '480m').

/*Madrid to Toronto*/
flight(madrid, 'Iberia', toronto, '$800', '480m').
flight(madrid, 'United', toronto, '$950', '540m').
flight(madrid, 'Air Canada', toronto, '$900', '480m').

/*Madrid to Barcelona*/
flight(madrid, 'Air Canada', barcelona, '$100', '60m').
flight(madrid, 'Iberia', barcelona, '$120', '65m').

/*Barcelona to Madrid*/
flight(barcelona, 'Air Canada', madrid, '$100', '60m').
flight(barcelona, 'Iberia', madrid, '$120', '65m').

/*Barcelona to London*/
flight(barcelona, 'Iberia', london, '$220', '240m').

/* London to Barcelona*/
flight(london, 'Iberia', barcelona, '$220', '240m').

/*Madrid to Valencia*/
flight(madrid, 'Iberia', valencia, '$40', '50m').

/*Valencia to Madrid*/
flight(valencia, 'Iberia', madrid, '$40', '50m').

/*Barcelona to Valencia*/
flight(barcelona, 'Iberia', valencia, '$110', '75m').

/*Valencia to Barcelona*/
flight(valencia, 'Iberia', barcelona, '$110', '75m').

/*Madrid to Malaga*/
flight(madrid, 'Iberia', malaga, '$50', '30m').

/*malaga to Madrid*/
flight(malaga, 'Iberia', madrid, '$50', '30m').

/*Valencia to Malaga*/
flight(valencia, 'Iberia', malaga, '$80', '120m').

/*Malaga to Valencia*/
flight(malaga, 'Iberia', valencia, '$80', '120m').

/*Paris to Toulouse*/
flight(paris, 'United', toulouse, '$35', '120m').

/*Toulouse to Paris*/
flight(toulouse, 'United', paris, '$35', '120m').


/*airport(city, tax, min_securitydelay)*/

airport(toronto, '$50', '60m').
airport(london, '$75', '80m').
airport(paris, '$50', '60m').
airport(toulhouse, '$40', '30m').
airport(barcelona, '$40', '30m').
airport(madrid, '$75', '45m').
airport(valencia, '$40', '20m').
airport(malaga, '$50', '30m').


/*flight query*/
flight_exist(A, B, C, D, E) :- flight(A, B, C, D, E).

/*airport query*/
airport_details(X, Y, Z) :- airport(X, Y, Z).

/* a. Is there a flight from Toronto to Madrid?*/
a(X, Y):- flight(X,_,Y,_,_) ; flight(Y,_,X,_,_). 

/* b. A flight from city A to city B with airline C is cheap is its price is less than $ 400 */
b(A, B, C) :- flight(A, C, B, D, _) , D<400.

/* c. Is it possible to go from Paris in two flights?*/
c(X, Z) :- flight(X,_,Y,_,_), flight(Y,_,Z,_,_). 

/* d. A flight from city A to city B with airline C is preferred if its cheap or its with Air Canada.*/
d(A, C, B) :- b(A, C, B) ; (C == 'Air Canada').

/* e. If there is a flight from A to B with United then there is a flight from A to B with Air Canada*/
e(A, 'Air Canada', B) :- flight(A, 'United', B, _, _) ; flight(B, 'United', A, _, _).
