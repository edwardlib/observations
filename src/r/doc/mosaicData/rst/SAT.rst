+-------+-------------------+
| SAT   | R Documentation   |
+-------+-------------------+

State by State SAT data
-----------------------

Description
~~~~~~~~~~~

SAT data assembled for a statistics education journal article on the
link between SAT scores and measures of educational expenditures

Usage
~~~~~

::

    data(SAT)

Format
~~~~~~

A data frame with 50 observations on the following variables.

-  ``state`` a factor with names of each state

-  ``expend`` expenditure per pupil in average daily attendance in
   public elementary and secondary schools, 1994-95 (in thousands of US
   dollars)

-  ``ratio`` average pupil/teacher ratio in public elementary and
   secondary schools, Fall 1994

-  ``salary`` estimated average annual salary of teachers in public
   elementary and secondary schools, 1994-95 (in thousands of US
   dollars)

-  ``frac`` percentage of all eligible students taking the SAT, 1994-95

-  ``verbal`` average verbal SAT score, 1994-95

-  ``math`` average math SAT score, 1994-95

-  ``sat`` average total SAT score, 1994-95

Source
~~~~~~

http://www.amstat.org/publications/jse/secure/v7n2/datasets.guber.cfm

References
~~~~~~~~~~

Deborah Lynn Guber, "Getting what you pay for: the debate over equity in
public school expenditures" (1999), *Journal of Statistics Education*
7(2).

Examples
~~~~~~~~

::

    data(SAT)
    if (require(lattice)) {
      xyplot(sat ~ expend, SAT)
      xyplot(sat ~ expend, SAT, 
           panel=function(x,y){grid.text(abbreviate(SAT$state, 3), x, y, default.units='native')})
    } 
