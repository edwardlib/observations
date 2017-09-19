from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import os
import zipfile

from observations.util import maybe_download_and_extract


def celeba(path):
  """Load the Large-scale CelebFaces Attributes (CelebA) data set
  [@liu2015faceattributes]. It consists of ~200,000 178x218 RGB
  images, each with 40 annotated attributes, and with a total of
  ~10,000 identities. Here we load only the images.

  Args:
    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there. Filename is `img_align_celeba/`.

  Returns:
    str. It is a message advising to load data manually.
  """
  path = os.path.expanduser(path)
  if not os.path.exists(os.path.join(path, 'img_align_celeba')):
    url = 'https://docs.google.com/uc?export=download&' \
          'id=0B7EVK8r0v71pZjFTYXZWM3FlRnM'
    maybe_download_and_extract(path, url,
                               save_file_name='img_align_celeba.zip')
  string = "Data set is larger than 1 GB. We recommend loading your " \
           "data in batches."
  return string
