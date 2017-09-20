from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rock_the_vote import rock_the_vote


def test_rock_the_vote():
  """Test module rock_the_vote.py by downloading
   rock_the_vote.csv and testing shape of
   extracted data has 85 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rock_the_vote(test_path)
  try:
    assert x_train.shape == (85, 6)
  except:
    shutil.rmtree(test_path)
    raise()
