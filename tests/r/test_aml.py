from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aml import aml


def test_aml():
  """Test module aml.py by downloading
   aml.csv and testing shape of
   extracted data has 23 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aml(test_path)
  try:
    assert x_train.shape == (23, 3)
  except:
    shutil.rmtree(test_path)
    raise()
