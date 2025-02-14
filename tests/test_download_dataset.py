from click.testing import CliRunner
from download_dataset import download, PROMPT_STRING


def test_download_ENV():
    """Test if the titanic data will be downloaded."""
    download_func_ENV("titanic")


def download_func_ENV(dataset):
    """This function wraps the download_dataset.download() and fill the prompt
    command generated by click with the value passed in the parameter input.

    Args:
        dataset (string): the dataset name
    """
    runner = CliRunner()
    result = runner.invoke(download, input=dataset)
    assert not result.exception
    assert result.output == f"{PROMPT_STRING}: {dataset}\nData downloaded!\n"


def test_nothing():
    """This is just a sample of test."""
    var = 1
    assert var == 1


def test_nothing2():
    """This is just a sample of test."""
    var2 = 1
    assert var2 == 1
