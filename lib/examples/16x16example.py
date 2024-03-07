from pyggle import Boggle
import timeit

if __name__ == "__main__":
    board = [["a", "q", "o", "a", "u", "s", "i", "e", "a", "r", "t", "u", "e", "l", "r", "o"],
            ["l", "n", "u", "c", "r", "s", "u", "r", "s", "d", "i", "r", "z", "t", "o", "m"],
            ["q", "c", "a", "c", "l", "o", "d", "q", "t", "y", "i", "y", "c", "r", "a", "v"],
            ["d", "e", "s", "m", "p", "a", "n", "t", "s", "e", "m", "t", "d", "e", "s", "t"],
            ["i", "t", "q", "e", "e", "t", "r", "o", "a", "b", "n", "o", "a", "h", "n", "a"],
            ["d", "n", "e", "c", "r", "p", "o", "l", "v", "n", "e", "z", "s", "m", "i", "m"],
            ["p", "l", "o", "r", "s", "s", "i", "s", "t", "t", "u", "g", "c", "t", "o", "g"],
            ["b", "a", "l", "v", "r", "i", "d", "n", "m", "o", "l", "s", "b", "a", "n", "v"],
            ["o", "j", "n", "a", "o", "y", "l", "o", "i", "f", "g", "a", "e", "s", "z", "a"],
            ["n", "m", "e", "l", "l", "s", "e", "n", "n", "p", "i", "r", "m", "c", "i", "n"],
            ["l", "s", "a", "l", "n", "m", "u", "c", "r", "l", "a", "r", "m", "b", "a", "m"],
            ["p", "e", "m", "h", "z", "a", "r", "n", "y", "e", "c", "l", "p", "e", "s", "r"],
            ["i", "s", "n", "o", "u", "s", "t", "a", "o", "s", "c", "e", "i", "c", "i", "o"],
            ["r", "d", "e", "a", "s", "d", "o", "l", "d", "l", "e", "s", "r", "l", "o", "m"],
            ["p", "g", "u", "r", "l", "v", "o", "c", "l", "s", "e", "r", "b", "m", "e", "m"],
            ["s", "i", "a", "s", "n", "a", "p", "r", "m", "u", "r", "h", "t", "o", "s", "c"]]

    boggle = Boggle(board)

    print(boggle.time_solve()) # roughly 26 seconds