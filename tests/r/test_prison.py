from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.prison import prison


def test_prison():
  """Test module prison.py by downloading
   prison.csv and testing shape of
   extracted data has 714 rows and 45 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = prison(test_path)
  try:
    assert x_train.shape == (714, 45)
  except:
    shutil.rmtree(test_path)
    raise()
