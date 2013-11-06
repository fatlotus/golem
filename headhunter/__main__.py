from runner import HunterRunner
import sys
import yaml
import os

try:
  config_file = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'configuration.yaml')
  sys.exit(HunterRunner(**yaml.load(open(config_file))).run(*sys.argv))
except KeyboardInterrupt:
  sys.exit(0)