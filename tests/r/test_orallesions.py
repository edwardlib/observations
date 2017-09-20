from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.orallesions import orallesions


def test_orallesions():
  """Test module orallesions.py by downloading
   orallesions.csv and testing shape of
   extracted data has 8 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = orallesions(test_path)
  try:
    assert x_train.shape == (8, 3)
  except:
    shutil.rmtree(test_path)
    raise()
