from runner import GolemRunner
import sys
import yaml

sys.exit(GolemRunner(
  **yaml.load(open('configuration.yaml'))
).run(*sys.argv))