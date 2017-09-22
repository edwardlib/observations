from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cancer_survival import cancer_survival


def test_cancer_survival():
  """Test module cancer_survival.py by downloading
   cancer_survival.csv and testing shape of
   extracted data has 64 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cancer_survival(test_path)
  try:
    assert x_train.shape == (64, 2)
  except:
    shutil.rmtree(test_path)
    raise()
