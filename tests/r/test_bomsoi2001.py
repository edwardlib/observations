from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bomsoi2001 import bomsoi2001


def test_bomsoi2001():
  """Test module bomsoi2001.py by downloading
   bomsoi2001.csv and testing shape of
   extracted data has 102 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bomsoi2001(test_path)
  try:
    assert x_train.shape == (102, 15)
  except:
    shutil.rmtree(test_path)
    raise()
