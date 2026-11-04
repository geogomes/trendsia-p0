from app.__main__ import main


def test_versao_executa():
    assert main(["--versao"]) == 0
