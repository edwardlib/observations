from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pulse import pulse


def test_pulse():
  """Test module pulse.py by downloading
   pulse.csv and testing shape of
   extracted data has 232 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pulse(test_path)
  try:
    assert x_train.shape == (232, 7)
  except:
    shutil.rmtree(test_path)
    raise()
