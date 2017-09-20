from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.consump import consump


def test_consump():
  """Test module consump.py by downloading
   consump.csv and testing shape of
   extracted data has 37 rows and 24 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = consump(test_path)
  try:
    assert x_train.shape == (37, 24)
  except:
    shutil.rmtree(test_path)
    raise()
