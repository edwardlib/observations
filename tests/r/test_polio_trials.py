from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.polio_trials import polio_trials


def test_polio_trials():
  """Test module polio_trials.py by downloading
   polio_trials.csv and testing shape of
   extracted data has 8 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = polio_trials(test_path)
  try:
    assert x_train.shape == (8, 6)
  except:
    shutil.rmtree(test_path)
    raise()
