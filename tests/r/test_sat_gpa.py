from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sat_gpa import sat_gpa


def test_sat_gpa():
  """Test module sat_gpa.py by downloading
   sat_gpa.csv and testing shape of
   extracted data has 24 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sat_gpa(test_path)
  try:
    assert x_train.shape == (24, 3)
  except:
    shutil.rmtree(test_path)
    raise()
