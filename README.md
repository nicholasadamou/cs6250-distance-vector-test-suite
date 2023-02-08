# CS6250 Distance Vector Test Suite

*Tests your Bellman Ford algorithm against the official solutions provided by the CS6250 TAs.*

## What does it do?

It will parse the solution for the selected topology you've chosen. It will sort each distance vector within the solution alphabetically so that we have a common base to compare to later. Then, it will then execute `run.sh` against your topology. From here, it will obtain the final round from your execution and perform the same sorting as mentioned previously. Next, it will compare both the solution and your test and acknowledge if your test passed or failed. Finally, it will clean up any log files the test suite generated.

## How were the solutions sourced?

The solutions were sourced from the *Part 5: Correct Logs for Provided Topologies* section of the project 2 official write-up. These solutions are the official solutions provided by the TAs for project 2.

## Debug mode?

Yes, this test suite has a debug mode; change the boolean `DEBUG` to `True` to allow debug messages to appear in your console.

## How do I download it?

Clone this repository into your `DistanceVector` directory.

```bash
git clone \
 https://github.com/nicholasadamou/cs6250-distance-vector-test-suite \
 test-suite
```

## How do I use it?

From within the `test-suite` directory, run the following command:

```bash
# python3 tester.py {name of topology here}

python3 tester.py SimpleTopo

# If no topology is specified it will default to use all topologies.
# By 'all' I mean each topology provided in the solutions directory.
# These solutions are the official solutions provided by the TAs for
# project 2.

python3 tester.py
```

## Example Output

```bash
$ python3 tester.py SimpleTopo
[✓] Test passed for topology SimpleTopo
```

```bash
$ python3 tester.py
[!] Topology file not specified.
[*] Defaulting to ALL ['SingleLoopTopo', 'ComplexTopo', 'SimpleNegativeCycleTopo', 'SimpleTopo'].

[✓] Test passed for topology SingleLoopTopo
[X] Test failed for topology ComplexTopo
[X] Test failed for topology SimpleNegativeCycleTopo
[✓] Test passed for topology SimpleTopo
```
