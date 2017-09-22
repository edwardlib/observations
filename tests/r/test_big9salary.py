from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.big9salary import big9salary


def test_big9salary():
  """Test module big9salary.py by downloading
   big9salary.csv and testing shape of
   extracted data has 786 rows and 30 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = big9salary(test_path)
  try:
    assert x_train.shape == (786, 30)
  except:
    shutil.rmtree(test_path)
    raise()
