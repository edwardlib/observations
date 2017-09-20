from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mental_health import mental_health


def test_mental_health():
  """Test module mental_health.py by downloading
   mental_health.csv and testing shape of
   extracted data has 36 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mental_health(test_path)
  try:
    assert x_train.shape == (36, 3)
  except:
    shutil.rmtree(test_path)
    raise()
