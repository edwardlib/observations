from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.prestige import prestige


def test_prestige():
  """Test module prestige.py by downloading
   prestige.csv and testing shape of
   extracted data has 102 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = prestige(test_path)
  try:
    assert x_train.shape == (102, 6)
  except:
    shutil.rmtree(test_path)
    raise()
