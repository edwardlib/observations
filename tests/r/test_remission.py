from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.remission import remission


def test_remission():
  """Test module remission.py by downloading
   remission.csv and testing shape of
   extracted data has 27 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = remission(test_path)
  try:
    assert x_train.shape == (27, 3)
  except:
    shutil.rmtree(test_path)
    raise()
