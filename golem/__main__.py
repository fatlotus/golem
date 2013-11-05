from runner import GolemRunner
import sys
import yaml

try:
  sys.exit(GolemRunner(
    **yaml.load(open('configuration.yaml'))
  ).run(*sys.argv))
except KeyboardInterrupt:
  sys.exit(0)