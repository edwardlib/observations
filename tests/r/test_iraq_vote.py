from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.iraq_vote import iraq_vote


def test_iraq_vote():
  """Test module iraq_vote.py by downloading
   iraq_vote.csv and testing shape of
   extracted data has 100 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = iraq_vote(test_path)
  try:
    assert x_train.shape == (100, 6)
  except:
    shutil.rmtree(test_path)
    raise()
