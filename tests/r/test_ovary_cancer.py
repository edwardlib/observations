from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ovary_cancer import ovary_cancer


def test_ovary_cancer():
  """Test module ovary_cancer.py by downloading
   ovary_cancer.csv and testing shape of
   extracted data has 16 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ovary_cancer(test_path)
  try:
    assert x_train.shape == (16, 5)
  except:
    shutil.rmtree(test_path)
    raise()
