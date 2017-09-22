from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lake_huron import lake_huron


def test_lake_huron():
  """Test module lake_huron.py by downloading
   lake_huron.csv and testing shape of
   extracted data has 98 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lake_huron(test_path)
  try:
    assert x_train.shape == (98, 2)
  except:
    shutil.rmtree(test_path)
    raise()
