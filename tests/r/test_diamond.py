from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.diamond import diamond


def test_diamond():
  """Test module diamond.py by downloading
   diamond.csv and testing shape of
   extracted data has 308 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = diamond(test_path)
  try:
    assert x_train.shape == (308, 5)
  except:
    shutil.rmtree(test_path)
    raise()
