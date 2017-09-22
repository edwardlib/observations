from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.youth_risk2009 import youth_risk2009


def test_youth_risk2009():
  """Test module youth_risk2009.py by downloading
   youth_risk2009.csv and testing shape of
   extracted data has 500 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = youth_risk2009(test_path)
  try:
    assert x_train.shape == (500, 6)
  except:
    shutil.rmtree(test_path)
    raise()
