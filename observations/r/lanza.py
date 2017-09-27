# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def lanza(path):
  """Prevention of Gastointestinal Damages

  Data from four randomised clinical trials on the prevention of
  gastointestinal damages by Misoprostol reported by Lanza et al. (1987,
  1988a,b, 1989).

  A data frame with 198 observations on the following 3 variables.

  `study`
      a factor with levels `I`, `II`, `III`, and `IV` describing
      the study number.

  `treatment`
      a factor with levels `Misoprostol` `Placebo`

  `classification`
      an ordered factor with levels `1` < `2` < `3` < `4` < `5`
      describing an ordered response variable.

  F. L. Lanza (1987), A double-blind study of prophylactic effect of
  misoprostol on lesions of gastric and duodenal mucosa induced by oral
  administration of tolmetin in healthy subjects. *British Journal of
  Clinical Practice*, May suppl, 91–101.

  F. L. Lanza, R. L. Aspinall, E. A. Swabb, R. E. Davis, M. F. Rack, A.
  Rubin (1988a), Double-blind, placebo-controlled endoscopic comparison of
  the mucosal protective effects of misoprostol versus cimetidine on
  tolmetin-induced mucosal injury to the stomach and duodenum.
  *Gastroenterology*, **95**\ (2), 289–294.

  F. L. Lanza, K. Peace, L. Gustitus, M. F. Rack, B. Dickson (1988b), A
  blinded endoscopic comparative study of misoprostol versus sucralfate
  and placebo in the prevention of aspirin-induced gastric and duodenal
  ulceration. *American Journal of Gastroenterology*, **83**\ (2),
  143–146.

  F. L. Lanza, D. Fakouhi, A. Rubin, R. E. Davis, M. F. Rack, C. Nissen,
  S. Geis (1989), A double-blind placebo-controlled comparison of the
  efficacy and safety of 50, 100, and 200 micrograms of misoprostol QID in
  the prevention of ibuprofen-induced gastric and duodenal mucosal lesions
  and symptoms. *American Journal of Gastroenterology*, **84**\ (6),
  633–636.

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `lanza.csv`.

  Returns:

    Tuple of np.ndarray `x_train` with 198 rows and 3 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'lanza.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'http://dustintran.com/data/r/HSAUR/Lanza.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='lanza.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0,
                     parse_dates=True)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
