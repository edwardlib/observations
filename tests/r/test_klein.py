from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.klein import klein


def test_klein():
  """Test module klein.py by downloading
   klein.csv and testing shape of
   extracted data has 22 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = klein(test_path)
  try:
    assert x_train.shape == (22, 10)
  except:
    shutil.rmtree(test_path)
    raise()
