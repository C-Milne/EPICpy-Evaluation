import re
import math


def calculate_stats(results_file_name):
    """
    :param results_file_name: String of file path to open
    :return:

    This function opens a results file and summarises the amount of problems solved per domain
    """
    file = open(results_file_name, 'r+')
    file_content = file.read()  # Read the file
    file.seek(0, 0)     # Move pointer to start of the file
    line_num = 1
    solved_problems = 0
    total_problems = 0
    domains = {}

    for line in file:   # Row in CSV file
        if line_num > 1:    # Check if we are looking at the header row
            solved = line[line.rfind(',') + 1:line.rfind('\\')]     # Get value in the last column of row
            problem_domain = line[:line.find('/')]      # Get value in the first column of row
            if solved.upper() == 'TRUE':
                solved_problems += 1
                commas = [m.start() for m in re.finditer(',', line)]    # Find all commas in row
                solve_time = float(line[commas[1] + 1:commas[2]])   # Locate solve time
                # Calculate score for problem using the IPC's scoring method
                if solve_time < 1:
                    problem_score = 1
                else:
                    problem_score = min(1, 1 - (math.log(solve_time) / math.log(1800)))
            else:
                problem_score = 0

            # If we have a new domain, create new entry in dictionary
            if problem_domain not in domains.keys():
                domains[problem_domain] = []
            domains[problem_domain].append(problem_score)   # Add score to list for domain
            total_problems += 1
        line_num += 1

    file.seek(0, 0)     # Move pointer back to start of file
    # Generate general summary string
    overview_string = "Total_Problems: {},Solved_Problems: {}, Percentage_Solved: {}\n".format(total_problems, solved_problems, (solved_problems / total_problems) * 100)

    total_score = 0
    domain_score_string = ""
    # For each domain, record the amount of problems attempted and score
    for domain in domains.keys():
        total_score += sum(domains[domain])
        # Domain Name (amount of problems attempted: score)
        domain_score_string += "{} ({}): {}\n".format(domain, len(domains[domain]), sum(domains[domain]))

    domain_score_string += "Total Score: {}\n".format(total_score)

    file.write(overview_string + domain_score_string + file_content)
    print(overview_string)
    file.close()


if __name__ == "__main__":
    calculate_stats('results/Hamming-Distance-seen-states-results.csv')
    # calculate_stats('Hamming-Distance-results.csv')
    # calculate_stats('Novelty_Facts_Only_Task-Method-Expand-0-results.csv')
    # calculate_stats('Novelty-results.csv')
    # calculate_stats('seen-state-breadth-first-results.csv')
    # calculate_stats('Tree-Distance-seen-states-results.csv')
