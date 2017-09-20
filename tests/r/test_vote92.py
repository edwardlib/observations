from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.vote92 import vote92


def test_vote92():
  """Test module vote92.py by downloading
   vote92.csv and testing shape of
   extracted data has 909 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = vote92(test_path)
  try:
    assert x_train.shape == (909, 9)
  except:
    shutil.rmtree(test_path)
    raise()
