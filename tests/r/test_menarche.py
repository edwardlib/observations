from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.menarche import menarche


def test_menarche():
  """Test module menarche.py by downloading
   menarche.csv and testing shape of
   extracted data has 25 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = menarche(test_path)
  try:
    assert x_train.shape == (25, 3)
  except:
    shutil.rmtree(test_path)
    raise()
