+---------+-------------------+
| meyer   | R Documentation   |
+---------+-------------------+

A pedigree data on 282 animals deriving from two generations
------------------------------------------------------------

Description
~~~~~~~~~~~

A data frame attributed to Meyer (1989).

“The pedigrees for each of these 282 animals derive from an additional
24 base population (Generation 0) animals that do not have records of
their own but, nevertheless, are of interest with respect to the
inference on their own additive genetic values. Furthermore, it is
presumed that these original 24 base animals are not related to each
other. Therefore, the row dimension of u is 306 (282+24).” (Templeman
\\& Rosa 2004)

Usage
~~~~~

::

    data(meyer)

Format
~~~~~~

A data frame containing 306 records

Source
~~~~~~

Meyer K (1989). Restricted maximum likelihood to estimate variance
components for animal models with several random effects using a
derivative-free algorithm. Genetics, Selection, Evolution 21:317-340.

Tempelman RJ, Rosa GJM. Empirical Bayes Approaches to Mixed Model
Inference in Quantitative Genetics. in Saxton AM (Ed). Genetic Analysis
of Complex Traits Using SAS, chapter 7. SAS Institute Inc., Cary, NC,
USA, 2004

Examples
~~~~~~~~

::

    ## Not run: 
    library(gap)
    meyer <- within(meyer,{
       g1 <- ifelse(generation==1,1,0)
       g2 <- ifelse(generation==2,1,0)
    })
    lm(y~-1+g1+g2,data=meyer)
    library(MCMCglmm)
    m <-MCMCglmm(y~-1+g1+g2,random=animal~1,pedigree=meyer[,1:3],data=meyer,verbose=FALSE)
    summary(m)
    plot(m)   

    meyer <- within(meyer,{
       id <- animal
       animal <- ifelse(!is.na(animal),animal,0)
       dam <- ifelse(!is.na(dam),dam,0)
       sire <- ifelse(!is.na(sire),sire,0)
    })
    # library(kinship)
    # A <- with(meyer,kinship(animal,sire,dam))*2

    A <- kin.morgan(meyer)$kin.matrix*2

    library(regress)
    regress(y~-1+g1+g2,~A,data=meyer)
    prior <- list(R=list(V=1, nu=0.002), G=list(G1=list(V=1, nu=0.002)))
    m2 <- MCMCgrm(y~-1+g1+g2,prior,meyer,A,singular.ok=TRUE,verbose=FALSE)
    summary(m2)
    plot(m2)   

    ## End(Not run)
