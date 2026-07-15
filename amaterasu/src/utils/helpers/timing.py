"""
Utilitário de Tempo de Execução

Decorator para medir tempo de execução de funções
"""
import functools
import time
from typing import Any, Callable


def medir_tempo(func: Callable) -> Callable:
    """
    Decorator que mede o tempo de execução de uma função

    Args:
        func: Função a decorar

    Returns:
        Função decorada com medição de tempo

    Exemplo:
        @medir_tempo
        def minha_funcao():
            time.sleep(2)

        minha_funcao()  # Printa: minha_funcao levou 2.00s
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        inicio = time.time()
        try:
            resultado = func(*args, **kwargs)
            tempo_decorrido = time.time() - inicio
            print(f'{func.__name__} levou {tempo_decorrido:.2f}s')
            return resultado
        except Exception as e:
            tempo_decorrido = time.time() - inicio
            print(f'{func.__name__} falhou após {tempo_decorrido:.2f}s: {e}')
            raise

    return wrapper
