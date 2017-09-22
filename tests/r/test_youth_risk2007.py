from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.youth_risk2007 import youth_risk2007


def test_youth_risk2007():
  """Test module youth_risk2007.py by downloading
   youth_risk2007.csv and testing shape of
   extracted data has 13387 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = youth_risk2007(test_path)
  try:
    assert x_train.shape == (13387, 6)
  except:
    shutil.rmtree(test_path)
    raise()
