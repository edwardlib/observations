from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mcas import mcas


def test_mcas():
  """Test module mcas.py by downloading
   mcas.csv and testing shape of
   extracted data has 220 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mcas(test_path)
  try:
    assert x_train.shape == (220, 17)
  except:
    shutil.rmtree(test_path)
    raise()
