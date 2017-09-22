from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.synth_tr import synth_tr


def test_synth_tr():
  """Test module synth_tr.py by downloading
   synth_tr.csv and testing shape of
   extracted data has 250 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = synth_tr(test_path)
  try:
    assert x_train.shape == (250, 3)
  except:
    shutil.rmtree(test_path)
    raise()
