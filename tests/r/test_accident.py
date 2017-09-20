from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.accident import accident


def test_accident():
  """Test module accident.py by downloading
   accident.csv and testing shape of
   extracted data has 40 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = accident(test_path)
  try:
    assert x_train.shape == (40, 5)
  except:
    shutil.rmtree(test_path)
    raise()
