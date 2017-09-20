from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.first_year_gpa import first_year_gpa


def test_first_year_gpa():
  """Test module first_year_gpa.py by downloading
   first_year_gpa.csv and testing shape of
   extracted data has 219 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = first_year_gpa(test_path)
  try:
    assert x_train.shape == (219, 10)
  except:
    shutil.rmtree(test_path)
    raise()
