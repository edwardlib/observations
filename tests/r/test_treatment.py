from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.treatment import treatment


def test_treatment():
  """Test module treatment.py by downloading
   treatment.csv and testing shape of
   extracted data has 2675 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = treatment(test_path)
  try:
    assert x_train.shape == (2675, 10)
  except:
    shutil.rmtree(test_path)
    raise()
