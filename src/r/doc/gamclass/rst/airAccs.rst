+-----------+-------------------+
| airAccs   | R Documentation   |
+-----------+-------------------+

Aircraft Crash data
-------------------

Description
~~~~~~~~~~~

Aircraft Crash Data

Usage
~~~~~

::

    data(airAccs)

Format
~~~~~~

A data frame with 5666 observations on the following 7 variables.

``Date``
    Date of Accident

``location``
    Location of accident

``operator``
    Aircraft operator

``planeType``
    Aircraft type

``Dead``
    Number of deaths

``Aboard``
    Number aboard

``Ground``
    Deaths on ground

Details
~~~~~~~

For details of inclusion criteria, see
http://www.planecrashinfo.com/database.htm

Source
~~~~~~

http://www.planecrashinfo.com/database.htm

References
~~~~~~~~~~

http://www.planecrashinfo.com/reference.htm

Examples
~~~~~~~~

::

    data(airAccs)
    str(airAccs)
