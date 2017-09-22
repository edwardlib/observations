from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.toxicity import toxicity


def test_toxicity():
  """Test module toxicity.py by downloading
   toxicity.csv and testing shape of
   extracted data has 38 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = toxicity(test_path)
  try:
    assert x_train.shape == (38, 10)
  except:
    shutil.rmtree(test_path)
    raise()
