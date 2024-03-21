from typing import Any, Iterator, Sequence


class CycleIter:
    """
    Custom iterator that cycles through elements of a sequence indefinitely.

    Args:
        some_iter_object (Sequence[Any]): The sequence of elements to cycle through.

    Yields:
        Any: The next element in the sequence.
    """
    def __init__(self, some_iter_object: Sequence[Any]) -> None:
        """
        Initialize the CycleIter object.

        Args:
            some_iter_object (Sequence[Any]): The sequence of elements to cycle through.
        """
        self.iter_obj = some_iter_object
        self.index: int = 0

    def __iter__(self) -> Iterator[Any]:
        """
        Make the CycleIter object iterable.

        Returns:
            Iterator[Any]: Iterator object.
        """
        return self

    def __next__(self) -> Any:
        """
        Get the next element in the sequence.

        Returns:
            Any: The next element in the sequence.
        """
        if self.index == len(self.iter_obj):
            self.index = 0

        value: Any = self.iter_obj[self.index]
        self.index += 1
        return value


def main():
    """
    Main function to demonstrate the usage of CycleIter.
    """
    for item in CycleIter([1, 2, 3]):
        print(item)


if __name__ == "__main__":
    main()
