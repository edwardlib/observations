from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.synth_te import synth_te


def test_synth_te():
  """Test module synth_te.py by downloading
   synth_te.csv and testing shape of
   extracted data has 1000 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = synth_te(test_path)
  try:
    assert x_train.shape == (1000, 3)
  except:
    shutil.rmtree(test_path)
    raise()
