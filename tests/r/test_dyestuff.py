from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.dyestuff import dyestuff


def test_dyestuff():
  """Test module dyestuff.py by downloading
   dyestuff.csv and testing shape of
   extracted data has 30 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = dyestuff(test_path)
  try:
    assert x_train.shape == (30, 2)
  except:
    shutil.rmtree(test_path)
    raise()
