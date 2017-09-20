from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.frogs import frogs


def test_frogs():
  """Test module frogs.py by downloading
   frogs.csv and testing shape of
   extracted data has 212 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = frogs(test_path)
  try:
    assert x_train.shape == (212, 10)
  except:
    shutil.rmtree(test_path)
    raise()
