+---------+-------------------+
| mgus2   | R Documentation   |
+---------+-------------------+

Monoclonal gammapothy data
--------------------------

Description
~~~~~~~~~~~

Natural history of 1341 sequential patients with monoclonal gammapothy
of undetermined significance (MGUS).

Usage
~~~~~

::

    data("mgus2")

Format
~~~~~~

A data frame with 1384 observations on the following 10 variables.

``id``
    subject identifier

``age``
    age at diagnosis, in years

``sex``
    a factor with levels ``F`` ``M``

``hgb``
    hemoglobin

``creat``
    creatinine

``mspike``
    size of the monoclonal serum splike

``ptime``
    time until progression to a plasma cell malignancy (PCM) or last
    contact, in months

``pstat``
    occurrence of PCM: 0=no, 1=yes

``futime``
    time until death or last contact, in months

``death``
    occurrence of death: 0=no, 1=yes

Details
~~~~~~~

This is a larger follow-on study of the condition also found in data set
``mgus``.

Source
~~~~~~

Mayo Clinic data courtesy of Dr. Robert Kyle. All patient identifiers
have been removed, age rounded to the nearest year, and follow-up times
rounded to the nearest month.

References
~~~~~~~~~~

R. Kyle, T. Therneau, V. Rajkumar, J. Offord, D. Larson, M. Plevak, and
L. J. Melton III, A long-terms study of prognosis in monoclonal
gammopathy of undertermined significance. New Engl J Med, 346:564-569
(2002).
