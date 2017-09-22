from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.voting import voting


def test_voting():
  """Test module voting.py by downloading
   voting.csv and testing shape of
   extracted data has 25 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = voting(test_path)
  try:
    assert x_train.shape == (25, 4)
  except:
    shutil.rmtree(test_path)
    raise()
