from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.med_gpa import med_gpa


def test_med_gpa():
  """Test module med_gpa.py by downloading
   med_gpa.csv and testing shape of
   extracted data has 55 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = med_gpa(test_path)
  try:
    assert x_train.shape == (55, 11)
  except:
    shutil.rmtree(test_path)
    raise()
