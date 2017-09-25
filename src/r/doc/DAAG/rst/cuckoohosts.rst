+---------------+-------------------+
| cuckoohosts   | R Documentation   |
+---------------+-------------------+

Comparison of cuckoo eggs with host eggs
----------------------------------------

Description
~~~~~~~~~~~

These data compare mean length, mean breadth, and egg color, between
cuckoos and their hosts.

Usage
~~~~~

::

    cuckoohosts

Format
~~~~~~

A data frame with 10 observations on the following 12 variables.

clength
    mean length of cuckoo eggs in given host's nest

cl.sd
    standard deviation of cuckoo egg lengths

cbreadth
    mean breadth of cuckoo eggs in given host's nest

cb.sd
    standard deviation of cuckoo egg breadths

cnum
    number of cuckoo eggs

hlength
    length of host eggs

hl.sd
    standard deviation of host egg lengths

hbreadth
    breadth of host eggs

hb.sd
    standard deviation of host egg breadths

hnum
    number of host eggs

match
    number of eggs where color matched

nomatch
    number where color did not match

Details
~~~~~~~

Although from the same study that generated data in the data frame
``cuckoos``, the data do not match precisely. The cuckoo egg lengths and
breadths are from the tables on page 168, the host egg lengths and
breadths from Appendix IV on page 176, and the color match counts from
the table on page 171.

Source
~~~~~~

Latter, O.H., 1902. The egg of *cuculus canorus*. an inquiry into the
dimensions of the cuckoo's egg and the relation of the variations to the
size of the eggs of the foster-parent, with notes on coloration, &c.
*Biometrika*, 1:164–176.

Examples
~~~~~~~~

::

    cuckoohosts
    str(cuckoohosts)
    plot(cuckoohosts)
    with(cuckoohosts,
         plot(c(clength,hlength),c(cbreadth,hbreadth),col=rep(1:2,c(6,6))))
