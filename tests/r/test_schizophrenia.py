from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.schizophrenia import schizophrenia


def test_schizophrenia():
  """Test module schizophrenia.py by downloading
   schizophrenia.csv and testing shape of
   extracted data has 251 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = schizophrenia(test_path)
  try:
    assert x_train.shape == (251, 2)
  except:
    shutil.rmtree(test_path)
    raise()
