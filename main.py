from pathlib import Path

from datasets import load_dataset

cwd = Path().cwd()
assert cwd.name == "workdir"

dataset = list(load_dataset("walledai/AdvBench")["train"]["prompt"])
