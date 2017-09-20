from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.psych import psych


def test_psych():
  """Test module psych.py by downloading
   psych.csv and testing shape of
   extracted data has 26 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = psych(test_path)
  try:
    assert x_train.shape == (26, 4)
  except:
    shutil.rmtree(test_path)
    raise()
