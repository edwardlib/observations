+---------------+-------------------+
| ToothGrowth   | R Documentation   |
+---------------+-------------------+

The Effect of Vitamin C on Tooth Growth in Guinea Pigs
------------------------------------------------------

Description
~~~~~~~~~~~

The response is the length of odontoblasts (cells responsible for tooth
growth) in 60 guinea pigs. Each animal received one of three dose levels
of vitamin C (0.5, 1, and 2 mg/day) by one of two delivery methods,
(orange juice or ascorbic acid (a form of vitamin C and coded as
``VC``).

Usage
~~~~~

::

    ToothGrowth

Format
~~~~~~

A data frame with 60 observations on 3 variables.

+--------+--------+-----------+-------------------------------+
| [,1]   | len    | numeric   | Tooth length                  |
+--------+--------+-----------+-------------------------------+
| [,2]   | supp   | factor    | Supplement type (VC or OJ).   |
+--------+--------+-----------+-------------------------------+
| [,3]   | dose   | numeric   | Dose in milligrams/day        |
+--------+--------+-----------+-------------------------------+

Source
~~~~~~

C. I. Bliss (1952) *The Statistics of Bioassay*. Academic Press.

References
~~~~~~~~~~

McNeil, D. R. (1977) *Interactive Data Analysis*. New York: Wiley.

Crampton, E. W. (1947) The growth of the odontoblast of the incisor
teeth as a criterion of vitamin C intake of the guinea pig. *The Journal
of Nutrition* **33(5)**: 491–504.
http://jn.nutrition.org/content/33/5/491.full.pdf

Examples
~~~~~~~~

::

    require(graphics)
    coplot(len ~ dose | supp, data = ToothGrowth, panel = panel.smooth,
           xlab = "ToothGrowth data: length vs dose, given type of supplement")
