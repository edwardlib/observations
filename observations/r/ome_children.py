# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def ome_children(path):
  """Tests of Auditory Perception in Children with OME

  Experiments were performed on children on their ability to differentiate
  a signal in broad-band noise. The noise was played from a pair of
  speakers and a signal was added to just one channel; the subject had to
  turn his/her head to the channel with the added signal. The signal was
  either coherent (the amplitude of the noise was increased for a period)
  or incoherent (independent noise was added for the same period to form
  the same increase in power).

  The threshold used in the original analysis was the stimulus loudness
  needs to get 75% correct responses. Some of the children had suffered
  from otitis media with effusion (OME).

  The `OME` data frame has 1129 rows and 7 columns:

  `ID`
      Subject ID (1 to 99, with some IDs missing). A few subjects were
      measured at different ages.

  `OME`
      `"low"` or `"high"` or `"N/A"` (at ages other than 30 and 60
      months).

  `Age`
      Age of the subject (months).

  `Loud`
      Loudness of stimulus, in decibels.

  `Noise`
      Whether the signal in the stimulus was `"coherent"` or
      `"incoherent"`.

  `Correct`
      Number of correct responses from `Trials` trials.

  `Trials`
      Number of trials performed.

  Background
  ~~~~~~~~~~

  The experiment was to study otitis media with effusion (OME), a very
  common childhood condition where the middle ear space, which is normally
  air-filled, becomes congested by a fluid. There is a concomitant
  fluctuating, conductive hearing loss which can result in various
  language, cognitive and social deficits. The term ‘binaural hearing’ is
  used to describe the listening conditions in which the brain is
  processing information from both ears at the same time. The brain
  computes differences in the intensity and/or timing of signals arriving
  at each ear which contributes to sound localisation and also to our
  ability to hear in background noise.

  Some years ago, it was found that children of 7–8 years with a history
  of significant OME had significantly worse binaural hearing than
  children without such a history, despite having equivalent sensitivity.
  The question remained as to whether it was the timing, the duration, or
  the degree of severity of the otitis media episodes during critical
  periods, which affected later binaural hearing. In an attempt to begin
  to answer this question, 95 children were monitored for the presence of
  effusion every month since birth. On the basis of OME experience in
  their first two years, the test population was split into one group of
  high OME prevalence and one of low prevalence.

  Sarah Hogan, Dept of Physiology, University of Oxford, via Dept of
  Statistics Consulting Service

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `ome_children.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 1097 rows and 7 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'ome_children.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/MASS/OME.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='ome_children.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
