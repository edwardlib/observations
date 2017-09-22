from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.broken_marriage import broken_marriage


def test_broken_marriage():
  """Test module broken_marriage.py by downloading
   broken_marriage.csv and testing shape of
   extracted data has 20 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = broken_marriage(test_path)
  try:
    assert x_train.shape == (20, 4)
  except:
    shutil.rmtree(test_path)
    raise()
