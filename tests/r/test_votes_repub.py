from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.votes_repub import votes_repub


def test_votes_repub():
  """Test module votes_repub.py by downloading
   votes_repub.csv and testing shape of
   extracted data has 50 rows and 31 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = votes_repub(test_path)
  try:
    assert x_train.shape == (50, 31)
  except:
    shutil.rmtree(test_path)
    raise()
