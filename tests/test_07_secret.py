"""Тесты задания 07: расшифровка секретного сообщения."""

# Позволяет запускать файл напрямую: python tests/test_XX.py
# Корень проекта добавляется в sys.path независимо от pytest.ini
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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


# Прямой запуск: python tests/test_XX.py -> тесты выполняются через pytest
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
