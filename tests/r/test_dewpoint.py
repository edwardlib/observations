from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.dewpoint import dewpoint


def test_dewpoint():
  """Test module dewpoint.py by downloading
   dewpoint.csv and testing shape of
   extracted data has 72 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = dewpoint(test_path)
  try:
    assert x_train.shape == (72, 3)
  except:
    shutil.rmtree(test_path)
    raise()
