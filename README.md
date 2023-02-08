# CS6250 Distance Vector Test Suite

*Tests your Bellman Ford algorithm against the official solutions provided by the CS6250 TAs*

## What does it do?

It will parse the solution for the selected topology you've chosen. It will sort each distance vector within the solution alphabetically so that we have a common base to compare to later. Then, it will then execute run.sh against your topology. From here, it will obtain the final round from your execution and perform the same sorting as mentioned previously. Next, it will compare both the solution and your test and acknowledge if your test passed or failed. Finally, it will clean up any log files the test suite generated.

## Debug mode?

Yes, this test suite has a debug mode, simply change the boolean `DEBUG` to `True` to allow debug messages to appear in your console.

## How to download it?

```bash
git clone https://github.com/nicholasadamou/cs6250-distance-vector-test-suite
```

## How do I use it?

Place the project files for project 2 in this directory.

This includes:

- run.sh
- run_topo.py
- Node.py
- output_validator.py
- helpers.py
- DistanceVector.py
- Topology.py
- SimpleNegativeCycleTopo.txt
- SingleLoopTopo.txt
- ComplexTopo.txt
- SimpleTopo.txt
- BadTopo.txt

Then, run the following command:

```bash
# python3 tester.py {name of topology here}

python3 tester.py SimpleTopo

# If no topology is specified it will default to use all topologies.
# By 'all' I mean each topology provided in the solutions directory.
# These solutions are the official solutions provided by the TAs for
# project 2.
```
