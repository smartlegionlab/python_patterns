# Python Patterns

A collection of design patterns and idioms in Python.

***

## Current Patterns

__Creational Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [Abstract Factory](patterns/creational/abstract_factory.py) | use a generic function with specific factories |
| [Builder](patterns/creational/builder.py) | instead of using multiple constructors, builder  receives parameters and returns constructed objects |
| [Factory Method](patterns/creational/factory.py) | delegate a specialized function/method to create instances|
| [Prototype](patterns/creational/prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive) |
| [Singleton](patterns/creational/singleton.py) | Ensures that the class has only one instance, and provides a global access point to it. |

__Structural Patterns__:

| Pattern | Description |
|:-------:| ----------- |
| [Adapter](patterns/structural/adapter.py) | converts the interface of one class to the interface of another that clients expect. |
| [Bridge](patterns/structural/bridge.py) | a client-provider middleman to soften interface changes |
| [Composite](patterns/structural/composite.py) | lets clients treat individual objects and compositions uniformly |
| [Decorator](patterns/structural/decorator.py) | wrap functionality with other functionality in order to affect outputs |
| [Facade](patterns/structural/facade.py) | use one class as an API to a number of others |
| [Flyweight](patterns/structural/flyweight.py) | transparently reuse existing instances of objects with similar/identical state |
| [Proxy](patterns/structural/proxy.py) | an object funnels operations to something else |

__Behavior Patterns__:

|                                  Pattern                                  | Description |
|:-------------------------------------------------------------------------:| ----------- |
|              [Blackboard](patterns/behavioral/blackboard.py)              | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern. |
| [Chain Of Responsibility](patterns/behavioral/chain_of_responsibility.py) | apply a chain of successive handlers to try and process the data. |
|                 [Command](patterns/behavioral/command.py)                 | bundle a command and arguments to call later. |
|             [Interpreter](patterns/behavioral/interpreter.py)             | a behavioral design pattern that solves a frequently encountered but subject to change problem. |
|                [Iterator](patterns/behavioral/iterator.py)                | traverse a container and access the container's elements. |
|                [Mediator](patterns/behavioral/mediator.py)                | an object that knows how to connect other objects and act as a proxy. |
|                 [Memento](patterns/behavioral/memento.py)                 | generate an opaque token that can be used to go back to a previous state. |
|                [Observer](patterns/behavioral/observer.py)                | provide a callback for notification of events/changes to data. |
|                   [State](patterns/behavioral/state.py)                   | logic is organized into a discrete number of potential states and the next state that can be transitioned to. |
|                [Strategy](patterns/behavioral/strategy.py)                | selectable operations over the same data. |
|         [Template Method](patterns/behavioral/template_method.py)         |defines the basis of the algorithm and allows subclasses to override some of the steps in the algorithm, without changing its structure as a whole. |
|                 [Visitor](patterns/behavioral/visitor.py)                 | invoke a callback for all items of a collection. |

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

    # --------------------------------------------------------
    # Licensed under the terms of the BSD 3-Clause License
    # (see LICENSE for details).
    # Copyright © 2018-2024, A.A Suvorov
    # All rights reserved.
    # --------------------------------------------------------