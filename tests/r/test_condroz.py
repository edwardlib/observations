from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.condroz import condroz


def test_condroz():
  """Test module condroz.py by downloading
   condroz.csv and testing shape of
   extracted data has 428 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = condroz(test_path)
  try:
    assert x_train.shape == (428, 2)
  except:
    shutil.rmtree(test_path)
    raise()
