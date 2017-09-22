from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sample_fg import sample_fg


def test_sample_fg():
  """Test module sample_fg.py by downloading
   sample_fg.csv and testing shape of
   extracted data has 30 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sample_fg(test_path)
  try:
    assert x_train.shape == (30, 13)
  except:
    shutil.rmtree(test_path)
    raise()
