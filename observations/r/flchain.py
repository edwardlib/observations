# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def flchain(path):
  """Assay of serum free light chain for 7874 subjects.

  This is a stratified random sample containing 1/2 of the subjects from a
  study of the relationship between serum free light chain (FLC) and
  mortality. The original sample contains samples on approximately 2/3 of
  the residents of Olmsted County aged 50 or greater.

  A data frame with 7874 persons containing the following variables.

  `age `
      age in years

  `sex`
      F=female, M=male

  `sample.yr`
      the calendar year in which a blood sample was obtained

  `kappa`
      serum free light chain, kappa portion

  `lambda`
      serum free light chain, lambda portion

  `flc.grp`
      the FLC group for the subject, as used in the original analysis

  `creatinine`
      serum creatinine

  `mgus`
      1 if the subject had been diagnosed with monoclonal gammapothy
      (MGUS)

  `futime`
      days from enrollment until death. Note that there are 3 subjects
      whose sample was obtained on their death date.

  `death`
      0=alive at last contact date, 1=dead

  `chapter`
      for those who died, a grouping of their primary cause of death by
      chapter headings of the International Code of Diseases ICD-9

  The primary investigator (A Dispenzieri) and statistician (T Therneau)
  for the study.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `flchain.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 7874 rows and 11 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'flchain.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/survival/flchain.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='flchain.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
