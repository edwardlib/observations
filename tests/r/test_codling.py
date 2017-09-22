from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.codling import codling


def test_codling():
  """Test module codling.py by downloading
   codling.csv and testing shape of
   extracted data has 99 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = codling(test_path)
  try:
    assert x_train.shape == (99, 10)
  except:
    shutil.rmtree(test_path)
    raise()
