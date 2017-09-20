from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.va_lung_cancer import va_lung_cancer


def test_va_lung_cancer():
  """Test module va_lung_cancer.py by downloading
   va_lung_cancer.csv and testing shape of
   extracted data has 137 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = va_lung_cancer(test_path)
  try:
    assert x_train.shape == (137, 8)
  except:
    shutil.rmtree(test_path)
    raise()
