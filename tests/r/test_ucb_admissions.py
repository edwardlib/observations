from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ucb_admissions import ucb_admissions


def test_ucb_admissions():
  """Test module ucb_admissions.py by downloading
   ucb_admissions.csv and testing shape of
   extracted data has 24 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ucb_admissions(test_path)
  try:
    assert x_train.shape == (24, 4)
  except:
    shutil.rmtree(test_path)
    raise()
