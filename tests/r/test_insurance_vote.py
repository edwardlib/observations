from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.insurance_vote import insurance_vote


def test_insurance_vote():
  """Test module insurance_vote.py by downloading
   insurance_vote.csv and testing shape of
   extracted data has 435 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = insurance_vote(test_path)
  try:
    assert x_train.shape == (435, 9)
  except:
    shutil.rmtree(test_path)
    raise()
