from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.urine import urine


def test_urine():
  """Test module urine.py by downloading
   urine.csv and testing shape of
   extracted data has 79 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = urine(test_path)
  try:
    assert x_train.shape == (79, 7)
  except:
    shutil.rmtree(test_path)
    raise()
