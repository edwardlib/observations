from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bladdercancer import bladdercancer


def test_bladdercancer():
  """Test module bladdercancer.py by downloading
   bladdercancer.csv and testing shape of
   extracted data has 31 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bladdercancer(test_path)
  try:
    assert x_train.shape == (31, 3)
  except:
    shutil.rmtree(test_path)
    raise()
