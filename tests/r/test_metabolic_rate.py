from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.metabolic_rate import metabolic_rate


def test_metabolic_rate():
  """Test module metabolic_rate.py by downloading
   metabolic_rate.csv and testing shape of
   extracted data has 305 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = metabolic_rate(test_path)
  try:
    assert x_train.shape == (305, 7)
  except:
    shutil.rmtree(test_path)
    raise()
