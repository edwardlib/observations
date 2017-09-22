from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bomsoi import bomsoi


def test_bomsoi():
  """Test module bomsoi.py by downloading
   bomsoi.csv and testing shape of
   extracted data has 106 rows and 21 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bomsoi(test_path)
  try:
    assert x_train.shape == (106, 21)
  except:
    shutil.rmtree(test_path)
    raise()
