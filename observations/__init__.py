from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from observations.abalone import abalone
from observations.boston_housing import boston_housing
from observations.caltech101_silhouettes import caltech101_silhouettes
from observations.celeba import celeba
from observations.cifar10 import cifar10
from observations.cifar100 import cifar100
from observations.crabs import crabs
from observations.enwik8 import enwik8
from observations.fashion_mnist import fashion_mnist
from observations.insteval import insteval
from observations.iris import iris
from observations.karate import karate
from observations.lsun import lsun
from observations.mnist import mnist
from observations.nips import nips
from observations.ptb import ptb
from observations.sick import sick
from observations.small32_imagenet import small32_imagenet
from observations.small64_imagenet import small64_imagenet
from observations.snli import snli
from observations.stanford_sentiment_treebank import stanford_sentiment_treebank
from observations.svhn import svhn
from observations.text8 import text8
from observations.util import maybe_download_and_extract
from observations.wikitext2 import wikitext2
from observations.wikitext103 import wikitext103
from observations.wine import wine
from observations.yelp17 import yelp17

__version__ = '0.1.1'
VERSION = __version__
