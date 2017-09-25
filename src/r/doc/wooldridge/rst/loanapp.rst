+-----------+-------------------+
| loanapp   | R Documentation   |
+-----------+-------------------+

loanapp
-------

Description
~~~~~~~~~~~

Data loads lazily. Type data(loanapp) into the console.

Usage
~~~~~

::

    data(loanapp)

Format
~~~~~~

A data.frame with 1989 rows and 59 variables:

-  occ. occupancy

-  loanamt. loan amt in thousands

-  action. type of action taken

-  msa. msa number of property

-  suffolk. =1 if property in suffolk co.

-  appinc. applicant income, $1000s

-  typur. type of purchaser of loan

-  unit. number of units in property

-  married. =1 if applicant married

-  dep. number of dependents

-  emp. years employed in line of work

-  yjob. years at this job

-  self. =1 if self employed

-  atotinc. total monthly income

-  cototinc. coapp total monthly income

-  hexp. propose housing expense

-  price. purchase price

-  other. other financing, $1000s

-  liq. liquid assets

-  rep. no. of credit reports

-  gdlin. credit history meets guidelines

-  lines. no. of credit lines on reports

-  mortg. credit history on mortgage paym

-  cons. credit history on consumer stuf

-  pubrec. =1 if filed bankruptcy

-  hrat. housing exp, percent total inc

-  obrat. other oblgs, percent total inc

-  fixadj. fixed or adjustable rate?

-  term. term of loan in months

-  apr. appraised value

-  prop. type of property

-  inss. PMI sought

-  inson. PMI approved

-  gift. gift as down payment

-  cosign. is there a cosigner

-  unver. unverifiable info

-  review. number of times reviewed

-  netw. net worth

-  unem. unemployment rate by industry

-  min30. =1 if minority pop. > 30percent

-  bd. =1 if boarded-up val > MSA med

-  mi. =1 if tract inc > MSA median

-  old. =1 if applic age > MSA median

-  vr. =1 if tract vac rte > MSA med

-  sch. =1 if > 12 years schooling

-  black. =1 if applicant black

-  hispan. =1 if applicant Hispanic

-  male. =1 if applicant male

-  reject. =1 if action == 3

-  approve. =1 if action == 1 or 2

-  mortno. no mortgage history

-  mortperf. no late mort. payments

-  mortlat1. one or two late payments

-  mortlat2. > 2 late payments

-  chist. =0 if accnts deliq. >= 60 days

-  multi. =1 if two or more units

-  loanprc. amt/price

-  thick. =1 if rep > 2

-  white. =1 if applicant white

Source
~~~~~~

https://www.cengage.com/cgi-wadsworth/course_products_wp.pl?fid=M20b&product_isbn_issn=9781111531041

Examples
~~~~~~~~

::

     str(loanapp)
