from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.chest_sizes import chest_sizes


def test_chest_sizes():
  """Test module chest_sizes.py by downloading
   chest_sizes.csv and testing shape of
   extracted data has 16 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = chest_sizes(test_path)
  try:
    assert x_train.shape == (16, 2)
  except:
    shutil.rmtree(test_path)
    raise()
