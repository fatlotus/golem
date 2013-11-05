from runner import GolemRunner
import sys
import yaml

try:
  config_file = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__, 'configuration.yaml' ))))
  sys.exit(GolemRunner(**yaml.load(open(config_file))).run(*sys.argv))
except KeyboardInterrupt:
  sys.exit(0)