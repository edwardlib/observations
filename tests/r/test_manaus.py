from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.manaus import manaus


def test_manaus():
  """Test module manaus.py by downloading
   manaus.csv and testing shape of
   extracted data has 1080 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = manaus(test_path)
  try:
    assert x_train.shape == (1080, 2)
  except:
    shutil.rmtree(test_path)
    raise()
