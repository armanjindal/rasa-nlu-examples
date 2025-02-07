import pytest

from rasa.train import train_nlu

# Take heed! Pytest fails if you use a function that starts with "test"
from rasa.test import test_nlu as run_nlu


english_yml_files = [
    "printer-config.yml",
    "stanza-tokenizer-config.yml",
    "fasttext-config.yml",
    "bytepair-config.yml",
    "gensim-config.yml",
    "semantic_map-config.yml",
    "lang-detect-ft-config.yml",
    "sparse-naive-bayes-intent-classifier-config.yml",
    "flashtext-config.yml",
]


@pytest.mark.fasttext
@pytest.mark.parametrize("fp", english_yml_files)
def test_run_train_test_command_english(fp):
    if "flashtext" in fp:
        nlu_data = "tests/data/nlu/en/nlu_w_lookups.md"
    else:
        nlu_data = "tests/data/nlu/en/nlu.md"
    mod = train_nlu(
        nlu_data=nlu_data,
        config=f"tests/configs/{fp}",
        output="models",
    )
    run_nlu(model=f"models/{mod}", nlu_data="tests/data/nlu/en/nlu.md")
