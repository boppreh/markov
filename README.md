markov
======

`markov` is a very simple implementation of the Markov chain algorithm.
It is useful for creating new data (especially text) from examples. For
example, you could give it a book's text and ask it to write a completely
new paragraph.

There are two ways to use this library:


predict(previous, length=1, prefix_size=2)
------------------------------------------

Given a list of items, predicts the next `length` items in the sequence.
`prefix_size` is a parameter to the algorithm that roughly dictates how
much of the original data should be used. A value of 0 will produce
completely random values sampled from the original data, while a value
of 2 or 3 may fool casual observers when generating text. The greater
the `prefix_size` value, the more data you need to avoid repetition.


class Markov
------------
The `Markov` class gives a more fine-grained control over the process.
You initialize it with the desired prefix size (see above for a description
of its function) and an optional data source. New data sources can be added
by using the `learn` method.

The method `chain(length=1, prefix=[])` generates a new chain of `length`
items, based on the data already given, and starting from `prefix`.

You can access the inner statistical model using the attribute `stats`, which
is in the format {prefix: {candidate: weight}}.
