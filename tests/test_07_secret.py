"""Тесты задания 07: расшифровка секретного сообщения."""

import importlib

secret = importlib.import_module('07_secret')


def test_decrypted_phrase():
    assert secret.decrypt_message(secret.secret_message) == (
        'в бане веник дороже денег'
    )


def test_main_prints_decrypted_phrase(capsys):
    secret.main()
    out = capsys.readouterr().out
    assert 'в бане веник дороже денег' in out
