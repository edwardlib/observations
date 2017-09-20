from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sat_act import sat_act


def test_sat_act():
  """Test module sat_act.py by downloading
   sat_act.csv and testing shape of
   extracted data has 700 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sat_act(test_path)
  try:
    assert x_train.shape == (700, 6)
  except:
    shutil.rmtree(test_path)
    raise()
