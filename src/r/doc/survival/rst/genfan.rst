+----------+-------------------+
| genfan   | R Documentation   |
+----------+-------------------+

Generator fans
--------------

Description
~~~~~~~~~~~

The data come from a field engineering study of the time to failure of
diesel generator fans. The ultimate goal was to decide whether or not to
replace the working fans with a higher quality fan to prevent future
failures. Seventy generators were studied. For each one, the number of
hours of running time from its first being put into service until fan
failure or until the end of the study(whichever came first) was
recorded.

Usage
~~~~~

::

    data("genfan")

Format
~~~~~~

A data frame with 70 observations on the following 2 variables.

``hours``
    hours of service

``status``
    1=failure, 0=censored

References
~~~~~~~~~~

Nelson, Journal of Quality Technology, 1:27-52, 1969
