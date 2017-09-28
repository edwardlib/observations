# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def msq(path):
  """75 mood items from the Motivational State Questionnaire for 3896 participa
  nts

  Emotions may be described either as discrete emotions or in dimensional
  terms. The Motivational State Questionnaire (MSQ) was developed to study
  emotions in laboratory and field settings. The data can be well
  described in terms of a two dimensional solution of energy vs tiredness
  and tension versus calmness. Additional items include what time of day
  the data were collected and a few personality questionnaire scores.

  A data frame with 3896 observations on the following 92 variables.

  `active`
      a numeric vector

  `afraid`
      a numeric vector

  `alert`
      a numeric vector

  `angry`
      a numeric vector

  `anxious`
      a numeric vector

  `aroused`
      a numeric vector

  `ashamed`
      a numeric vector

  `astonished`
      a numeric vector

  `at.ease`
      a numeric vector

  `at.rest`
      a numeric vector

  `attentive`
      a numeric vector

  `blue`
      a numeric vector

  `bored`
      a numeric vector

  `calm`
      a numeric vector

  `cheerful`
      a numeric vector

  `clutched.up`
      a numeric vector

  `confident`
      a numeric vector

  `content`
      a numeric vector

  `delighted`
      a numeric vector

  `depressed`
      a numeric vector

  `determined`
      a numeric vector

  `distressed`
      a numeric vector

  `drowsy`
      a numeric vector

  `dull`
      a numeric vector

  `elated`
      a numeric vector

  `energetic`
      a numeric vector

  `enthusiastic`
      a numeric vector

  `excited`
      a numeric vector

  `fearful`
      a numeric vector

  `frustrated`
      a numeric vector

  `full.of.pep`
      a numeric vector

  `gloomy`
      a numeric vector

  `grouchy`
      a numeric vector

  `guilty`
      a numeric vector

  `happy`
      a numeric vector

  `hostile`
      a numeric vector

  `idle`
      a numeric vector

  `inactive`
      a numeric vector

  `inspired`
      a numeric vector

  `intense`
      a numeric vector

  `interested`
      a numeric vector

  `irritable`
      a numeric vector

  `jittery`
      a numeric vector

  `lively`
      a numeric vector

  `lonely`
      a numeric vector

  `nervous`
      a numeric vector

  `placid`
      a numeric vector

  `pleased`
      a numeric vector

  `proud`
      a numeric vector

  `quiescent`
      a numeric vector

  `quiet`
      a numeric vector

  `relaxed`
      a numeric vector

  `sad`
      a numeric vector

  `satisfied`
      a numeric vector

  `scared`
      a numeric vector

  `serene`
      a numeric vector

  `sleepy`
      a numeric vector

  `sluggish`
      a numeric vector

  `sociable`
      a numeric vector

  `sorry`
      a numeric vector

  `still`
      a numeric vector

  `strong`
      a numeric vector

  `surprised`
      a numeric vector

  `tense`
      a numeric vector

  `tired`
      a numeric vector

  `tranquil`
      a numeric vector

  `unhappy`
      a numeric vector

  `upset`
      a numeric vector

  `vigorous`
      a numeric vector

  `wakeful`
      a numeric vector

  `warmhearted`
      a numeric vector

  `wide.awake`
      a numeric vector

  `alone`
      a numeric vector

  `kindly`
      a numeric vector

  `scornful`
      a numeric vector

  `EA`
      Thayer's Energetic Arousal Scale

  `TA`
      Thayer's Tense Arousal Scale

  `PA`
      Positive Affect scale

  `NegAff`
      Negative Affect scale

  `Extraversion`
      Extraversion from the Eysenck Personality Inventory

  `Neuroticism`
      Neuroticism from the Eysenck Personality Inventory

  `Lie`
      Lie from the EPI

  `Sociability`
      The sociability subset of the Extraversion Scale

  `Impulsivity`
      The impulsivity subset of the Extraversions Scale

  `MSQ_Time`
      Time of day the data were collected

  `MSQ_Round`
      Rounded time of day

  `TOD`
      a numeric vector

  `TOD24`
      a numeric vector

  `ID`
      subject ID

  `condition`
      What was the experimental condition after the msq was given

  `scale`
      a factor with levels `msq` `r` original or revised msq

  `exper`
      Which study were the data collected: a factor with levels `AGES`
      `BING` `BORN` `CART` `CITY` `COPE` `EMIT` `FAST`
      `Fern` `FILM` `FLAT` `Gray` `imps` `item` `knob`
      `MAPS` `mite` `pat-1` `pat-2` `PATS` `post` `RAFT`
      `Rim.1` `Rim.2` `rob-1` `rob-2` `ROG1` `ROG2` `SALT`
      `sam-1` `sam-2` `SAVE/PATS` `sett` `swam` `swam-2`
      `TIME` `VALE-1` `VALE-2` `VIEW`

  Data collected at the Personality, Motivation, and Cognition Laboratory,
  Northwestern University.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `msq.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 3896 rows and 92 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'msq.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/psych/msq.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='msq.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
