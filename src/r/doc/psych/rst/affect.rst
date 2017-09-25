+----------+-------------------+
| affect   | R Documentation   |
+----------+-------------------+

Two data sets of affect and arousal scores as a function of personality and movie conditions
--------------------------------------------------------------------------------------------

Description
~~~~~~~~~~~

A recurring question in the study of affect is the proper dimensionality
and the relationship to various personality dimensions. Here is a data
set taken from two studies of mood and arousal using movies to induce
affective states.

Usage
~~~~~

::

    data(affect)

Details
~~~~~~~

These are data from two studies conducted in the Personality, Motivation
and Cognition Laboratory at Northwestern University. Both studies used a
similar methodology:

Collection of pretest data using 5 scales from the Eysenck Personality
Inventory and items taken from the Motivational State Questionnaire (see
``msq``. In addition, state and trait anxiety measures were given. In
the “maps" study, the Beck Depression Inventory was given also.

Then subjects were randomly assigned to one of four movie conditions: 1:
Frontline. A documentary about the liberation of the Bergen-Belsen
concentration camp. 2: Halloween. A horror film. 3: National Geographic,
a nature film about the Serengeti plain. 4: Parenthood. A comedy. Each
film clip was shown for 9 minutes. Following this the MSQ was given
again.

Data from the MSQ were scored for Energetic and Tense Arousal (EA and
TA) as well as Positive and Negative Affect (PA and NA).

Study flat had 170 participants, study maps had 160.

These studies are described in more detail in various publications from
the PMC lab. In particular, Revelle and Anderson, 1997 and Rafaeli and
Revelle (2006). An analysis of these data has also appeared in Smillie
et al. (2012).

Source
~~~~~~

Data collected at the Personality, Motivation, and Cognition Laboratory,
Northwestern University.

References
~~~~~~~~~~

Revelle, William and Anderson, Kristen Joan (1997) Personality,
motivation and cognitive performance: Final report to the Army Research
Institute on contract MDA 903-93-K-0008

Rafaeli, Eshkol and Revelle, William (2006), A premature consensus: Are
happiness and sadness truly opposite affects? Motivation and Emotion,
30, 1, 1-12.

Smillie, Luke D. and Cooper, Andrew and Wilt, Joshua and Revelle,
William (2012) Do Extraverts Get More Bang for the Buck? Refining the
Affective-Reactivity Hypothesis of Extraversion. Journal of Personality
and Social Psychology, 103 (2), 206-326.

Examples
~~~~~~~~

::

    data(affect)
    describeBy(affect[-1],group="Film")
    pairs.panels(affect[14:17],bg=c("red","black","white","blue")[affect$Film],pch=21,
        main="Affect varies by movies ")
    errorCircles("EA2","TA2",data=affect,group="Film",labels=c("Sad","Fear","Neutral","Humor")
    , main="Enegetic and Tense Arousal by Movie condition")
    errorCircles(x="PA2",y="NA2",data=affect,group="Film",labels=c("Sad","Fear","Neutral","
    Humor"),  main="Positive and Negative Affect by Movie condition")

