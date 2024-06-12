import os
from typing import Union, List, Dict, Tuple
from timeit import timeit

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        return self._search_prefix(prefix) is not None

    def _search_prefix(self, prefix: str) -> Union[TrieNode, None]:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

class Boggle:
    def __init__(self, board: Union[List[List[str]], str], words: List[str] = None, official: bool = False):
        self.board = board
        self.words = words
        self.official = official
        self._solve_cache = None

        if not self.words:
            this_directory = os.path.abspath(os.path.dirname(__file__))
            words_alpha_path = os.path.join(this_directory, "data", "NWL2020_formatted.txt")
            
            with open(words_alpha_path, "r") as f:
                self.words = [word.strip() for word in f]

        if not self.__check_board():
            raise TypeError("Board must be a list of lists or string")
        
        if not self.__check_words():
            raise TypeError("Words must be a list of strings")
        
        if not self.__check_official():
            raise TypeError("Official must be a boolean")

        if isinstance(self.board, str):
            self.board = self.__bogglefy()

        self.trie = Trie(self.words)

    def __print__(self) -> None:
        self.print_board()

    def __str__(self) -> str:
        return self.__stringify()

    def __len__(self) -> int:
        return self.get_length()

    def __repr__(self) -> str:
        return f"Boggle({self.board}, {self.words}, {self.official})"

    def __getitem__(self, x: int) -> str:
        if isinstance(x, int) and 0 <= x < self.get_length():
            return self.board[x]
        raise IndexError("Index out of range")

    def __contains__(self, word: str) -> bool:
        return word in self.get_words()
    
    def solve(self) -> Dict[str, List[Tuple[int, int]]]:
        if self._solve_cache is not None:
            return self._solve_cache

        if self.official and self.get_length() < 3:
            return {}

        result = {}
        rows = len(self.board)
        cols = len(self.board[0])
        
        for i in range(rows):
            for j in range(cols):
                self.__search_from_cell(i, j, "", [], result)

        self._solve_cache = result
        return result

    def get_length(self) -> int:
        return len(self.board) * len(self.board[0])

    def get_words(self) -> List[str]:
        return list(self.solve().keys())

    def get_coords(self) -> List[Tuple[int, int]]:
        return list(self.solve().values())

    def time_solve(self) -> float:
        return timeit(self.solve, number=1)

    def print_result(self) -> None:
        if not self.solve():
            print("No words!")
            return

        for word, positions in self.solve().items():
            print(f"{word}: {positions}")

    def print_board(self) -> None:
        print(self.__stringify())

    def __check_board(self) -> bool:
        if isinstance(self.board, str):
            return True
        if isinstance(self.board, list) and all(isinstance(sublist, list) for sublist in self.board):
            return True
        return False

    def __check_words(self) -> bool:
        return isinstance(self.words, list)
    
    def __check_official(self) -> bool:
        return isinstance(self.official, bool)

    def __bogglefy(self) -> List[List[int]]:
        return [list(row) for row in self.board.split()]
    
    def __stringify(self) -> str:
        return "\n".join([" ".join(row) for row in self.board])

    def __search_from_cell(self, x: int, y: int, prefix: str, positions: List[Tuple[int, int]], result: Dict) -> None:
        if (y, x) in positions:
            return

        if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]):
            return

        char = self.board[x][y]
        prefix += char

        if not self.trie.starts_with(prefix):
            return

        positions.append((y, x))

        if self.trie.search(prefix):
            if not self.official or len(prefix) >= 3:
                result[prefix] = positions[:]

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                self.__search_from_cell(x + i, y + j, prefix, positions, result)

        positions.pop()

