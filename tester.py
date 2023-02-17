import os
import sys
import subprocess

DEBUG = False

TOPOLOGIES = ",".join(
    file[:-4] if file.endswith(".log") else '' for file in os.listdir("solutions")
).split(",")

def sort(line):
    components = line.split(":")

    node = components[0].strip()

    if DEBUG:
        print(f"node: {node}")

    distance_vector = components[1].strip()

    if DEBUG:
        print(f"distance vector: {distance_vector}")

    sorted_distance_vector = sorted(distance_vector.split(","))

    if DEBUG:
        print(f"*sorted* distance vector: {sorted_distance_vector}")

    return f"{node}:" + ",".join(sorted_distance_vector) + "\n"

def clean_up(executed_tests):
    for topology in executed_tests:
        if not os.path.exists(f"{topology}.log"):
            continue

        os.remove(f"{topology}.log")

        if DEBUG:
            print(f"\n[!] Deleted output file: {topology}.log")

def compare_solutions(executed_tests, solutions):
    for topology in executed_tests:
        executed_test = executed_tests[topology]

        solution = solutions[topology]

        if executed_test == solution:
            print(f"[✓] Test passed for topology {topology}")

            continue

        print(f"[X] Test failed for topology {topology}")

def parse_solutions(topologies):
    parsed_solutions = {}

    for topology in topologies:
        if DEBUG:
            print(f"\nParsing Solution for Topology: {topology}\n")

        # Read the corresponding solution file from solutions/{topology}.log

        solution_file = open(f"solutions/{topology}.log", "r")

        solution = "".join(sort(line) for line in solution_file)
        if DEBUG:
            print()
            print("Solution")
            print("--------")
            print(f"{solution}")
            print("--------")

        parsed_solutions[topology] = solution

    return parsed_solutions

def execute_tests(topologies):
    executed_tests = {}

    for topology in topologies:
        if DEBUG:
            print(f"\nExecuting Test on Topology: {topology}\n")

        # Execute run.sh with topology file name

        process = subprocess.Popen(
            ["./run.sh", topology],
            stdout=subprocess.DEVNULL,
        )

        # Wait until process is finished

        process.wait()

        # Check if process exited with error

        if process.returncode != 0:
            print(f"[X] Error executing run.sh against topology {topology}")

            continue

        output_file = open(f"{topology}.log", "r")

        test_dict = {}
        rounds = 1

        # Read output file line by line

        for line in output_file:
            if line == "-----\n":
                rounds += 1

                continue

            if test_dict.get(rounds) is None:
                test_dict[rounds] = ""

            test_dict[rounds] += sort(line)

        num_rounds = len(test_dict)

        if DEBUG:
            print(f"Number of rounds: {num_rounds}")

        final_round = test_dict[num_rounds]

        if DEBUG:
            print()
            print("Final round")
            print("-----------")
            print(f"{final_round}")
            print("-----------")

        executed_tests[topology] = final_round

    return executed_tests

def main(args):
    topologies = []

    if len(args) == 1:
        print("[!] Topology file not specified.")
        print(f"[*] Defaulting to ALL {TOPOLOGIES}.")
        print()

        topologies = TOPOLOGIES

    else:
        topology = args[1]

        components = os.path.splitext(topology)

        topology = components[0]

        topologies.append(topology)

    if DEBUG:
        print(f"[*] Selected topologies: {topologies}")

    # Parse solutions

    parsed_solutions = parse_solutions(topologies=topologies)

    # Execute test

    executed_tests = execute_tests(topologies=topologies)

    # Compare solutions

    compare_solutions(executed_tests, parsed_solutions)

    # Delete output files

    clean_up(executed_tests)


if __name__ == "__main__":
    main(sys.argv)
