from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pneumon import pneumon


def test_pneumon():
  """Test module pneumon.py by downloading
   pneumon.csv and testing shape of
   extracted data has 3470 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pneumon(test_path)
  try:
    assert x_train.shape == (3470, 15)
  except:
    shutil.rmtree(test_path)
    raise()
