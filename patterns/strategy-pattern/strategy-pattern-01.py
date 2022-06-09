"""
Strategy is a behavioral design pattern that turns a set of behaviors into
objects and makes them interchangable inside original context
"""
from __future__ import annotations
from abc import ABC, abstractmethod



class Context():
    """
    The context defines the interface of the interest to clients. 
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strtegy through the constructor, but
        also provides a setter to change it at runtime.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        print("Context: sorting data using the strategy")
        result = self.strategy.do_algorithm(['a', 'b', 'c', 'd', 'e'])
        print(','.join(result))


class Strategy(ABC):
    """
    The Strategy interface teclares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass



class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)



class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))



if __name__ == '__main__':
    # The client code picks a crate strategy and passes it to the context.
    # The client should be aware of the differences between strategies in oreder
    # to make the right choice.

    context = Context(ConcreteStrategyA())
    print('Client: strategy is set to normal sorting.')
    context.do_some_business_logic()
    print()

    context = Context(ConcreteStrategyB())
    print('Client: strategy is set to reversed sorting.')
    context.do_some_business_logic()
    print()


