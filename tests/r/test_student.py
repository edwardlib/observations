from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.student import student


def test_student():
  """Test module student.py by downloading
   student.csv and testing shape of
   extracted data has 9679 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = student(test_path)
  try:
    assert x_train.shape == (9679, 13)
  except:
    shutil.rmtree(test_path)
    raise()
