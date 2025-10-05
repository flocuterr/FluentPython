# def show_count(count: int,word:str) -> str:
#     if count == 1:
#         return f'1 {word}'
#     count_str = str(count) if count else 'no'
#     return f'{count_str} {word}s'

def show_count(count: int,singular:str, plural: str='') -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if plural:
        return f'{count} {plural}'
    return f'{count_str} {singular}s'

def test_irregular() -> None:
    got = show_count(2,'child','children')
from collections import abc

def double(x: abc.Sequence):
    return x * 2