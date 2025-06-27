"""Module basic pour tester le CI/CD"""


class SimpleMath:
    """Class pour implementer des fonctions basic de math."""

    def __init__(self):
        pass

    @staticmethod
    def add(a: int, b: int) -> int:
        """Addition de int deux entier ensemble.

        Args:
            a (int): First number to add
            b (int): Second number to add

        Returns:
            int: The sum of a and b
        """
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        """Soustraction d'un entier et un autre.

         Args:
             a (int): Number to subtract from
             b (int): Number to subtract

         Returns:
             int: The result of a minus b
         """

        return a - b
