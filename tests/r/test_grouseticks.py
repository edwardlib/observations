from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.grouseticks import grouseticks


def test_grouseticks():
  """Test module grouseticks.py by downloading
   grouseticks.csv and testing shape of
   extracted data has 403 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = grouseticks(test_path)
  try:
    assert x_train.shape == (403, 7)
  except:
    shutil.rmtree(test_path)
    raise()
