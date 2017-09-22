from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.word_memory import word_memory


def test_word_memory():
  """Test module word_memory.py by downloading
   word_memory.csv and testing shape of
   extracted data has 40 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = word_memory(test_path)
  try:
    assert x_train.shape == (40, 4)
  except:
    shutil.rmtree(test_path)
    raise()
