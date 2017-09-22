from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.income_inequality import income_inequality


def test_income_inequality():
  """Test module income_inequality.py by downloading
   income_inequality.csv and testing shape of
   extracted data has 66 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = income_inequality(test_path)
  try:
    assert x_train.shape == (66, 22)
  except:
    shutil.rmtree(test_path)
    raise()
