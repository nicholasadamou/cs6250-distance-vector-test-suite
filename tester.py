import os
import sys
import subprocess

DEBUG = True

TOPOLOGIES = ",".join(
    file[:-4] if file.endswith(".log") else '' for file in os.listdir("solutions")
    ).split(",")

def clean_up(executed_tests):
    for topology in executed_tests:
        if not os.path.exists(topology + ".log"):
            continue

        os.remove(topology + ".log")

        if DEBUG:
            print("\nDeleted output file: {}".format(topology + ".log"))

def compare_solutions(executed_tests, solutions):
    for topology in executed_tests:
        executed_test = executed_tests[topology]

        solution = solutions[topology]

        if executed_test == solution:
            print("Test passed for topology {}".format(topology))

            return

        print("Test failed for topology {}".format(topology))

def parse_solutions(topologies):
    parsed_solutions = dict()

    for topology in topologies:
        if DEBUG:
            print("\nParsing Solution for Topology: {}\n".format(topology))

        # Read the corresponding solution file from solutions/{topology}.log

        solution_file = open("solutions/" + topology + ".log", "r")

        solution = ""

        for line in solution_file:
            components = line.split(":")

            node = components[0].strip()

            if DEBUG:
                print("node: {}".format(node))

            distance_vector = components[1].strip()

            if DEBUG:
                print("distance vector: {}".format(distance_vector))

            sorted_distance_vector = sorted(distance_vector.split(","))

            if DEBUG:
                print("*sorted* distance vector: {}".format(sorted_distance_vector))

            solution += node + ":" + ",".join(sorted_distance_vector) + "\n"

        if DEBUG:
            print()
            print("Solution")
            print("--------")
            print("{}".format(solution))
            print("--------")

        parsed_solutions[topology] = solution

    return parsed_solutions

def execute_tests(topologies):
    executed_tests = dict()

    for topology in topologies:
        if DEBUG:
            print("\nExecuting Test on Topology: {}\n".format(topology))

        # Execute run.sh with topology file name

        process = subprocess.Popen(["./run.sh", topology], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait until process is finished

        process.wait()

        output_file = open(topology + ".log", "r")

        test_dict = dict()
        rounds = 1

        # Read output file line by line

        for line in output_file:
            if line == "-----\n":
                rounds += 1

                continue

            if test_dict.get(rounds) is None:
                test_dict[rounds] = ""

            test_dict[rounds] += line

        num_rounds = len(test_dict)

        if DEBUG:
            print("Number of rounds: {}".format(num_rounds))

        final_round = test_dict[num_rounds]

        if DEBUG:
            print()
            print("Final round")
            print("-----------")
            print("{}".format(final_round))
            print("-----------")

        executed_tests[topology] = final_round

    return executed_tests

def main(args):
    topologies = []

    if len(args) == 1:
        print("Topology file not specified.")
        print("Defaulting to ALL topologies.")
        print()

        topologies = TOPOLOGIES

    else:
        topology = args[1]

        components = os.path.splitext(topology)

        topology = components[0]

        topologies.append(topology)

    if DEBUG:
        print("Selected topologies: {}".format(topologies))

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
